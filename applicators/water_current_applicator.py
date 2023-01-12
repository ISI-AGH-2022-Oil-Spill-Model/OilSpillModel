from applicators.i_applicator import IApplicator
from model.model_constants import MIN_OIL_LEVEL
from model.cell import Cell, CellType


class WaterCurrentApplicator(IApplicator):

    factors = [0.15, .7, 0.15]

    def __init__(self, speed_modifier):
        self.speed_modifier = speed_modifier

    def apply(self, cell: Cell, model=None):

        change_sum = 0

        for i, direction in enumerate(cell.current_directions):
            neighbour = cell.neighbours[direction]
            if neighbour is None or neighbour.type == CellType.EARTH:
                continue

            change = self.speed_modifier * cell.current_speed * cell.oil_level * WaterCurrentApplicator.factors[i]
            change_sum += change
            neighbour.oil_change += change

        cell.oil_level -= change_sum
