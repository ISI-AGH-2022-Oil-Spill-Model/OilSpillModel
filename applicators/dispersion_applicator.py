from applicators.i_applicator import IApplicator
from model.change_matrix import ChangeMatrix
from model.model import Model


class DispersionApplicator(IApplicator):

    def __init__(self, diagonal_dispersion_modifier, dispersion_constant):
        self.p = diagonal_dispersion_modifier
        self.D = dispersion_constant

    def apply(self, model: Model, change_matrix: ChangeMatrix) -> ChangeMatrix:
        pass
