import pygame

from model.model import Model

from view.colors import Color


class Animator:

    def __init__(self) -> None:
        self.window = None

    def initialize_animation(self, window_size):
        pygame.display.set_caption('Oil Spill Model')
        self.window = pygame.display.set_mode(window_size)

    def show(self, model: Model):
        self.draw(model)
        pygame.display.update()

    def draw(self, model: Model):
        self.window.fill(Color.tea_green)
        for row in model.cells:
            for cell in row:
                cell.draw(self.window)

    def close_animation(self):
	    pygame.quit()
