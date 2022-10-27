from applicators.i_applicator import IApplicator
from model.model import Model
from model.cell import CellType


class DispersionApplicator(IApplicator):

    def __init__(self, dispersion_modifier, diagonal_constant):
        self.D = dispersion_modifier
        self.d = diagonal_constant
        self.eps = 1e-4

    def apply(self, model: Model):

        for row in model.cells:
            for cell in row:
                if cell.type == CellType.EARTH or cell.oil_level <= self.eps:
                    continue
                change = cell.oil_level * self.D

                for i, neighbour in enumerate(cell.neighbours):
                    if neighbour == None:
                        continue
                    if neighbour.type == CellType.EARTH:
                        continue
                    if neighbour.oil_level > cell.oil_level:
                        continue

                    is_diagonal = i % 2 == 0
                    if is_diagonal:
                        cell.oil_change -= change * self.d
                        neighbour.oil_change += change * self.d
                    else:
                        cell.oil_change -= change 
                        neighbour.oil_change += change

