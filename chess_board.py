from itertools import product
from position import Position
from collections import OrderedDict

class ChessBoard:
    # positions = dict.fromkeys([i[1] + i[0] for i in product("12345678", "abcdefgh")], None)
    _keys = sorted([i + str(j) for i in "abcdefgh" for j in range(1, 9)], key=lambda x: x[1], reverse=True)

    def __init__(self, chess_set):
        self.chess_set = chess_set
        self.positions = OrderedDict(zip(self._keys, [Position(self) for _ in range(len(self._keys))]))
        self.positions_b = dict(reversed(self.positions.items()))


    def set_figure(self, position, figure):
        self.positions[position].populate(figure)

    def print_chessboard(self):
       print ("""
      8   {} | {} | {} | {} | {} | {} | {} | {}
         _____________________________________________________
      7   {} | {} | {} | {} | {} | {} | {} | {}
         _____________________________________________________
      6   {} | {} | {} | {} | {} | {} | {} | {}
         _____________________________________________________
      5   {} | {} | {} | {} | {} | {} | {} | {}
         _____________________________________________________                
      4   {} | {} | {} | {} | {} | {} | {} | {}
         _____________________________________________________
      3   {} | {} | {} | {} | {} | {} | {} | {}
         _____________________________________________________
      2   {} | {} | {} | {} | {} | {} | {} | {}
         _____________________________________________________
      1   {} | {} | {} | {} | {} | {} | {} | {}
            A      B      C      D      E      F      G      H """.format(*self.positions.values()))

    def print_chessboard_b(self):
       print ("""
      1   {} | {} | {} | {} | {} | {} | {} | {}
         _____________________________________________________
      2   {} | {} | {} | {} | {} | {} | {} | {}
         _____________________________________________________
      3   {} | {} | {} | {} | {} | {} | {} | {}
         _____________________________________________________
      4   {} | {} | {} | {} | {} | {} | {} | {}
         _____________________________________________________                
      5   {} | {} | {} | {} | {} | {} | {} | {}
         _____________________________________________________
      6   {} | {} | {} | {} | {} | {} | {} | {}
         _____________________________________________________
      7   {} | {} | {} | {} | {} | {} | {} | {}
         _____________________________________________________
      8   {} | {} | {} | {} | {} | {} | {} | {}
            H      G      F      E      D      C      B      A """.format(*self.positions_b.values()))


if __name__ == '__main__':
    pass




# def columns():
#     for i in range(1, 9):
#         print(i, " | ".join(["{:^14}"]) * 8)
#         print("_" * 100)
#     a = [Position(i + str(j)) for i in "abcdefgh" for j in range(1, 9)]
#     print(a)