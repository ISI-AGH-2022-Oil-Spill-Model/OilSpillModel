from model.change_matrix import ChangeMatrix
from model.model import Model


class IApplicator:

    def apply(self, model: Model, change_matrix: ChangeMatrix) -> ChangeMatrix:
        raise NotImplementedError
