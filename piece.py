class Piece:
    def __init__(self, chess_set, color, position):
        self.color = color
        self.chess_set = chess_set
        self.position = self.chess_set.board.set_figure(position, self)

    def __repr__(self):
        return __class__.__name__

    def move(self, new_position, figure):
        pass


class Pawn(Piece):
    def __init__(self, chess_set, color, position):
        super().__init__(chess_set, color, position)
        self.first_move = True

    def __repr__(self):
        return " " + self.color + " " + __class__.__name__ + " "

    def _white_attack_condition(self, x1, y1, x2, y2):
        return x2 == chr(ord(x1) + 1) and y2 == str(int(y1) + 1) or \
               x2 == chr(ord(x1) - 1) and y2 == str(int(y1) + 1)

    def _black_attack_condition(self, x1, y1, x2, y2):
        return x2 == chr(ord(x1) - 1) and y2 == str(int(y1) - 1) or \
               x2 == chr(ord(x1) + 1) and y2 == str(int(y1) - 1)

    def _white_condition(self, x1, y1, x2, y2):
        return x2 == x1 and y2 == str(int(y1) + 1)

    def _black_condition(self, x1, y1, x2, y2):
        return x2 == x1 and y2 == str(int(y1) - 1)

    def _white_first_condition(self, x1, y1, x2, y2):
        return x2 == x1 and y2 == str(int(y1) + 1) or x2 == x1 and y2 == str(int(y1) + 2)

    def _black_first_condition(self, x1, y1, x2, y2):
        return x2 == x1 and y2 == str(int(y1) - 1) or x2 == x1 and y2 == str(int(y1) - 2)

    def _can_move_method(self, condition, value=False):
        all_appr_positions = []
        for pos in self.chess_set.board.positions:
            if condition(self.position[0], self.position[1], pos[0], pos[1]) is True:
                all_appr_positions.append(pos)
        empty_pos = [p for p in all_appr_positions if self.chess_set.board.positions[p].not_empty == value]
        return True if empty_pos else False

    def _can_attack_method(self, condition):
        return self._can_move_method(condition, value=True)

    def _check_attack(self, position):
        all_appr_positions = []
        for pos in self.chess_set.board.positions:
            if self.color == "white":
                condition = self._white_attack_condition
            else:
                condition = self._black_attack_condition
            if condition(self.position[0], self.position[1], pos[0], pos[1]) is True:
                all_appr_positions.append(pos)
        return True if position in all_appr_positions else False

    # def check(self, pos, new_posit):




    def move(self, piece_position, new_position):
        x1, y1 = piece_position
        x2, y2 = new_position

        def _move_method(condition, attack=False):
            if condition:
                if attack:
                    piece = [piece for piece in self.chess_set.pieces if piece.position == new_position][0]
                    self.chess_set.pieces.remove(piece)
                    user = [user for user in self.chess_set.players if user.color == piece.color][0]
                    user.user_pieces.remove(piece)
                    attacked = next_pos.resident

                self.chess_set.board.positions[self.position].clear()
                self.position = new_position
                self.chess_set.board.set_figure(new_position, self)
                self.first_move = False
                if attack:
                    print("Your " + type(self).__name__ + " killed enemy's {0!r} at".format(attacked),
                          new_position)
                    print(f"{len(self.chess_set.pieces)} piece(s) remained")

                if self.color == "white":
                    self.chess_set.board.print_chessboard_b()
                else:
                    self.chess_set.board.print_chessboard()
            else:
                if attack:
                    print("\nThe piece is not in attack range!")
                    advice = input("\n1 - to change position to go\n0 - to choose another piece\n:")
                    while advice not in ("0", "1"):
                        print("You enter wrong number!")
                        advice = input("You must enter the right one: ")
                    if advice == "1":
                        return "wrong"
                    else:
                        return "again"
                else:
                    print(f"Wrong move! You choose {type(self).__name__.lower()} on position {self.position}")
                    return "wrong"

        next_pos = self.chess_set.board.positions[new_position]

        if next_pos.not_empty:

            if self.color == "white":
                return _move_method(self._white_attack_condition(x1, y1, x2, y2), attack=True)
            else:
                return _move_method(self._black_attack_condition(x1, y1, x2, y2), attack=True)
        else:
            if self.first_move:

                # if self.color == "white":
                #     return self.check(pos, new_posit)

                if self.color == "white":
                    return _move_method(self._white_first_condition(x1, y1, x2, y2))
                else:
                    return _move_method(self._black_first_condition(x1, y1, x2, y2))

            else:
                if self.color == "white":
                    return _move_method(self._white_condition(x1, y1, x2, y2))
                else:
                    return _move_method(self._black_condition(x1, y1, x2, y2))

    @property
    def can_move(self) -> bool:
        if self.color == "white":
            return self._can_move_method(self._white_condition)
        else:
            return self._can_move_method(self._black_condition)

    @property
    def can_attack(self) -> bool:
        if self.color == "white":
            return self._can_attack_method(self._white_attack_condition)
        else:
            return self._can_attack_method(self._black_attack_condition)


class Rook(Pawn):
    def __init__(self, chess_set, color, position):
        super().__init__(chess_set, color, position)
        self.first_move = False

    def universal_condition(self, x1, y1, x2, y2):
        return x2 == x1 or y2 == y1

    def _white_condition(self, x1, y1, x2, y2):
        return self.universal_condition(x1, y1, x2, y2)

    def _black_condition(self, x1, y1, x2, y2):
        return self.universal_condition(x1, y1, x2, y2)

    def _white_attack_condition(self, x1, y1, x2, y2):
        return self.universal_condition(x1, y1, x2, y2)

    def _black_attack_condition(self, x1, y1, x2, y2):
        return self.universal_condition(x1, y1, x2, y2)

    @property
    def can_move(self):
        return self._can_move_method(self.universal_condition)\


    def __repr__(self):
        return " " + self.color + " " + __class__.__name__ + " "


class Bishop(Rook):
    def __init__(self, chess_set, color, position):
        super().__init__(chess_set, color, position)
        self.first_move = False

    def universal_condition(self, x1, y1, x2, y2):
        return abs(ord(x1) - ord(x2)) == abs(int(y1) - int(y2))

    def __repr__(self):
        return self.color + " " + __class__.__name__


class Knight(Bishop):
    def __init__(self, chess_set, color, position):
        super().__init__(chess_set, color, position)
        self.first_move = False

    def universal_condition(self, x1, y1, x2, y2):
        return abs(ord(x1) - ord(x2)) * 2 == abs(int(y1) - int(y2)) or \
               abs(ord(x1) - ord(x2)) == abs(int(y1) - int(y2)) * 2

    def __repr__(self):
        return self.color + " " + __class__.__name__


class King(Rook):
    def __init__(self, chess_set, color, position):
        super().__init__(chess_set, color, position)
        self.first_move = False

    def universal_condition(self, x1, y1, x2, y2):
        return abs(ord(x1) - ord(x2)) == 1 or abs(int(y1) - int(y2)) == 1

    def __repr__(self):
        return " " + self.color + " " + __class__.__name__ + " "


class Queen(Bishop):
    def __init__(self, chess_set, color, position):
        super().__init__(chess_set, color, position)
        self.first_move = False

    def universal_condition(self, x1, y1, x2, y2):
        bishop_condition = super().universal_condition(x1, y1, x2, y2)
        return bishop_condition or x1 == x2 or y1 == y2

    def __repr__(self):
        return " " + self.color + " " + __class__.__name__
