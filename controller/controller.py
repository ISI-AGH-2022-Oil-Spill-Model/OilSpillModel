import sys

from applicators.i_applicator import IApplicator
from model.change_matrix import ChangeMatrix
from model.model import Model
from view.animator import Animator
import time
from matplotlib import animation, pyplot as plt



class Controller:
    def __init__(self, animator: Animator = Animator()):
        self.animator = animator
        self.interval = 1

    def run_simulation(self, iterations: int, model: Model, applicators: list[IApplicator]):
        window_size = tuple(model.cell_size * x for x in model.shape)
        self.animator.initialize_animation(window_size)
        change_matrix = ChangeMatrix(model.shape)
        s_time = time.time() - self.interval

        for i in range(iterations):
            print(i)
            s_time = self._wait_register_time(s_time)
            self.animator.show(model)

            # for applicator in applicators:
            #     change_matrix = applicator.apply(model, change_matrix)

            # model.apply_change(change_matrix)
            # change_matrix.clear()
        
        self.animator.close_animation()
            


    def _wait_register_time(self, s_time) -> float:
        c_time = time.time()
        if c_time - s_time < self.interval:
            time.sleep(s_time + self.interval - c_time)

        return time.time()

