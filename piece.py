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
        if self.color == "white":
            return "\u265f"
        else:
            return "\u2659"

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
        suitable_pos = [p for p in all_appr_positions if self.chess_set.board.positions[p].is_not_empty == value]
        return True if suitable_pos else False

    def _can_attack_method(self, condition):
        return self._can_move_method(condition, value=True)
################################################################################################
    # def _check_attack(self, position):
    #     all_appr_positions = []
    #     for pos in self.chess_set.board.positions:
    #         if self.color == "white":
    #             condition = self._white_attack_condition
    #         else:
    #             condition = self._black_attack_condition
    #         if condition(self.position[0], self.position[1], pos[0], pos[1]) is True:
    #             all_appr_positions.append(pos)
    #     return True if position in all_appr_positions else False
##############################################################################################
    # def check(self, pos, new_posit):
    #     x1, y1 = pos
    #     x2, y2 = new_posit
    #     if self.chess_set.board.positions[new_posit].is_not_empty:
    #         if self.color == "white":
    #             if self._white_attack_condition(x1, y1, x2, y2):
    #                 return True
    #         else:
    #             if self._black_attack_condition(x1, y1, x2, y2):
    #                 return True
    #     else:
    #         if self.first_move:
    #             if self.color == "white":
    #                 if self._white_first_condition(x1, y1, x2, y2):
    #                     return True
    #             else:
    #                 if self._black_first_condition(x1, y1, x2, y2):
    #                     return True
    #
    #         else:
    #             if self.color == "white":
    #                 if self._white_condition(x1, y1, x2, y2):
    #                     return True
    #             else:
    #                 if self._black_condition(x1, y1, x2, y2):
    #                     return True
