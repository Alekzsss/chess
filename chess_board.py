from itertools import product

class ChessBoard:
    # positions = dict.fromkeys([i[1] + i[0] for i in product("12345678", "abcdefgh")], None)
    raw_grid = sorted([i + str(j) for i in "abcdefgh" for j in range(1, 9)], key=lambda x: x[1], reverse=True)
    print(raw_grid)
    positions = dict.fromkeys(raw_grid, None)

    print([i + str(j) for i in "abcdefgh" for j in range(1, 9)])

    def __init__(self, chess_set):
        self.chess_set = chess_set

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

class User:
    pass

if __name__ == '__main__':

    c = ChessBoard("set1")
    print(c.chess_set)
    # print(c.positions)
    c.print_chessboard()


# def columns():
#     for i in range(1, 9):
#         print(i, " | ".join(["{:^14}"]) * 8)
#         print("_" * 100)

