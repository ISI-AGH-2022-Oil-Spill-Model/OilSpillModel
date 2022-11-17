from applicators.i_applicator import IApplicator
from model.model_constants import MIN_OIL_LEVEL
from model.cell import Cell, CellType


class DispersionApplicator(IApplicator):

    def __init__(self, dispersion_modifier, diagonal_constant):
        self.D = dispersion_modifier
        self.d = diagonal_constant

    def apply(self, cell: Cell):
        for i, neighbour in enumerate(cell.neighbours):
            if neighbour is None or neighbour.type == CellType.EARTH:
                continue
            if neighbour.oil_level > cell.oil_level:
                continue

            change = (cell.oil_level - neighbour.oil_level) * self.D

            if i % 2 == 0:
                change *= self.d

            cell.oil_change -= change
            neighbour.oil_change += change