##################################################################################################

    def move(self, piece_position, new_position):
        x1, y1 = piece_position
        x2, y2 = new_position

        def obstacles(condition):
            attacked = next_pos.resident
            all_appr_positions = [pos for pos in self.chess_set.board.positions if condition(x1, y1, pos[0], pos[1])]
            print(all_appr_positions) # begin of changes
            appr_positions = []
            for pos in all_appr_positions:
                x1_lt_pos0_lt_x2 = ord(x1) < ord(pos[0]) < ord(x2)
                x1_gt_pos0_gt_x2 = ord(x1) > ord(pos[0]) > ord(x2)
                y1_lt_pos1_lt_y2 = int(y1) < int(pos[1]) < int(y2)
                y1_gt_pos1_gt_y2 = int(y1) > int(pos[1]) > int(y2)
                if ord(x2) - ord(x1) == 0:
                    if int(y2) - int(y1) > 0:
                        if ord(x2) == ord(pos[0]) and y1_lt_pos1_lt_y2:
                            appr_positions.append(pos)
                        # print(appr_positions)
                    elif int(y1) - int(y2):
                        if ord(x2) == ord(pos[0]) and y1_gt_pos1_gt_y2:
                            appr_positions.append(pos)
                        # print(appr_positions)
                elif int(y2) - int(y1) == 0:
                    if ord(x2) - ord(x1) > 0:
                        if int(y2) == int(pos[1]) and x1_lt_pos0_lt_x2:
                            appr_positions.append(pos)
                        # print(appr_positions)
                    elif ord(x1) - ord(x2) > 0:
                        if int(y2) == int(pos[1]) and x1_gt_pos0_gt_x2:
                            appr_positions.append(pos)
                        # print(appr_positions)
                elif ord(x2) - ord(x1) > 0:
                    if int(y2) - int(y1) > 0:
                        if x1_lt_pos0_lt_x2 and y1_lt_pos1_lt_y2:
                            appr_positions.append(pos)
                        # print(appr_positions)
                    elif int(y1) - int(y2) > 0:
                        if x1_lt_pos0_lt_x2 and y1_gt_pos1_gt_y2:
                            appr_positions.append(pos)
                        # print(appr_positions)
                elif ord(x1) - ord(x2) > 0:
                    if int(y2) - int(y1) > 0:
                        if x1_gt_pos0_gt_x2 and y1_lt_pos1_lt_y2:
                            appr_positions.append(pos)
                        # print(appr_positions)
                    elif int(y1) - int(y2) > 0:
                        if x1_gt_pos0_gt_x2 and y1_gt_pos1_gt_y2:
                            appr_positions.append(pos)
                        # print(appr_positions)
            obstacles = [ pos for pos in appr_positions if self.chess_set.board.positions[pos].is_not_empty]
            return obstacles

        def _attack_method(condition):
            attacked = next_pos.resident
            if not obstacles(condition) or type(self).__name__ == "Knight":
                if condition(x1, y1, x2, y2):
                    piece = [piece for piece in self.chess_set.pieces if piece.position == new_position][0]
                    self.chess_set.delete_piece(piece)
                    self.chess_set.relocate_piece(self, new_position)
                    self.first_move = False
                    print("Your " + type(self).__repr__(self) + " killed enemy's {0!r} at".format(attacked), new_position)
                    print(f"{len(self.chess_set.pieces)} piece(s) remained")
                    if type(self).__name__ == "Pawn":
                        if self.color == "white":
                            if "8" in self.position:
                                self.chess_set.add_piece(self, Queen)
                                self.chess_set.delete_piece(self)
                                print("now you're a queen")
                        else:
                            if "1" in self.position:
                                self.chess_set.add_piece(self, Queen)
                                self.chess_set.delete_piece(self)
                                print("now you're a queen")

                    self.chess_set.board.print_chessboard(self)
                else:
                    print("\nThe piece is not in attack range!")
                    message = "\n1 - to change position to go\n0 - to choose another piece\n:"
                    while True:
                        try:
                            advice = input(message)
                            if advice not in ("0", "1"):
                                raise Exception
                        except:
                            print("You enter wrong number!")
                            message = input("You must enter the right one: ")
                        else:
                            break
                    if advice == "1":
                        return "wrong"
                    else:
                        return "again"
            else:
                print("piece is beyond an obstacle...")
                return "wrong"

        def _move_method(condition):
            if not obstacles(condition) or type(self).__name__ == "Knight":
                if condition(x1, y1, x2, y2):
                    self.chess_set.relocate_piece(self, new_position)
                    self.first_move = False
                    if type(self).__name__ == "Pawn":
                        if self.color == "white":
                            if "8" in self.position:
                                self.chess_set.add_piece(self, Queen)
                                self.chess_set.delete_piece(self)
                                print("now you're a queen")
                        else:
                            if "1" in self.position:
                                self.chess_set.add_piece(self, Queen)
                                self.chess_set.delete_piece(self)
                                print("now you're a queen")
                    self.chess_set.board.print_chessboard(self)
                else:
                    print(f"Wrong move! You choose {type(self).__name__.lower()} on position {self.position}")
                    return "wrong"
            else:
                print("This piece can't move across piece")
                return "wrong"

        next_pos = self.chess_set.board.positions[new_position]
        if next_pos.is_not_empty:

            if self.color == "white":
                return _attack_method(self._white_attack_condition)
            else:
                return _attack_method(self._black_attack_condition)
        else:
            if self.first_move:
                if self.color == "white":
                    return _move_method(self._white_first_condition)
                else:
                    return _move_method(self._black_first_condition)

            else:
                if self.color == "white":
                    return _move_method(self._white_condition)
                else:
                    return _move_method(self._black_condition)

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

    def universal_condition(self, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            return False
        elif x2 == x1 or y2 == y1:
            return True

    def _white_condition(self, x1, y1, x2, y2):
        return self.universal_condition(x1, y1, x2, y2)

    def _black_first_condition(self, x1, y1, x2, y2):
        return self.universal_condition(x1, y1, x2, y2)

    def _white_first_condition(self, x1, y1, x2, y2):
        return self.universal_condition(x1, y1, x2, y2)

    def _black_condition(self, x1, y1, x2, y2):
        return self.universal_condition(x1, y1, x2, y2)

    def _white_attack_condition(self, x1, y1, x2, y2):
        return self.universal_condition(x1, y1, x2, y2)

    def _black_attack_condition(self, x1, y1, x2, y2):
        return self.universal_condition(x1, y1, x2, y2)

    @property
    def can_move(self):
        return self._can_move_method(self.universal_condition)

    def __repr__(self):
        if self.color == "white":
            return "\u265c"
        else:
            return "\u2656"


class Bishop(Rook):
    def __init__(self, chess_set, color, position):
        super().__init__(chess_set, color, position)

    def universal_condition(self, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            return False
        elif abs(ord(x1) - ord(x2)) == abs(int(y1) - int(y2)):
            return True

    def __repr__(self):
        if self.color == "white":
            return "\u265d"
        else:
            return "\u2657"


class Knight(Bishop):
    def __init__(self, chess_set, color, position):
        super().__init__(chess_set, color, position)

    def universal_condition(self, x1, y1, x2, y2):
        return abs(ord(x1) - ord(x2)) * 2 == abs(int(y1) - int(y2)) or \
               abs(ord(x1) - ord(x2)) == abs(int(y1) - int(y2)) * 2

    def __repr__(self):
        if self.color == "white":
            return "\u265e"
        else:
            return "\u2658"


class King(Rook):
    def __init__(self, chess_set, color, position):
        super().__init__(chess_set, color, position)

    def universal_condition(self, x1, y1, x2, y2):
        return abs(ord(x1) - ord(x2)) == 1 or abs(int(y1) - int(y2)) == 1

    def __repr__(self):
        if self.color == "white":
            return "\u265a"
        else:
            return "\u2654"

class Queen(Bishop):
    def __init__(self, chess_set, color, position):
        super().__init__(chess_set, color, position)

    def universal_condition(self, x1, y1, x2, y2):
        bishop_condition = super().universal_condition(x1, y1, x2, y2)
        if x1 == y2 and y1 == y2:
            return False
        elif bishop_condition or x1 == x2 or y1 == y2:
            return True

    def __repr__(self):
        if self.color == "white":
            return "\u265b"
        else:
            return "\u2655"
