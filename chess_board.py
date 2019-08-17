from position import Position
from collections import OrderedDict
from itertools import cycle



class ChessBoard:
    _keys = sorted([i + str(j) for i in "abcdefgh" for j in range(1, 9)], key=lambda x: x[1], reverse=True)


    def __init__(self, chess_set):
        self.chess_set = chess_set
        self.positions = OrderedDict(zip(self._keys, [Position(self) for _ in range(len(self._keys))]))
        self.positions_b = dict(reversed(self.positions.items()))

        colors_list = ['black', 'white']
        _colors = cycle(colors_list)
        field_num = "8"
        for pos in self.positions:
            if field_num in pos:
                self.positions[pos].color = next(_colors)
            else:
                field_num = pos[1]
                colors_list = colors_list[::-1]
                self.positions[pos].color = colors_list[0]





    def set_figure(self, position, figure):
        self.positions[position].populate(figure)
        return position

    def print_board(self):
        print("""
      8   {} | {} | {} | {} | {} | {} | {} | {}
         _______________________________
      7   {} | {} | {} | {} | {} | {} | {} | {}
         _______________________________
      6   {} | {} | {} | {} | {} | {} | {} | {}
         _______________________________
      5   {} | {} | {} | {} | {} | {} | {} | {}
         _______________________________      
      4   {} | {} | {} | {} | {} | {} | {} | {}
         _______________________________
      3   {} | {} | {} | {} | {} | {} | {} | {}
         _______________________________
      2   {} | {} | {} | {} | {} | {} | {} | {}
         _______________________________
      1   {} | {} | {} | {} | {} | {} | {} | {}
          A   B   C   D   E   F   G   H
               """.format(*self.positions.values()))

    def print_board_black(self):
        print("""
      1   {} | {} | {} | {} | {} | {} | {} | {}
         _______________________________
      2   {} | {} | {} | {} | {} | {} | {} | {}
         _______________________________
      3   {} | {} | {} | {} | {} | {} | {} | {}
         _______________________________
      4   {} | {} | {} | {} | {} | {} | {} | {}
         _______________________________     
      5   {} | {} | {} | {} | {} | {} | {} | {}
         _______________________________
      6   {} | {} | {} | {} | {} | {} | {} | {}
         _______________________________
      7   {} | {} | {} | {} | {} | {} | {} | {}
         _______________________________
      8   {} | {} | {} | {} | {} | {} | {} | {}
          H   G   F   E   D   C   B   A
            """.format(*self.positions_b.values()))

    def print_chessboard(self, piece):
        if piece.color == "white":
            self.chess_set.board.print_board_black()
        else:
            self.chess_set.board.print_board()

    def print_board_for_castling(self, piece):
        if piece.color == "white":
            self.chess_set.board.print_board()
        else:
            self.chess_set.board.print_board_black()



if __name__ == '__main__':
    c = ChessBoard("?")
    for pos in c.positions:
        print(pos, c.positions[pos].color)
    pass


# def columns():
#     for i in range(1, 9):
#         print(i, " | ".join(["{:^14}"]) * 8)
#         print("_" * 100)
#     a = [Position(i + str(j)) for i in "abcdefgh" for j in range(1, 9)]
#     print(a)

    # lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    #        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    #
    # by_num = 4
    #
    # for x in range(0, len(lst), by_num):
    #     if x + by_num > len(lst):
    #         by_num = len(lst) - x
    #
    #     template = ' | '.join(['{:>2} - {}'] * by_num)
    #     print(template.format(*[j for i in zip(range(x, x + by_num), lst[x:x + by_num]) for j in i]))

#
# word = "abc"
# print(word.center(100, "*"))
# print(word[::-1])
