from matplotlib.backend_bases import MouseEvent
from applicators.dispersion_applicator import DispersionApplicator
from applicators.oil_leak_applicator import OilLeakApplicator
from controller.controller import Controller
from model.model import Model
from data.map_intializer import MapInitializer


# create new applicators here
def get_applicators():
    leaks = OilLeakApplicator(200)
    dispersion = DispersionApplicator(0.1, 0.7)
    return [leaks, dispersion]


def main():
    image_name = "gulfOfMexicoMap.png"
    # map_init = MapInitializer("\images\\" + image_name)
    # model = Model(map_init.get_image_size(), 1)
    # model.fill_cells(map_init)
    model = Model((100,100), 10)
    model.init_surface("ocean")
    iterations = 500
    controller = Controller()
    controller.run_simulation(iterations, model, get_applicators())


if __name__ == '__main__':
    main()
