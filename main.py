from applicators.dispersion_applicator import DispersionApplicator
from controller.controller import Controller
from model.change_matrix import ChangeMatrix
from model.model import Model
from data.map_intializer import MapInitializer


# create new applicators here
def get_applicators():
    dispersion = DispersionApplicator(0.2, 0.7)
    return [dispersion]


def main():
    image_name = "gulfOfMexicoMap.png"
    map_init = MapInitializer("\images\\" + image_name)
    model = Model(map_init.get_image_size(), 1)
    model.fill_cells(map_init)
    model.init_surface("ocean")
    iterations = 25
    controller = Controller()
    controller.run_simulation(iterations, model, get_applicators())


if __name__ == '__main__':
    main()
