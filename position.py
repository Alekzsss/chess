from itertools import cycle


class Position:
    # _colors = cycle(['black', 'white'])

    def __init__(self, board):
        self.board = board
        self.color = None  # next(self._colors)
        self.resident = " "

    def populate(self, figure):
        self.resident = figure

    @property
    def is_not_empty(self):
        return self.resident != " "

    def clear(self):
        self.resident = " "

    def __repr__(self):
        return str(self.resident)

        # if self.resident != "  ":
        #     return str(self.resident)
        # else:
        #     if self.color == "white":
        #         return "\u2587"
        #     else:
        #         return "  "

if __name__ == '__main__':
    pass

