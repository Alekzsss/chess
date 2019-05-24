from chess_board import ChessBoard
from piece import Pawn, Rook


class ChessSet:
    def __init__(self):
        self.board = ChessBoard(self)
        self.pieces = [Pawn(self, "white", item) for item in [i + "2" for i in "abcdefgh"]]
        self.pieces.extend([Pawn(self, "black", item) for item in [i + "7" for i in "abcdefgh"]])
        self.pieces.extend([Rook(self, "white", item) for item in ("a1", "h1")])
        self.pieces.extend([Rook(self, "black", item) for item in ("a8", "h8")])
        self.players = []

    def _piece_position(self, player):
        message = "Enter piece position: "
        while True:
            piece_pos = input(message)
            try:
                if piece_pos not in self.board.positions:
                    raise KeyError
                elif piece_pos not in [piece.position for piece in player.user_pieces]:
                    raise ValueError
            except ValueError:
                print("It's not your piece.")
                message = "Enter position of your piece: "
            except KeyError:
                print("Position doesn't exist.")
                message = "Enter right piece position: "
                continue
            else:
                break
        return piece_pos

    def _pos_to_go(self, player):
        # print('func "_pos_to_go"')
        message = "Choose position to go:"
        while True:
            position_to_go = input(message)
            try:
                if position_to_go not in self.board.positions:
                    raise KeyError
                elif position_to_go in [piece.position for piece in player.user_pieces]:
                    raise ValueError
            except KeyError:
                print("Position out of board!")
                message = "Choose another position: "
            except ValueError:
                print("Oops there is your piece.")
                message = "Choose another position: "
                continue
            else:
                break
        return position_to_go

    def print_board(self, player):
        if player.color == "black":
            self.board.print_chessboard()
        else:
            self.board.print_chessboard_b()

    def move_piece(self, player):
        piece_position = self._piece_position(player)
        piece = [piece for piece in self.pieces if piece.position == piece_position][0]
        position_resident = self.board.positions[piece_position].resident
        if position_resident.can_move:
            pos_to_go = self._pos_to_go(player)
            # print(piece_position)
            # print("3")
            # print("feedback")
            feedback = piece.move(piece_position, pos_to_go)
            # print("feedback = ", feedback)
            while feedback == "again":
                # print(f"{self.name} сработал 'again'")
                self._first_call = False
                if self.move_piece(player):
                    self._first_call = True

            # print("между wrong и False")
            while feedback == "wrong":
                # print("сработал wrong")
                feedback = piece.move(piece_position, pos_to_go)
            self.print_board(player)
        else:
            print("You cannot move")
            # print("check attack = ", position_resident.can_attack)
            if position_resident.can_attack:
                advice = input('"You can attack or choose another figure:"\n\n"1 - to attack"\n"'
                               '2 - to choose another piece"\n')
                if advice == "1":
                    piece.move(piece_position, self._pos_to_go(player)) # must be "pos_to_go" but due to use "else" now unreacheable
                    self.print_board(player)
                else:
                    self.move_piece(player)
            else:
                print("You cannot attack")
                self.move_piece(player)