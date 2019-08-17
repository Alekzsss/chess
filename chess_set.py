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

    def _piece_position(self, player, piece_pos=None): #
        if piece_pos == None:
            message = "Enter piece position: "
            while True:
                piece_pos = input(message)
                try:
                    if piece_pos not in self.board.positions:
                        raise KeyError
                    elif piece_pos not in player.army_pos:
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
        message = "Choose position to go:\n('0' to choose another piece)\n"
        while True:
            position_to_go = input(message)
            try:
                if position_to_go == "0":
                    position_to_go = int(position_to_go)
                    break
                if position_to_go not in self.board.positions:
                    raise KeyError
                elif position_to_go in player.army_pos:
                    raise ValueError
                elif type(self).__name__ == "King" and position_to_go in player.enemy_attack_pos:
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
        pos_resident = self.board.positions[piece_position].resident

        # auxiliary function that swaps 2 figures and prints board
        def piece_swap(figure, pos1, pos2):
            self.relocate_piece(pos_resident, pos1)
            self.relocate_piece(figure, pos2)
            self.board.print_board_for_castling(pos_resident)

        #checks if you can make castling
        if type(pos_resident).__name__ == "King" and pos_resident.first_move == True:
            rooks = [piece for piece in player.pl_pieces if type(piece).__name__ == "Rook" and piece.first_move and
                     not piece.obstacles(piece_position, player.army_pos) and
                     not piece.obstacles(piece_position, player.enemy_attack_pos)]

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

        # take on a pass
        enemy_player = [pl for pl in self.players if pl.color != pos_resident.color][0]
        if type(pos_resident).__name__ == "Pawn" and enemy_player.move_history:
            enemy_last_move = enemy_player.move_history[-1]
            needed_pos = [pos for pos in self.board.positions if piece_position[1] == pos[1] and
                            abs(ord(piece_position[0]) - ord(pos[0])) == 1 and
                          self.board.positions[pos].is_not_empty and
                          type(self.board.positions[pos].resident).__name__ == "Pawn" and
                          self.board.positions[pos].resident.position not in player.army_pos and
                          self.board.positions[pos].resident.position in enemy_last_move and
                          abs(int(enemy_last_move[0][1]) - int(enemy_last_move[1][1])) == 2]
            if needed_pos:
                attacked_pos = needed_pos[0]
                print(attacked_pos)
                attacked_resident = self.board.positions[attacked_pos].resident
                print("attacked figure = ", self.board.positions[attacked_pos])
                while True:
                    try:
                        query = int(input(f"Do you wanna take on a pass figure on position '{attacked_pos}'\n"
                                          f"1 - take figure\n0 - continue move\n"))
                        if query not in (0, 1):
                            raise ValueError
                        elif query == 1:
                            raise IndexError
                        elif query == 0:
                            raise SyntaxError
                    except ValueError:
                        print("Oops, missprint!")
                    except IndexError:
                        if pos_resident.color == "white":
                            new_pos = attacked_pos[0] + str(int(attacked_pos[1]) + 1)
                        else:
                            new_pos = attacked_pos[0] + str(int(attacked_pos[1]) - 1)
                        self.relocate_piece(pos_resident, new_pos)
                        self.delete_piece(self.board.positions[attacked_pos].resident)
                        print("Your " + type(pos_resident).__repr__(pos_resident) + " take on pass enemy's {0!r} at".format(attacked_resident),
                              attacked_pos)
                        print(f"{len(self.pieces)} piece(s) remained")
                        self.board.print_chessboard(pos_resident)
                        break
                        # return
                    except SyntaxError:
                        break

        # continues main function
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
            pos_with_enemy = player.all_enemy_pos & pos_resident.attack_positions()
            if pos_with_enemy:
                advice = input('"You can attack or choose another figure:"\n\n"1 - to attack"\n"'
                               '0 - to choose another piece"\n')
                if advice == "1":
                    while True:
                        new_position = input("Enter position to attack: ")
                        try:
                            if new_position not in pos_with_enemy:
                                raise ValueError
                            else:
                                raise KeyError
                        except ValueError:
                                print("Wrong position!")
                                continue
                        except KeyError:
                               pos_resident.move(pos_resident.position, new_position)
                               break
                else:
                    self.move_piece(player)
            else:
                self.move_piece(player)

    def relocate_piece(self, piece, new_position):
        self.board.positions[piece.position].clear()
        piece.position = new_position
        self.board.set_figure(new_position, piece)

    def add_piece(self, old_piece, piece, player):
        new_piece = piece(self, old_piece.color, old_piece.position)
        player.pl_pieces.extend([new_piece])
        self.pieces.extend([new_piece])

    def delete_piece(self, piece):
        self.pieces.remove(piece)
        player = [player for player in self.players if player.color == piece.color][0]
        player.pl_pieces.remove(piece)
        self.board.positions[piece.position].clear()
