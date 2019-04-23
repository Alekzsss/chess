from itertools import cycle


class Position:

    _colors = cycle(['black', 'white'])

    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]
        self.color = next(self._colors)
        self.resident = None

if __name__ == '__main__':
    p = Position("d1")
    print("\n".join([p.x, p.y, str(p.color), str(p.resident)]))
    p2 = Position("d2")
    print("\n".join([p2.x, p2.y, str(p2.color), str(p2.resident)]))
    p3 = Position("d3")
    print("\n".join([p3.x, p3.y, str(p3.color), str(p3.resident)]))