import pygame

from model.model import Model

from view.colors import Color


class Animator:

    def __init__(self) -> None:
        self.window = None

    def initialize_animation(self, window_size: tuple, model: Model):
        pygame.display.set_caption('Oil Spill Model')
        self.window = pygame.display.set_mode(window_size)
        pygame.display.update()
        
    def update(self, model: Model, fps):
        pygame.event.get()
        self.__draw_active(model)
        pygame.display.update()
        pygame.time.Clock().tick(fps)

    def draw_map(self, model: Model):
        pygame.event.get()
        self.window.fill(Color.water)
        for row in model.cells:
            for cell in row:
                cell.draw(self.window)
        pygame.display.update()
        
    def __draw_active(self, model: Model):
        for row in model.active_cells():
            for cell in row:
                cell.draw(self.window)

    def close_animation(self):
	    pygame.quit()
