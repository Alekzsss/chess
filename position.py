from itertools import cycle


class Position:
    _colors = cycle(['black', 'white'])

    def __init__(self, board):
        self.board = board
        self.color = next(self._colors)
        self.resident = "   empty    "

    def populate(self, figure):
        self.resident = figure


    def clear(self):
        self.resident = "   empty    "

    # def __call__(self, *ags, **kwargs):
    #     return self.resident

    def __repr__(self):
        return str(self.resident)


if __name__ == '__main__':
    pass

