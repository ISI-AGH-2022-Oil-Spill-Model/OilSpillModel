from applicators.i_applicator import IApplicator
from model.model import Model
from view.animator import Animator
import time



class Controller:
    def __init__(self, animator: Animator = Animator()):
        self.animator = animator

    def run_simulation(self, iterations: int, model: Model, applicators: list[IApplicator], fps):
        window_size = tuple(model.cell_size * x for x in model.shape)
        self.animator.initialize_animation(window_size, fps)

        for i in range(iterations):
            print("Iteration: ", i)
            self.animator.show(model)

            for applicator in applicators:
                applicator.apply(model)

            model.apply_change()

        self.animator.close_animation()
            

