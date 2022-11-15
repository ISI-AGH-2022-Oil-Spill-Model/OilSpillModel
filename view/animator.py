import pygame

from model.model import Model

from view.colors import Color


class Animator:

    def __init__(self) -> None:
        self.window = None
        self.fps = 1

    def initialize_animation(self, window_size: tuple, fps: int, model: Model):
        pygame.display.set_caption('Oil Spill Model')
        self.window = pygame.display.set_mode(window_size)
        self.fps = fps
        self.__draw(model)
        pygame.display.update()
        pygame.time.Clock().tick(self.fps)
        

    def show(self, model: Model):
        pygame.event.get()
        self.__draw_active(model)
        pygame.display.update()
        pygame.time.Clock().tick(self.fps)


    def __draw(self, model: Model):
        self.window.fill(Color.water)
        for row in model.cells:
            for cell in row:
                cell.draw(self.window)

    def __draw_active(self, model: Model):
        for row in model.active_cells():
            for cell in row:
                cell.draw(self.window)

    def close_animation(self):
	    pygame.quit()
