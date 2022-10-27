from applicators.i_applicator import IApplicator
from model.model import Model
from model.cell import CellType


class OilLeakApplicator(IApplicator):

    def __init__(self, leak_rate):
        self.leak_rate = leak_rate

    def apply(self, model: Model):

         for row in model.cells:
            for cell in row:
                if cell.type == CellType.OIL_SOURCE:
                    cell.oil_change += self.leak_rate
                    print(cell.oil_level)

            
                        
