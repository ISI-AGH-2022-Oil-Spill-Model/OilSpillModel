import pygame

from model.model import Model
from matplotlib import pyplot as plt
import numpy as np


class Animator:

    def __init__(self) -> None:
        self.window = None

    def initialize_animation(self, window_size):
        pygame.display.set_caption('Oil Spill Model')
        # self.window = pygame.display.set_mode(tuple(cell_size * x for x in shape))
        self.window = pygame.display.set_mode(window_size)

    # def __init__(self):
    #     self.fig, self.ax = plt.subplots()

    #     self.x = np.zeros(100)
    #     self.y = np.zeros(100)
    #     self.ax.set_xlabel("X-axis")
    #     self.ax.set_ylabel("Y-plot")
    #     self.ax.set_title("Simple x-y plot")
    #     self.ax.set_ylim(100)
    #     self.ax.set_xlim(100)


    def show(self, model: Model):
        model.draw(self.window)
        pygame.display.update()

        # self.x.append(random.randint(0, 100))
        # self.y.append(random.randint(0, 100))
        # self.ax.scatter(self.x, self.y, color="green")
        # plt.pause(0.01)

    def close_animation(self):
	    pygame.quit()
