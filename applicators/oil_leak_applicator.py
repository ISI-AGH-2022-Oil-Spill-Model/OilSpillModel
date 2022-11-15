from applicators.i_applicator import IApplicator
from model.model import Model
from model.cell import CellType


class OilLeakApplicator(IApplicator):

    def __init__(self, leak_rate: float, once: bool):
        self.leak_rate = leak_rate
        self.once = once
        self.applied = False

    def apply(self, model: Model):

        if self.once and self.applied:
            return
        for row in model.active_cells():
            for cell in row:
                if cell.type == CellType.OIL_SOURCE:
                    cell.oil_change += self.leak_rate
                    self.applied = True
            
                        
