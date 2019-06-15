class Piece:
    def __init__(self, chess_set, color, position):
        self.color = color
        self.chess_set = chess_set
        self.position = self.chess_set.board.set_figure(position, self)
        self.move_history = []

    def __repr__(self):
        return __class__.__name__

    def move(self, new_position, figure):
        pass

    @property
    def player(self):
        return [player for player in self.chess_set.players if player.color == self.color][0]

    @property
    def self_army_pos(self):
        return [piece.position for piece in self.player.pl_pieces]

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

    def move(self, piece_position, new_position):

        def figure_exchange():
            if type(self).__name__ == "Pawn":
                if self.color == "white":
                    half_pos = "8"
                else:
                    half_pos = "1"

                if half_pos in self.position:
                    self.chess_set.add_piece(self, Queen)
                    self.chess_set.delete_piece(self)
                    print("Now you're a queen!")

        def check(old_pos):
            enemy_army = set(self.chess_set.pieces) - set(self.player.pl_pieces)  #
            all_enemy_attack_pos = set()
            for piece in enemy_army:
                all_enemy_attack_pos.update(piece.attack_positions())
            king = [piece for piece in self.player.pl_pieces if type(piece).__name__ == "King"][0]
            print("king position = ", king.position)
            if king.position in all_enemy_attack_pos:
                print("At first you must protect the king!!!")
                self.chess_set.relocate_piece(self, old_pos)
                return True
            else:
                return False


        def _attack_method():
            attacked = next_pos.resident
            if attacked.position in self.attack_positions():
                old_position = self.position
                attacked_piece = [piece for piece in self.chess_set.pieces if piece.position == new_position][0]
                self.chess_set.relocate_piece(self, new_position)
                if check(old_position):
                    return "again"
                self.chess_set.delete_piece(attacked_piece)
                self.first_move = False
                print("Your " + type(self).__repr__(self) + " killed enemy's {0!r} at".format(attacked), new_position)
                print(f"{len(self.chess_set.pieces)} piece(s) remained")
                figure_exchange()
                self.player.move_history.append((old_position, new_position))
                print("player.move_history")
                for i in self.player.move_history:
                    print(i[0], "-", i[1])
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

        def _move_method():
            if new_position in self.move_positions():
                old_position = self.position
                self.chess_set.relocate_piece(self, new_position)
                if check(old_position):
                    return "again"
                self.first_move = False
                figure_exchange()
                self.player.move_history.append((old_position, new_position))
                print("player.move_history")
                for i in self.player.move_history:
                    print(i[0], "-", i[1])
                self.chess_set.board.print_chessboard(self)
            else:
                print(f"Wrong move! You choose {type(self).__name__.lower()} on position {self.position}")
                return "wrong"

        next_pos = self.chess_set.board.positions[new_position]
        if next_pos.is_not_empty:
            return _attack_method()
        else:
            return _move_method()

    def move_positions(self, attack=False):
        if self.color == "white":
            if attack:
                condition = self._white_attack_condition
            elif type(self).__name__ == "Pawn" and self.first_move:
                condition = self._white_first_condition
            else:
                condition = self._white_condition
        else:
            if attack:
                condition = self._black_attack_condition
            elif type(self).__name__ == "Pawn" and self.first_move:
                condition = self._black_first_condition
            else:
                condition = self._black_condition
        self_positions = [piece.position for piece in self.chess_set.pieces if piece.color == self.color]
        all_positions = []
        obstacles = []
        enemy_pos = []
        for pos in self.chess_set.board.positions:
            if condition(self.position[0], self.position[1], pos[0], pos[1]) is True:
                all_positions.append(pos)
                if self.chess_set.board.positions[pos].is_not_empty:
                    if pos not in self_positions:
                        if attack:
                            enemy_pos.append(pos)
                        else:
                            obstacles.append(pos)
                    else:
                        obstacles.append(pos)
        # if type(self).__name__ == "Queen" and self.color == "white" and self.position == "a4" and attack==True:
        #     print("all_positions = ", all_positions)
        #     print("obstacles = ", obstacles)
        #     print("cutted_pos = ", cutted_pos)
        #     print("enemy_pos = ", enemy_pos)
        cutted_pos  = []
        for obs_pos in obstacles:
            self_x = ord(self.position[0])
            self_y = int(self.position[1])
            obs_x = ord(obs_pos[0])
            obs_y = int(obs_pos[1])
            if obs_x == self_x:
                if obs_y - self_y > 0:
                    cutted_pos.extend([p for p in all_positions if ord(p[0]) == obs_x and int(p[1]) >= obs_y])
                elif self_y - obs_y > 0:
                    cutted_pos.extend([p for p in all_positions if ord(p[0]) == obs_x and obs_y >= int(p[1])])
            elif obs_y == self_y:
                if obs_x - self_x > 0:
                    cutted_pos.extend([p for p in all_positions if int(p[1]) == obs_y and ord(p[0]) >= obs_x])
                elif self_x - obs_x > 0:
                    cutted_pos.extend([p for p in all_positions if int(p[1]) == obs_y and obs_x >= ord(p[0])])
            elif obs_x - self_x > 0:
                if obs_y - self_y > 0:
                    cutted_pos.extend([p for p in all_positions if ord(p[0]) >= obs_x and int(p[1]) >= obs_y])
                elif self_y - obs_y > 0:
                    cutted_pos.extend([p for p in all_positions if ord(p[0]) >= obs_x and obs_y >= int(p[1])])
            elif self_x - obs_x > 0:
                if obs_y - self_y > 0:
                    cutted_pos.extend([p for p in all_positions if obs_x >= ord(p[0]) and int(p[1]) >= obs_y])
                elif self_y - obs_y > 0:
                    cutted_pos.extend([p for p in all_positions if obs_x >= ord(p[0]) and obs_y >= int(p[1])])
        # if type(self).__name__ == "Queen" and self.color == "white" and self.position == "a4" and attack==True:
        #     print("cutted_pos after work with obstacles = ", cutted_pos)
        ignored_pos = set()
        if attack:
            for pos in enemy_pos:
                self_x = ord(self.position[0])
                self_y = int(self.position[1])
                enemy_x = ord(pos[0])
                enemy_y = int(pos[1])
                if enemy_x == self_x:
                    if enemy_y - self_y > 0:
                        positions = sorted([p for p in enemy_pos if ord(p[0]) == self_x and int(p[1]) > self_y])
                        del positions[0]
                        ignored_pos.update(set(positions))
                    elif self_y - enemy_y > 0:
                        positions = sorted([p for p in enemy_pos if ord(p[0]) == self_x and self_y > int(p[1])],
                                           key=lambda x: x[1], reverse=True)
                        del positions[0]
                        ignored_pos.update(set(positions))
                elif enemy_y == self_y:
                    if enemy_x - self_x > 0:
                        positions = sorted([p for p in enemy_pos if int(p[1]) == self_y and ord(p[0]) > self_x])
                        del positions[0]
                        ignored_pos.update(set(positions))
                    elif self_x - enemy_x > 0:
                        positions = sorted([p for p in enemy_pos if int(p[1]) == self_y and self_x > ord(p[0])], reverse=True)
                        del positions[0]
                        ignored_pos.update(set(positions))
                elif enemy_x - self_x > 0:
                    if enemy_y - self_y > 0:
                        positions = sorted([p for p in enemy_pos if ord(p[0]) > self_x and int(p[1]) > self_y])
                        del positions[0]
                        ignored_pos.update(set(positions))
                    elif self_y - enemy_y > 0:
                        positions = sorted([p for p in enemy_pos if ord(p[0]) > self_x and self_y > int(p[1])])
                        del positions[0]
                        ignored_pos.update(set(positions))
                elif self_x - enemy_x > 0:
                    if enemy_y - self_y > 0:
                        positions = sorted([p for p in enemy_pos if self_x > ord(p[0]) and int(p[1]) > self_y], reverse=True)
                        del positions[0]
                        ignored_pos.update(set(positions))
                    elif self_y - enemy_y > 0:
                        positions = sorted([p for p in enemy_pos if self_x > ord(p[0]) and self_y > int(p[1])], reverse=True)
                        del positions[0]
                        ignored_pos.update(set(positions))
        # if type(self).__name__ == "Queen" and self.color == "white" and self.position == "a4":
        #     print("ignored_pos = ", ignored_pos)
        #     print("all_positions = ", all_positions)
        #     print("cutted_pos = ", cutted_pos)
        #     print("enemy_pos = ", enemy_pos)
        available_pos = set(all_positions) - set(cutted_pos)
        # print("available_pos = ", available_pos)
        if attack:
            available_pos = available_pos - ignored_pos
            # if type(self).__name__ == "Queen" and self.color == "white" and self.position == "a4":
            #     print("if attack available_pos = ", available_pos)
        return set(all_positions) - set(self_positions) if type(self).__name__ == "Knight" else available_pos

    # def axis_finder(self, pos_list, second_list=None):
    #     if not second_list:
    #         second_list = pos_list
    #     added_pos = []
    #     for obs_pos in pos_list:
    #         x = ord(self.position[0])
    #         y = int(self.position[1])
    #         x2 = ord(obs_pos[0])
    #         y2 = int(obs_pos[1])
    #         if x2 - x == 0:
    #             if y2 - y > 0:
    #                 for p in second_list:
    #                     if ord(p[0]) == x2 and int(p[1]) > y2:
    #                         added_pos = p
    #             elif y - y2 > 0:
    #                 added_pos = [p for p in second_list if ord(p[0]) == x2 and y2 > int(p[1])]
    #         elif y2 - y == 0:
    #             if x2 - x > 0:
    #                 added_pos = [p for p in second_list if int(p[1]) == y2 and ord(p[0]) > x2]
    #             elif x - x2 > 0:
    #                 added_pos = [p for p in second_list if int(p[1]) == y2 and x2 > ord(p[0])]
    #         elif x2 - x > 0:
    #             if y2 - y > 0:
    #                 added_pos = [p for p in second_list if ord(p[0]) > x2 and int(p[1]) > y2]
    #             elif y - y2 > 0:
    #                 added_pos = [p for p in second_list if ord(p[0]) > x2 and y2 > int(p[1])]
    #         elif x - x2 > 0:
    #             if y2 - y > 0:
    #                 added_pos = [p for p in second_list if x2 > ord(p[0]) and int(p[1]) > y2]
    #             elif y - y2 > 0:
    #                 added_pos = [p for p in second_list if x2 > ord(p[0]) and y2 > int(p[1])]
    #     return added_pos

    def attack_positions(self):
        return self.move_positions(attack=True)
    # @property
    # def can_move(self) -> bool:
    #     if self.color == "white":
    #         return self._can_move_method(self._white_condition)
    #     else:
    #         return self._can_move_method(self._black_condition)
    #
    # @property
    # def can_attack(self) -> bool:
    #     if self.color == "white":
    #         return self._can_attack_method(self._white_attack_condition)
    #     else:
    #         return self._can_attack_method(self._black_attack_condition)

    def obstacles(self, piece_pos, required_positions):
        x1, y1 = self.position
        x2, y2 = piece_pos
        if self.color == "white":
            condition = self._white_attack_condition
        else:
            condition = self._black_attack_condition
        all_appr_positions = [pos for pos in required_positions if condition(x1, y1, pos[0], pos[1])]
        appr_positions = []
        for pos in all_appr_positions:
            x1_lt_pos0_lt_x2 = ord(x1) < ord(pos[0]) < ord(x2)
            x1_gt_pos0_gt_x2 = ord(x1) > ord(pos[0]) > ord(x2)
            y1_lt_pos1_lt_y2 = int(y1) < int(pos[1]) < int(y2)
            y1_gt_pos1_gt_y2 = int(y1) > int(pos[1]) > int(y2)
            if x2 == x1:
                if int(y2) - int(y1) > 0:
                    if x2 == pos[0] and y1_lt_pos1_lt_y2:
                        appr_positions.append(pos)
                elif int(y1) - int(y2):
                    if x2 == pos[0] and y1_gt_pos1_gt_y2:
                        appr_positions.append(pos)
            elif y2 == y1:
                if ord(x2) - ord(x1) > 0:
                    if y2 == pos[1] and x1_lt_pos0_lt_x2:
                        appr_positions.append(pos)
                elif ord(x1) - ord(x2) > 0:
                    if y2 == pos[1] and x1_gt_pos0_gt_x2:
                        appr_positions.append(pos)
            elif ord(x2) - ord(x1) > 0:
                if int(y2) - int(y1) > 0:
                    if x1_lt_pos0_lt_x2 and y1_lt_pos1_lt_y2:
                        appr_positions.append(pos)
                elif int(y1) - int(y2) > 0:
                    if x1_lt_pos0_lt_x2 and y1_gt_pos1_gt_y2:
                        appr_positions.append(pos)
            elif ord(x1) - ord(x2) > 0:
                if int(y2) - int(y1) > 0:
                    if x1_gt_pos0_gt_x2 and y1_lt_pos1_lt_y2:
                        appr_positions.append(pos)
                elif int(y1) - int(y2) > 0:
                    if x1_gt_pos0_gt_x2 and y1_gt_pos1_gt_y2:
                        appr_positions.append(pos)
        return appr_positions

    def rear_cover(self, self_army):
        unit_attack_positions = []
        pieces_that_cover = []
        for piece in self_army:
            if piece.color == "white":
                condition = self._white_attack_condition
            else:
                condition = self._black_attack_condition
            for pos in self.chess_set.board.positions:
                if condition(piece.position[0], piece.position[1], pos[0], pos[1]):
                    unit_attack_positions.append(pos)
            all_non_empty_pos = [pos for pos in self.chess_set.board.positions if self.chess_set.board.positions[pos].is_not_empty]
            if self.position in unit_attack_positions and not self.obstacles(piece.position, all_non_empty_pos):
                pieces_that_cover.append(piece)
        return pieces_that_cover


