from applicators.i_applicator import IApplicator
from model.cell import Cell, CellType


class OilLeakApplicator(IApplicator):

    def __init__(self, leak_rate: float, once: bool):
        self.leak_rate = leak_rate
        self.once = once
        self.applied = False

    def apply(self, cell: Cell):

        if self.once and self.applied:
            return
        if cell.type == CellType.OIL_SOURCE:
            cell.oil_change += self.leak_rate
            self.applied = True
            