from applicators.i_applicator import IApplicator
from model.cell import Cell, CellType


class OilLeakApplicator(IApplicator):

    def __init__(self, leak_rate: float, max_leaks_from_all_sources: int):
        self.leak_rate = leak_rate
        self.max_iters = max_leaks_from_all_sources
        self.iters = 0

    def apply(self, cell: Cell, model=None):

        if self.max_iters <= self.iters:
            cell.type = CellType.WATER
            return
        if cell.type == CellType.OIL_SOURCE:
            model.oil_spilled += self.leak_rate
            cell.oil_change += self.leak_rate
            self.iters += 1
        
            