from applicators.dispersion_applicator import DispersionApplicator
from applicators.oil_leak_applicator import OilLeakApplicator
from applicators.vapor_photo_applicator import VaporPhotoApplicator
from applicators.water_current_applicator import WaterCurrentApplicator
from applicators.wind_applicator import WindApplicator
from controller.controller import Controller
import os


# create new applicators here
def get_applicators():
    leaks = OilLeakApplicator(5000, 200)
    dispersion = DispersionApplicator(0.15, 0.7)
    water_current = WaterCurrentApplicator(0.5)
    wind = WindApplicator(0.2)
    vapor_photo = VaporPhotoApplicator(0.001, 0.001)
    return [leaks, water_current, wind, dispersion, vapor_photo]


def main():
    image_dir = "images"

    map_name = os.path.join(image_dir, "mapbg.png")
    current_direction_image = os.path.join(image_dir, "mapbgcurrentsdirect.png")
    current_speed_image = os.path.join(image_dir, "mapbgcurrentsvelocity.png")
    wind_direction_image = os.path.join(image_dir, "mapwinddirection.png")
    wind_speed_image = os.path.join(image_dir, "mapwindvelocity.png")

    iterations = 1000
    fps = 1000
    pixel_size = 2

    controller = Controller()
    controller.setup(get_applicators(), map_name, current_direction_image, 
                     current_speed_image, wind_direction_image, wind_speed_image, pixel_size)
    controller.run_simulation(iterations, fps)


if __name__ == '__main__':
    main()
