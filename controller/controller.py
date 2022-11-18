from applicators.bulk_applicator import BulkApplicator
from applicators.i_applicator import IApplicator
from model.model import Model
from view.animator import Animator
from model.model import Model
from data.map_intializer import MapInitializer
from data.current_map_initializer import CurrentMapInitializer
from data.wind_map_initializer import WindMapInitializer



class Controller:
    def __init__(self, animator: Animator = Animator(), model: Model = None):
        self.animator = animator
        self.model = model
        self.bulk_applicator = None

    def setup(self, applicators: list[IApplicator], map_name, current_direction_image, current_speed_image, wind_direction_image, wind_speed_image, pixel_size):
        self.bulk_applicator = BulkApplicator(applicators)
        map_init = MapInitializer(map_name)
        self.model = Model(map_init.get_image_size(), pixel_size)
        window_size = tuple(self.model.cell_size * x for x in reversed(self.model.shape))
        self.animator.initialize_animation(window_size, self.model)

        self.model.fill_cells(map_init)
        self.animator.draw_map(self.model)

        current_direction, current_speed = CurrentMapInitializer(current_direction_image, current_speed_image).get_cell_arrays()
        wind_direction, wind_speed = WindMapInitializer(wind_direction_image, wind_speed_image, 0, 1).get_cell_arrays()
        
        self.model.update_current(current_direction, current_speed)
        self.model.update_wind(wind_direction, wind_speed)

    def run_simulation(self, iterations: int, fps: int):
        for i in range(iterations):
            print("Iteration: ", i)

            self.bulk_applicator.bulk_apply(self.model)
            self.model.apply_change()
            self.animator.update(self.model, fps)

        self.animator.close_animation()
            

