from applicators.i_applicator import IApplicator
from model.model_constants import MIN_OIL_LEVEL
from model.cell import Cell


class VaporPhotoApplicator(IApplicator):

    def __init__(self, vaporization_modifier, photolysis_modifier):
        self.V = vaporization_modifier
        self.P = photolysis_modifier

    def apply(self, cell: Cell):

        cell.oil_change -= max(MIN_OIL_LEVEL, cell.oil_level) * (self.V + self.P)
