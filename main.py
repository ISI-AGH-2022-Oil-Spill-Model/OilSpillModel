from applicators.dispersion_applicator import DispersionApplicator
from controller.controller import Controller
from model.change_matrix import ChangeMatrix
from model.model import Model


# create new applicators here
def get_applicators():
    dispersion = DispersionApplicator(0.2, 0.7)
    return [dispersion]


def main():
    shape = (100, 100)
    image_name = "1231" # TODO
    model = Model(shape, 10)
    model.init_surface("ocean")
    iterations = 25
    controller = Controller()
    controller.run_simulation(iterations, model, get_applicators())


if __name__ == '__main__':
    main()
