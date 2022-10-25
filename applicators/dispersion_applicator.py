import numpy as np

from applicators.i_applicator import IApplicator
from model.change_matrix import ChangeMatrix
from model.model import Model


def dispersion(x, y, x2, y2, oil_level, modified, modifier):
    change = oil_level[x2, y2] * modifier

    # condition which prevents from creating negative values in cells in case of
    # too big dispersion constants or oil layer being too thin

    if oil_level[x2, y2] - 4 * change > 0:
        modified[x, y] += change
        modified[x2, y2] -= change
    else:
        modified[x, y] += change / 4
        modified[x2, y2] -= change / 4
    return modified


class DispersionApplicator(IApplicator):

    def __init__(self, diagonal_dispersion_modifier, dispersion_constant):
        self.p = diagonal_dispersion_modifier
        self.D = dispersion_constant

    def apply(self, model: Model, change_matrix: ChangeMatrix) -> ChangeMatrix:
        oil_level = change_matrix.oil_level
        x_max = oil_level.shape[0]
        y_max = oil_level.shape[1]

        modified = oil_level.copy()
        for x in range(x_max):
            for y in range(y_max):

                # in these conditional statements we make sure that we are not at the edge of the map and that
                # the neighbouring cell has less oil than the current one

                # diagonal
                if x > 0 and y > 0 and oil_level[x - 1, y - 1] > oil_level[x, y]:
                    modified = dispersion(x, y, x - 1, y - 1, oil_level, modified, self.p)
                if x > 0 and y < y_max - 1 and oil_level[x - 1, y + 1] > oil_level[x, y]:
                    modified = dispersion(x, y, x - 1, y + 1, oil_level, modified, self.p)
                if x < x_max - 1 and y > 0 and oil_level[x + 1, y - 1] > oil_level[x, y]:
                    modified = dispersion(x, y, x + 1, y - 1, oil_level, modified, self.p)
                if x < x_max - 1 and y < y_max - 1 and oil_level[x + 1, y + 1] > oil_level[x, y]:
                    modified = dispersion(x, y, x + 1, y + 1, oil_level, modified, self.p)
                # neighbouring
                if x > 0 and oil_level[x - 1, y] > oil_level[x, y]:
                    modified = dispersion(x, y, x - 1, y, oil_level, modified, self.D)
                if x < x_max - 1 and oil_level[x + 1, y] > oil_level[x, y]:
                    modified = dispersion(x, y, x + 1, y, oil_level, modified, self.D)
                if y > 0 and oil_level[x, y - 1] > oil_level[x, y]:
                    modified = dispersion(x, y, x, y - 1, oil_level, modified, self.D)
                if y < oil_level.shape[1] - 1 and oil_level[x, y + 1] > oil_level[x, y]:
                    modified = dispersion(x, y, x, y + 1, oil_level, modified, self.D)

        change_matrix.oil_level = modified
        return change_matrix

