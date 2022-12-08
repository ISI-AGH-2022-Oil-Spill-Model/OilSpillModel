from enum import Enum
import numpy as np

from pygame import Surface
from model.model_constants import MIN_OIL_LEVEL
from view.colors import Color

from view.spot import Spot


class CellType(Enum):
    WATER = 0
    EARTH = 1
    OIL_SOURCE = 2

class Cell:
    max_oil_with_color = 2000
    oil_color_map = list((max(0, 20,- int(np.ceil(np.sqrt(oil) * 0.5))), 
                           max(0, 50 - int(np.ceil(np.sqrt(oil) * 2))), 
                           max(0, 190 - int(np.ceil(np.sqrt(oil) * 8)))) for oil in range(0, max_oil_with_color + 1))

    def __init__(self, type: CellType, cell_size: int, row: int, col: int) -> None:
        self.oil_level = 0
        self.oil_change = 0
        self.type = type
        self.row = row
        self.col = col
        self.visual = Spot(col, row, cell_size)
        self.neighbours = np.empty(8, dtype=np.dtype(object)) # NW, N, NE ,E, SE, S ,SW ,W  - can be None
        self.update_color(self._get_color_by_type())
        self.current_directions = []
        self.current_speed = 0
        self.wind_directions = []
        self.wind_speed = 0

    def _get_color_by_type(self) -> Color:
        if self.type == CellType.WATER:
            return Color.water
        if self.type == CellType.EARTH:
            return Color.earth_visual
        if self.type == CellType.OIL_SOURCE:
            return Color.oil
        return Color.red

    def draw(self, window: Surface):
        self.visual.draw(window)

    def merge_change(self):
        self.oil_level += self.oil_change
        self.oil_change = 0

    def update_color_by_oil_level(self):
        if self.type != CellType.WATER:
            return
        if self.visual.color == Cell.oil_color_map[1] and self.oil_level < MIN_OIL_LEVEL:
            self.update_color((25, 55, 195))
        if  self.oil_level < MIN_OIL_LEVEL:
            return
        self.update_color(Cell.oil_color_map[min(Cell.max_oil_with_color, int(np.ceil(self.oil_level)))])
            
    def update_color(self, new_color: Color):
        self.visual.color = new_color 

    def update_current_direction(self, direction):
        self.current_directions = np.array(self._get_affected_neighbours(direction), dtype=np.int16)

    def update_current_speed(self, speed: int):
        self.current_speed = speed
        
    def update_wind_direction(self, direction):
        self.wind_directions = np.array(self._get_affected_neighbours(direction), dtype=np.int16)

    def update_wind_speed(self, speed: int):
        self.wind_speed = speed

    def _get_affected_neighbours(self, direction) -> list[int]:
        direction = list(direction)
        match direction:
            case [1, -1]:
                return [7, 0, 1]
            case [1, 0]:
                return [0, 1, 2]
            case [1, 1]:
                return [1, 2, 3]
            case [0, 1]:
                return [2, 3, 4]
            case [-1, 1]:
                return [3, 4, 5]
            case [-1, 0]:
                return [4, 5, 6]
            case [-1, -1]:
                return [5, 6, 7]
            case [0, -1]:
                return [6, 7, 0]
            case _:
                return []

    def update_neighbours(self, grid: np.ndarray):
        """Updates neighbours list with all spot's neighbours."""
        height, width = grid.shape

        bot_border = self.row == height - 1
        top_border = self.row == 0
        right_border = self.col == width - 1
        left_border = self.col == 0

        self.neighbours.fill(None)
        if not (top_border or left_border):  # NW
            self.neighbours[0] = grid[self.row - 1, self.col - 1]
        if not (top_border):                 # N
            self.neighbours[1] = grid[self.row - 1, self.col]
        if not (top_border or right_border): # NE
            self.neighbours[2] = grid[self.row - 1, self.col + 1]
        if not (right_border):               # E
            self.neighbours[3] = grid[self.row, self.col + 1]
        if not (bot_border or right_border): # SE
            self.neighbours[4] = grid[self.row + 1, self.col + 1]
        if not (bot_border):                 # S
            self.neighbours[5] = grid[self.row + 1, self.col]
        if not (bot_border or left_border):  # SW
            self.neighbours[6] = grid[self.row + 1, self.col - 1]
        if not (left_border):                # W
            self.neighbours[7] = grid[self.row, self.col - 1]

