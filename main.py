from applicators.dispersion_applicator import DispersionApplicator
from applicators.oil_leak_applicator import OilLeakApplicator
from applicators.water_current_applicator import WaterCurrentApplicator
from applicators.wind_applicator import WindApplicator
from controller.controller import Controller
from model.model import Model
from data.map_intializer import MapInitializer
from data.current_map_initializer import CurrentMapInitializer
from data.wind_map_initializer import WindMapInitializer


# create new applicators here
def get_applicators():
    leaks = OilLeakApplicator(1000, False)
    dispersion = DispersionApplicator(0.2, 0.7)
    water_current = WaterCurrentApplicator(0.4)
    wind = WindApplicator(0.4)
    return [leaks, water_current, wind, dispersion]


def main():

    image_name = "mapbg.png"
    current_direction_image = "images/mapbgcurrentsdirect.png"
    current_speed_image = "images/mapbgcurrentsvelocity.png"
    wind_direction_image = "images/mapwinddirection.png"
    wind_speed_image = "images/mapwindvelocity.png"
    
    map_init = MapInitializer("images/" + image_name)
    model = Model(map_init.get_image_size(), 2)
    model.fill_cells(map_init)
    current_direction, current_speed = CurrentMapInitializer(current_direction_image, current_speed_image).get_cell_arrays()
    wind_direction, wind_speed = WindMapInitializer(wind_direction_image, wind_speed_image, 0, 1).get_cell_arrays()
    
    model.update_current(current_direction, current_speed)
    model.update_wind(wind_direction, wind_speed)
    iterations = 1000
    fps = 1000

    controller = Controller()
    controller.run_simulation(iterations, model, get_applicators(), fps)


if __name__ == '__main__':
    main()
