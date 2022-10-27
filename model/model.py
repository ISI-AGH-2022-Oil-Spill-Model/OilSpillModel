from types import CellType
import numpy as np
import pygame
from model.cell import Cell, CellType

from model.change_matrix import ChangeMatrix
from view.colors import Color
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

    def draw(self, window: pygame.Surface):
        """Draws square grid with colored spots."""
        window.fill(Color.tea_green)
        for row in self.cells:
            for cell in row:
                cell.draw(window)
        self._draw_grid(window)


    def _update_neighbours(self):
        for row in self.cells:
            for cell in row:
                cell.update_neighbours(self.cells)


    def _draw_grid(self, window):
        """Draws square grid."""
        height, width = self.shape
        for row_idx in range(height):
            pygame.draw.line(window, Color.dark_green, (0, row_idx * self.cell_size), (height * self.cell_size, row_idx * self.cell_size))
            for col_idx in range(width):
                pygame.draw.line(window, Color.dark_green, (col_idx * self.cell_size, 0), (col_idx * self.cell_size, width * self.cell_size))

    def fill_cells(self, map_init: MapInitializer):
        self.cells = map_init.get_cell_array(self.cell_size)

