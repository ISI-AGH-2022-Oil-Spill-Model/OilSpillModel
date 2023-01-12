from model.model import Model
from applicators.i_applicator import IApplicator
from model.model_constants import MIN_OIL_LEVEL
from model.cell import CellType


class BulkApplicator:
    def __init__(self, applicators: list[IApplicator]) -> None:
        self.applicators = applicators

    def bulk_apply(self, model: Model):
        for row in model.active_cells():
            for cell in row:
                if cell.type == CellType.EARTH or (cell.type == CellType.WATER and cell.oil_level <= MIN_OIL_LEVEL):
                    continue
                for applicator in self.applicators:
                    applicator.apply(cell, model)

