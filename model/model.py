from types import CellType
import numpy as np
from model.cell import Cell, CellType

from data.map_intializer import MapInitializer
from model.model_constants import MIN_OIL_LEVEL



class Model:

    def __init__(self, shape: tuple, cell_size: int):
        self.shape = shape
        self.cell_size = cell_size
        self.cells = np.empty(shape, dtype=np.dtype(object))
        self.__active_cells_border = np.array([shape[0], shape[1], 0, 0], dtype=int)
        self.__active_cells = None
        self.oil_spilled = 0

    def active_cells(self):
        if self.__active_cells is None:
            self.__active_cells = self.cells[self.__active_cells_border[0]: self.__active_cells_border[2] + 1,
                                  self.__active_cells_border[1]: self.__active_cells_border[3] + 1]
        return self.__active_cells

    def get_active_cells_with_border(self, border: int):
        top = max(0, self.__active_cells_border[0] - border)
        left = max(0, self.__active_cells_border[1] - border)
        bottom = min(self.shape[0] - 1, self.__active_cells_border[2] + 1 + border)
        right = min(self.shape[1] - 1, self.__active_cells_border[3] + 1 + border)
        return self.cells[top: bottom, left: right]

    def apply_change(self):
        self.__active_cells = None
        for y, row in enumerate(self.get_active_cells_with_border(3)):
            for x, cell in enumerate(row):
                if cell.oil_change != 0:
                    cell.merge_change()
                    cell.update_color_by_oil_level()
                    self.__update_active_cells_border(cell, y, x)
                

    def init_surface(self, kind: str):
        if kind == "ocean":
            height, width = self.shape
            for row_idx in range(height):
                for col_idx in range(width):
                    if row_idx == height // 2 and col_idx == width // 2:
                        self.cells[row_idx][col_idx] = Cell(CellType.OIL_SOURCE, self.cell_size, row_idx, col_idx)
                        continue
                    self.cells[row_idx][col_idx] = Cell(CellType.WATER, self.cell_size, row_idx, col_idx)
            self.__update_neighbours()
            self.__clear_and_update_active_cells_border()
            return

        raise NotImplementedError

    def update_current(self, directions, speed):
        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                cell.update_current_direction(directions[i][j])
                cell.update_current_speed(speed[i][j])

    def update_wind(self, directions, speed):
        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                cell.update_wind_direction(directions[i][j])
                cell.update_wind_speed(speed[i][j])

    def __update_neighbours(self):
        for row in self.cells:
            for cell in row:
                cell.update_neighbours(self.cells)

    def fill_cells(self, map_init: MapInitializer):
        self.cells = map_init.get_cell_array(self.cell_size)
        self.__update_neighbours()
        self.__clear_and_update_active_cells_border()

    def __clear_and_update_active_cells_border(self):
        self.__active_cells = None
        for y, row in enumerate(self.cells):
            for x, cell in enumerate(row):
                self.__update_active_cells_border(cell, y, x)

    def __update_active_cells_border(self, cell, y, x):
        if cell.type == CellType.OIL_SOURCE or cell.oil_level >= MIN_OIL_LEVEL:
            self.__active_cells_border[0] = min(y, self.__active_cells_border[0])
            self.__active_cells_border[1] = min(x, self.__active_cells_border[1])
            self.__active_cells_border[2] = max(y, self.__active_cells_border[2])
            self.__active_cells_border[3] = max(x, self.__active_cells_border[3])
