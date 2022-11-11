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
    current_vel_dict = {
        Color.v0: 0,
        Color.v35: 9,
        Color.v70: 18,
        Color.v105: 27,
        Color.v140: 45,
        Color.v175: 63,
        Color.v210: 81,
        Color.v245: 100
    }
