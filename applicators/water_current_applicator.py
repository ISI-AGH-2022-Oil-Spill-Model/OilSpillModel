from applicators.i_applicator import IApplicator
from model.model import MIN_OIL_LEVEL, Model
from model.cell import CellType


class WaterCurrentApplicator(IApplicator):

    def __init__(self, speed_modifier):
        self.speed_modifier = speed_modifier

    def apply(self, model: Model):
        for row in model.active_cells():
            for cell in row:
                if cell.type == CellType.EARTH or cell.oil_level <= MIN_OIL_LEVEL:
                    continue

                if cell.current_direction != -1:
                    neighbour = cell.neighbours[cell.current_direction]
                    if neighbour is None or neighbour.type == CellType.EARTH:
                        continue

                    change = self.speed_modifier * cell.current_speed * cell.oil_level
                    cell.oil_level -= change
                    neighbour.oil_level += change
