from chess_board import ChessBoard
from piece import Pawn, Rook, Bishop, Knight, King, Queen


class ChessSet:
    def __init__(self):
        self.board = ChessBoard(self)
        self.pieces = [Pawn(self, "white", item) for item in [i + "2" for i in "abcdefgh"]]
        self.pieces.extend([Pawn(self, "black", item) for item in [i + "7" for i in "abcdefgh"]])
        self.pieces.extend([Rook(self, "white", item) for item in ("a1", "h1")])
        self.pieces.extend([Rook(self, "black", item) for item in ("a8", "h8")])
        self.pieces.extend([Bishop(self, "white", item) for item in ("c1", "f1")])
        self.pieces.extend([Bishop(self, "black", item) for item in ("c8", "f8")])
        self.pieces.extend([Knight(self, "white", item) for item in ("b1", "g1")])
        self.pieces.extend([Knight(self, "black", item) for item in ("b8", "g8")])
        self.pieces.extend([King(self, "white", "e1"), King(self, "black", "e8"), Queen(self, "white", "d1"), Queen(self, "black", "d8")])
        self.players = []

    def _piece_position(self, player, piece_pos=None):
        if piece_pos == None:
            message = "Enter piece position: "
            while True:
                piece_pos = input(message)
                try:
                    if piece_pos not in self.board.positions:
                        raise KeyError
                    elif piece_pos not in [piece.position for piece in player.pl_pieces]:
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
        else:
            return piece_pos

    def _pos_to_go(self, player):
        enemy_army = set(self.pieces) - set(player.pl_pieces)
        all_enemy_attack_pos = set()
        for piece in enemy_army:
            all_enemy_attack_pos.update(piece.attack_positions())


        message = "Choose position to go:\n('0' to choose another piece)\n"
        while True:
            position_to_go = input(message)
            try:
                if position_to_go == "0":
                    position_to_go = int(position_to_go)
                    break
                if position_to_go not in self.board.positions:
                    raise KeyError
                elif position_to_go in [piece.position for piece in player.pl_pieces]:
                    raise ValueError
                elif type(self).__name__ == "King" and position_to_go in all_enemy_attack_pos:
                    raise IndexError
            except KeyError:
                print("Position out of board!")
                message = "Choose another position: "
            except ValueError:
                print("Oops there is your piece.")
                message = "Choose another position: "
            except IndexError:
                print("This position under enemy's attack!")
                message = "Choose safe position: "
                continue
            else:
                break
        return position_to_go

    def move_piece(self, player):
        piece_position = self._piece_position(player)
        enemy_army = set(self.pieces) - set(player.pl_pieces)
        all_enemy_attack_pos = set()
        for piece in enemy_army:
            all_enemy_attack_pos.update(piece.attack_positions())
        pos_resident = self.board.positions[piece_position].resident
        self_positions = [piece.position for piece in player.pl_pieces]
        if type(pos_resident).__name__ == "King" and pos_resident.first_move == True:
            rooks = [piece for piece in player.pl_pieces if type(piece).__name__ == "Rook" and piece.first_move and
                     not piece.obstacles(piece_position, self_positions) and
                     not piece.obstacles(piece_position, all_enemy_attack_pos)]
            def piece_swap(figure, pos1, pos2):
                self.relocate_piece(pos_resident, pos1)
                self.relocate_piece(figure, pos2)
                self.board.print_board_for_castling(pos_resident)
            if len(rooks) == 1:
                rook = rooks[0]
                print(rooks)
                while True:
                    try:
                        castl_query = int(input(f"Do you want to do castling with rook on '{rook.position}'?\n"
                                                f"1 - to do castling\n0 - no\n"))
                        if castl_query not in (0, 1):
                            raise ValueError
                        elif castl_query == 1:
                            raise IndexError
                        elif castl_query == 0:
                            raise SyntaxError
                    except ValueError:
                        print("Oops, missprint!")
                    except IndexError:
                        if rook.color == "white":
                            if "h" in rook.position:
                                piece_swap(rook, "g1", "f1")
                                break
                            else:
                                piece_swap(rook, "c1", "d1")
                                break
                        else:
                            if "h" in rook.position:
                                piece_swap(rook, "g8", "f8")
                                break
                            else:
                                piece_swap(rook, "c8", "d8")
                                break
                    except SyntaxError:
                        break
            elif len(rooks) == 2:
                rook1, rook2 = rooks
                print("rook1.position = ", rook1.position,"rook2.position = ", rook2.position)
                while True:
                    try:
                        castl_query = int(input(f"Do you want to do castling with rook on '{rook1.position}' or "
                                                f"rook on '{rook2.position}'?\n"
                                                f"1 - to do castling with rook on '{rook1.position}'\n"
                                                f"2 - to do castling with rook on '{rook2.position}'\n"
                                                f"0 - continue move\n"))
                        if castl_query not in (0, 1, 2):
                            raise ValueError
                        elif castl_query == 1:
                            raise IndexError
                        elif castl_query == 2:
                            raise NameError
                        elif castl_query == 0:
                            raise SyntaxError
                    except ValueError:
                        print("Oops, missprint!")
                    except IndexError:
                        if rook1.color == "white":
                            if "h" in rook1.position:
                                piece_swap(rook1, "g1", "f1")
                                break
                            else:
                                piece_swap(rook1, "c1", "d1")
                                break
                        else:
                            if "h" in rook1.position:
                                piece_swap(rook1, "g8", "f8")
                                break
                            else:
                                piece_swap(rook1, "c8", "d8")
                                break
                    except NameError:
                        if rook2.color == "white":
                            if "h" in rook2.position:
                                piece_swap(rook2, "g1", "f1")
                                break
                            else:
                                piece_swap(rook2, "c1", "d1")
                                break
                        else:
                            if "h" in rook2.position:
                                piece_swap(rook2, "g8", "f8")
                                break
                            else:
                                piece_swap(rook2, "c8", "d8")
                                break
                    except SyntaxError:
                        break

        if pos_resident.move_positions():
            pos_to_go = self._pos_to_go(player)
            if pos_to_go:  # checks if there is a position to move the piece
                feedback = pos_resident.move(piece_position, pos_to_go)
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
                                feedback = pos_resident.move(piece_position, posit_to_go)
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
            if pos_resident.attack_positions():
                advice = input('"You can attack or choose another figure:"\n\n"1 - to attack"\n"'
                               '0 - to choose another piece"\n')
                if advice == "1":
                    pos_resident.move(piece_position, self._pos_to_go(player))
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
        user.pl_pieces.extend([new_piece])
        self.pieces.extend([new_piece])

    def delete_piece(self, piece):
        self.pieces.remove(piece)
        user = [user for user in self.players if user.color == piece.color][0]
        user.pl_pieces.remove(piece)
