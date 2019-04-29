from chess_board import ChessBoard
from piece import Pawn


class Chess_set:
    def __init__(self):
        self.board = ChessBoard(self)
        self.pieces = [Pawn(self, "white", item) for item in [i + "2" for i in "abcdefgh"]]
        self.pieces.extend([Pawn(self, "black", item) for item in [i + "7" for i in "abcdefgh"]])

    def move(self, piece_id, new_position):
        for piece in self.pieces:
            if piece.id == piece_id:
                if new_position in self.board.positions:
                    x1, y1 = piece.position
                    x2, y2 = new_position
                    return piece.move(new_position, x1, y1, x2, y2)




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



# outer = [[1,2,3], [4,5,6], [7,8,9]]
# new_list = [item for sublist in outer for item in sublist]
# print(new_list)
#
# word = "abc"
# print(word.center(100, "*"))
# print(word[::-1])
