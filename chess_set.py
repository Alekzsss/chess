from chess_board import ChessBoard
from piece import Pawn, Rook, Bishop, Knight, King, Queen


class ChessSet:
    def __init__(self):
        self.board = ChessBoard(self)
        self.pieces = [Pawn(self, "white", item) for item in [i + "2" for i in "abcdefgh"]]
        self.pieces.extend([Pawn(self, "black", item) for item in [i + "7" for i in "abcdefgh"]])
        self.pieces.extend([Rook(self, "white", item) for item in ("a1", "h1")])
        # self.pieces.extend([Rook(self, "black", item) for item in ("a8", "h8")])
        # self.pieces.extend([Bishop(self, "white", item) for item in ("c1", "f1")])
        # self.pieces.extend([Bishop(self, "black", item) for item in ("c8", "f8")])
        # self.pieces.extend([Knight(self, "white", item) for item in ("b1", "g1")])
        # self.pieces.extend([Knight(self, "black", item) for item in ("b8", "g8")])
        # self.pieces.extend([King(self, "white", "e1"), King(self, "black", "e8"), Queen(self, "white", "d1"),
        #                     Queen(self, "black", "d8")])
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
        message = "\nChoose position to go:\n('0' to choose another piece)\n"
        while True:
            position_to_go = input(message)
            try:
                if position_to_go == "0":
                    position_to_go = int(position_to_go)
                    break
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

    def move_piece(self, player):
        piece_position = self._piece_position(player)
        piece = self.board.positions[piece_position].resident
        if piece.can_move:
            pos_to_go = self._pos_to_go(player)
            if pos_to_go:  # checks if there is a position to move the piece     #  marker of the beginning of change
                # if piece.check(piece_position, pos_to_go):
                #     if self.board.positions[pos_to_go].not_empty:
                #         print("\nThe piece is not in attack range!")
                #         advice = input("\n1 - to change position to go\n0 - to choose another piece\n:")
                #         while advice not in ("0", "1"):
                #             print("You enter wrong number!")
                #             advice = input("You must enter the right one: ")
                #
                #         if advice == "1":
                #             posit_to_go = self._pos_to_go(player)
                #             if posit_to_go:
                #                 feedback = piece.move(piece_position, posit_to_go)
                #             else:
                #                 self.move_piece(player)
                #                 return
                #         else:
                #             self.move_piece(player)
                #             return
                #
                #     # feedback = piece.move(piece_position, pos_to_go)
                #     # while feedback in ("again", "wrong"):
                #     #     if feedback == "again":
                #     #         feedback = None
                #     #         self.move_piece(player)
                #     #         continue
                #     #     elif feedback == "wrong":
                #     #         feedback = None
                #     #         posit_to_go = self._pos_to_go(player)
                #     #         if posit_to_go:
                #     #             feedback = piece.move(piece_position, posit_to_go)
                #     #         else:
                #     #             self.move_piece(player)
                #     #             return
                # else:
                #     print(f"Wrong move! You choose {type(piece).__name__.lower()} on position {piece_position}")
                #     posit_to_go = self._pos_to_go(player)
                #     if posit_to_go:
                #         feedback = piece.move(piece_position, posit_to_go)
                #     else:
                #         self.move_piece(player)
                #         return
                feedback = piece.move(piece_position, pos_to_go)
                while True:
                    try:
                        if feedback == "again":
                            raise ValueError
                        elif feedback == "wrong":
                            raise KeyError
                    except ValueError:
                            feedback = None
                            self.move_piece(player)
                            continue
                    except KeyError:
                            feedback = None
                            posit_to_go = self._pos_to_go(player)
                            if posit_to_go:
                                feedback = piece.move(piece_position, posit_to_go)
                            else:
                                self.move_piece(player)
                                return
                    else:
                        break
            else:
                self.move_piece(player)
                return
        else:
            print("You cannot move")
            if piece.can_attack:
                advice = input('"You can attack or choose another figure:"\n\n"1 - to attack"\n"'
                               '0 - to choose another piece"\n')
                if advice == "1":
                    piece.move(piece_position, self._pos_to_go(player))
                else:
                    self.move_piece(player)
            else:
                print("You cannot attack")
                self.move_piece(player)

    def relocate_piece(self, piece, new_position):
        self.board.positions[piece.position].clear()
        piece.position = new_position
        self.board.set_figure(new_position, piece)

    def add_piece(self, old_piece, piece):
        user = [user for user in self.players if user.color == old_piece.color][0]
        new_piece = piece(self, old_piece.color, old_piece.position)
        user.user_pieces.extend([new_piece])

    def delete_piece(self, piece):
        self.pieces.remove(piece)
        user = [user for user in self.players if user.color == piece.color][0]
        user.user_pieces.remove(piece)
