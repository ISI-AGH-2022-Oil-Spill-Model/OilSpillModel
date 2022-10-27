import numpy as np

from applicators.i_applicator import IApplicator
from model.change_matrix import ChangeMatrix
from model.model import Model
from model.cell import Cell
from model.cell import CellType


class DispersionApplicator(IApplicator):

    def __init__(self, diagonal_dispersion_modifier, cross_dispersion_constant):
        self.D = diagonal_dispersion_modifier
        self.C = cross_dispersion_constant

    def apply(self, model: Model, change_matrix: ChangeMatrix):

        for cells in model.cells:
            for cell in cells:
                if cell.type == CellType.EARTH:
                    continue
                cross_cells = np.array([], dtype=np.dtype(object))
                for neighbour in cell.neighbours[[1, 3, 5, 7]]:
                    if neighbour is not None and neighbour.type != CellType.EARTH:
                        cross_cells = np.append(cross_cells, neighbour)

                diagonal_cells = np.array([], dtype=np.dtype(object))
                for neighbour in cell.neighbours[[0, 2, 4, 6]]:
                    if neighbour is not None and neighbour.type != CellType.EARTH:
                        diagonal_cells = np.append(diagonal_cells, neighbour)

                c_change = cell.oil_level * self.C / 4
                c_count = len(cross_cells)
                d_change = cell.oil_level * self.D / 4
                d_count = len(diagonal_cells)

                # If change is too high decrease it
                while c_change + d_change > cell.oil_level:
                    c_change *= 0.5
                    d_change *= 0.5

                cell.oil_change -= c_change * c_count + d_change * d_count

                for neighbour in cross_cells:
                    neighbour.oil_change += c_change

                for neighbour in diagonal_cells:
                    neighbour.oil_change += d_change
