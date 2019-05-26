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
            message = f"Player {self.number} enter your name: "
            while True:
                try:
                    value = input(message)
                    if " " in value or value in self._names:
                        raise Exception
                except:
                    print("Choose another name)")
                    message = f"Player {self.number} enter right name: "
                else:
                    break
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
                while True:
                    try:
                        color_num = int(input('Choose your color:\n\nwhite - "1"\nblack - "2"\n'))
                        if color_num not in (1, 2):
                            raise Exception
                    except:
                        print("Oops, missprint!")
                    else:
                        break
                value = self._colors.pop(color_num - 1)
                self._color = value

    def __repr__(self):
        return self.name

    def make_move(self):
        print(f"Your turn {self.name}({self.color})")
        self.chess_set.move_piece(self)


if __name__ == '__main__':
    pass
