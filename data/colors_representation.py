from view.colors import Color

class ColorsRepresentation:

    direction_dict = {
        Color.N: [1, 0],
        Color.NE: [1, 1],
        Color.E: [0, 1],
        Color.SE: [-1, 1],
        Color.S: [-1, 0],
        Color.SW: [-1, -1],
        Color.W: [0, -1],
        Color.NW: [1, -1]
    }
