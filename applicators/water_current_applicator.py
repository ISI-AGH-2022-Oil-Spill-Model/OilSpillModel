from applicators.i_applicator import IApplicator
from model.model import Model
from model.cell import CellType


class WaterCurrentApplicator(IApplicator):

    def __init__(self, speed_modifier):
        self.speed_modifier = speed_modifier
        self.eps = 1e-4

    def apply(self, model: Model):

        for row in model.cells:
            for cell in row:
                if cell.type == CellType.EARTH or cell.oil_level <= self.eps:
                    continue

                if cell.current_direction != -1:
                    neighbour = cell.neighbours[cell.current_direction]
                    if neighbour.type == CellType.EARTH:
                        continue

                    change = self.speed_modifier * cell.current_speed * cell.oil_level
                    cell.oil_level -= change
                    neighbour.oil_level += change
