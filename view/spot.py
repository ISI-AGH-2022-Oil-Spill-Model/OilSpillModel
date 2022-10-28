import numpy as np
from view.colors import Color
import pygame

class Spot:
    """Representation of the pixel on a grid."""
    
    def __init__(self, row, col, size) -> None:
        self.row = row
        self.col = col
        self.size = size
        self.x = row * size
        self.y = col * size
        self.color = Color.water
    
    def get_pos(self):
        """Returns idx of row and column of the object."""
        return self.row, self.col
    
    def draw(self, window):
        """Draw the square with proper color and standaralized size."""
        pygame.draw.rect(window, self.color, (self.x, self.y, self.size, self.size))
    

