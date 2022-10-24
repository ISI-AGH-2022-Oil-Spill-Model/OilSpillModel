from applicators.dispersion_applicator import DispersionApplicator
from model.change_matrix import ChangeMatrix
from model.model import Model


# create new applicators here
def get_applicators():
    dispersion = DispersionApplicator(0.2, 0.7)
    return [dispersion]


def main():
    shape = (100, 100)
    model = Model(shape)
    applicators = get_applicators()
    iterations = 100
    for i in range(iterations):
        change_matrix = ChangeMatrix(shape)
        for applicator in applicators:
            change_matrix = applicator.apply(model, change_matrix)
        model.apply_change(change_matrix)


if __name__ == '__main__':
    main()
