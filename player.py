from itertools import count
from chess_set import Chess_set


class Player:
    _number = count(1)

    def __init__(self, chess_set):
        self.number = next(self._number)
        self.name = input(f"Player {self.number} enter your name: ").title()
        self.chess_set = chess_set
        self.color = input("Choose your color: ").lower()
        self.user_pieces = [piece for piece in self.chess_set.pieces if self.color == piece.color]
        print(f"'{self.name}' you are playing on {self.color} side.", "\n")

    def __repr__(self):
        return self.name

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