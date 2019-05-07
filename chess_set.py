from chess_board import ChessBoard
from piece import Pawn, Rook


class Chess_set:
    def __init__(self):
        self.board = ChessBoard(self)
        self.pieces = [Pawn(self, "white", item) for item in [i + "2" for i in "abcdefgh"]]
        self.pieces.extend([Pawn(self, "black", item) for item in [i + "7" for i in "abcdefgh"]])
        self.pieces.extend([Rook(self, "white", item) for item in ("a1", "h1")])
        self.pieces.extend([Rook(self, "black", item) for item in ("a8", "h8")])


    def move(self, piece_pos, new_position):
        # print([piece.position for piece in self.pieces])
        # piece = [piece.position for piece in self.pieces if piece.position == piece_pos][0]
        for piece in self.pieces:
            if piece.position == piece_pos:
                x1, y1 = piece.position
                x2, y2 = new_position
                # print(x1, y1, x2, y2, new_position)
                # print("result of piece.move =", piece.move(new_position, x1, y1, x2, y2))
                return piece.move(new_position, x1, y1, x2, y2)

