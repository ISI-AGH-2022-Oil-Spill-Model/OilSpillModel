from types import CellType
import numpy as np
from model.cell import Cell, CellType

from data.map_intializer import MapInitializer


class Model:

    def __init__(self, shape: tuple, cell_size: int):
        self.shape = shape
        self.cell_size = cell_size
        self.cells = np.empty(shape, dtype=np.dtype(object))

    def apply_change(self):
        for row in self.cells:
            for cell in row:
                cell.merge_change()
                cell.update_color_by_oil_level()

    def init_surface(self, kind: str):
        if kind == "ocean":
            height, width = self.shape
            for row_idx in range(height):
                for col_idx in range(width):
                    if row_idx == height // 2 and col_idx == width // 2:
                        self.cells[row_idx][col_idx] = Cell(CellType.OIL_SOURCE, self.cell_size, row_idx, col_idx)
                        continue
                    self.cells[row_idx][col_idx] = Cell(CellType.WATER, self.cell_size, row_idx, col_idx)
            self._update_neighbours()
            return
            
        raise NotImplementedError

    def _update_neighbours(self):
        for row in self.cells:
            for cell in row:
                cell.update_neighbours(self.cells)

    def fill_cells(self, map_init: MapInitializer):
        self.cells = map_init.get_cell_array(self.cell_size)
        self._update_neighbours()

