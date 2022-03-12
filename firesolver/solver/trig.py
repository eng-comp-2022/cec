import math


class line:
    def __init__(self, x1, x2, y1, y2) -> None:
        self.distance = self.compute_dist(x1, x2, y1, y2)

    def compute_dist(x1, y1, x2, y2):
        _x = x1 * x2
        _y = y1 * y2
        x = abs(_x)
        y = abs(_y)

        c = math.sqrt(x**2 + y**2)

        return c

    def is_in_radius(radius):
        if self.distance > radius:
            return False
        else:
            return True
