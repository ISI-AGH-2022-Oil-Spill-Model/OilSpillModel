from applicators.i_applicator import IApplicator
from model.model import MIN_OIL_LEVEL, Model
from model.cell import CellType


class DispersionApplicator(IApplicator):

    def __init__(self, dispersion_modifier, diagonal_constant):
        self.D = dispersion_modifier
        self.d = diagonal_constant

    def apply(self, model: Model):

        for row in model.active_cells():
            for cell in row:
                if cell.type == CellType.EARTH or cell.oil_level <= MIN_OIL_LEVEL:
                    continue
                
                for i, neighbour in enumerate(cell.neighbours):
                    if neighbour is None or neighbour.type == CellType.EARTH:
                        continue

                    next_tile_oil_level = 0
                    if neighbour != None:
                        if neighbour.oil_level > cell.oil_level:
                            continue
                        next_tile_oil_level = neighbour.oil_level
                        
                    change = (cell.oil_level - next_tile_oil_level) * self.D

                    if i % 2 == 0:
                        change *= self.d

                    cell.oil_change -= change
                    if neighbour != None:
                        neighbour.oil_change += change
