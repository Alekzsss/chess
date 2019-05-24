from itertools import count


class Player:
    _number = count(1)
    _colors = ["white", "black"]
    _names = []

    def __init__(self, chess_set):
        self.number = next(self._number)
        self.name = None
        self.color = None
        self.chess_set = chess_set
        self.user_pieces = [piece for piece in self.chess_set.pieces if self.color == piece.color]

        self.chess_set.players.append(self)
        print(f"'{self.name}' you are playing on {self.color} side.", "\n") if self.number == 1 \
            else print(f"'So you {self.name}' playing on {self.color} side.", "\n")  # print notification message to
        # players

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        while not value:
            value = input(f"Player {self.number} enter your name: ")
        while len(value) < 1 or " " in value or value in self._names:
            value = input(f"Player {self.number} enter right name: ")
        self._name = value
        self._names.append(self._name)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        while not value:
            if len(self._colors) == 1:
                value = self._colors[0]
                self._color = value
            else:
                color_num = int(input('Choose your color:\n\nwhite - "1"\nblack - "2"\n'))
                while color_num not in (1, 2):
                    print("Oops, missprint!")
                    color_num = int(input("Choose another color"))
                else:
                    value = self._colors.pop(color_num - 1)
                    self._color = value

    def __repr__(self):
        return self.name

    _first_call = True

    def make_move(self):
        if self._first_call == True:
            print(f"Your turn {self.name}({self.color})")
        else:
            print("Try another one")

        self.chess_set.move_piece(self)


if __name__ == '__main__':
    pass
