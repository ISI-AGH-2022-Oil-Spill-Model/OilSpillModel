from types import CellType
import numpy as np
from model.cell import Cell, CellType

from model.change_matrix import ChangeMatrix
from data.map_intializer import MapInitializer


class Model:

    def __init__(self, shape: tuple, cell_size: int):
        self.shape = shape
        self.cell_size = cell_size
        self.cells = np.empty(shape, dtype=np.dtype(object))

    def apply_change(self, change_matrix: ChangeMatrix):
        pass

    def init_surface(self, kind: str):
        if kind == "ocean":
            height, width = self.shape
            for row_idx in range(height):
                for col_idx in range(width):
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

