from itertools import count
from collections import OrderedDict
from chess_set import Chess_set


class Player:
    _number = count(1)
    _colors = {"1": "white", "2": "black"}
    _num_colors = (1, 2)

    def __init__(self, chess_set):
        self.number = next(self._number)
        self.name = input(f"Player {self.number} enter your name: ").title()
        self.chess_set = chess_set
        self.color = None

        if len(self._colors) == 1:
            for i in self._colors:
                self.color = self._colors[i]
        else:
            color_num = input("""
Choose your color: 
                
white - "1"
black - "2"
""")
            if color_num in self._colors:
                self.color = self._colors.pop(color_num)
            else:
                print("Oops, missprint!")
                self.color = input("Choose another color) ").lower()

        self.user_pieces = [piece for piece in self.chess_set.pieces if self.color == piece.color]
        if self.number == 1:
            print(f"'{self.name}' you are playing on {self.color} side.", "\n")
        else:
            print(f"'So you {self.name}' playing on {self.color} side.", "\n")


    def __repr__(self):
        return self.name

    # @property
    # def _color(self):
    #     return self.color
    #
    # @_color.setter
    # def _color(self, value):
    #     if value in ["white", "black"]:
    #         self.color = value
    #     else:
    #         print("error")

    def make_move(self):
        print(f"Your turn {self.name}")
        self.piece_id = input("Enter piece ID :")
        self.position = input("Choose position you wanna go to:")
        if self.piece_id in [piece.id for piece in self.user_pieces]:
            return self.chess_set.move(self.piece_id, self.position)
        else:
            print("It's not your piece")

if __name__ == '__main__':
    pass