class Rook(Pawn):
    def __init__(self, chess_set, color, position):
        super().__init__(chess_set, color, position)

    def universal_condition(self, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            return False
        elif x1 == x2 and y1 != y2 or x1 != x2 and y1 == y2:
            return True

    def _black_first_condition(self, x1, y1, x2, y2):
        return self.universal_condition(x1, y1, x2, y2)

    def _white_first_condition(self, x1, y1, x2, y2):
        return self.universal_condition(x1, y1, x2, y2)

    def _white_condition(self, x1, y1, x2, y2):
        return self.universal_condition(x1, y1, x2, y2)

    def _black_condition(self, x1, y1, x2, y2):
        return self.universal_condition(x1, y1, x2, y2)

    def _white_attack_condition(self, x1, y1, x2, y2):
        return self.universal_condition(x1, y1, x2, y2)

    def _black_attack_condition(self, x1, y1, x2, y2):
        return self.universal_condition(x1, y1, x2, y2)

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


class Knight(Rook):
    def __init__(self, chess_set, color, position):
        super().__init__(chess_set, color, position)

    def universal_condition(self, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            return False
        else:
            return abs(ord(x1) - ord(x2)) == 2 and abs(int(y1) - int(y2)) == 1 or \
               abs(ord(x1) - ord(x2)) == 1 and abs(int(y1) - int(y2)) == 2

    def __repr__(self):
        if self.color == "white":
            return "\u265e"
        else:
            return "\u2658"


class King(Rook):
    def __init__(self, chess_set, color, position):
        super().__init__(chess_set, color, position)

    def universal_condition(self, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            return False
        else:
            return abs(ord(x1) - ord(x2)) <= 1 and abs(int(y1) - int(y2)) <= 1

    def __repr__(self):
        if self.color == "white":
            return "\u265a"
        else:
            return "\u2654"

class Queen(Rook):
    def __init__(self, chess_set, color, position):
        super().__init__(chess_set, color, position)

    def universal_condition(self, x1, y1, x2, y2):
        # bishop_condition = super().universal_condition(x1, y1, x2, y2)
        if x1 == x2 and y1 == y2:
            return False
        elif abs(ord(x1) - ord(x2)) == abs(int(y1) - int(y2)):
            return True
        elif x1 == x2 and y1 != y2 or x1 != x2 and y1 == y2:
            return True

    def __repr__(self):
        if self.color == "white":
            return "\u265b"
        else:
            return "\u2655"
