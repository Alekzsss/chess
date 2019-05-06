class Piece:
    def __init__(self, chess_set, color, position):
        self.color = color
        self.chess_set = chess_set
        self.position = self.chess_set.board.set_figure(position, self)

    def __repr__(self):
        return __class__.__name__

    def move(self, new_position, x1, y1, x2, y2):
        pass


class Pawn(Piece):
    def __init__(self, set, color, position):
        super().__init__(set, color, position)
        self.first_move = True


    def __repr__(self):
        return self.color + " " + __class__.__name__

    def move(self, new_position, x1, y1, x2, y2):
        def move_figure():
            self.chess_set.board.positions[self.position].clear()
            self.position = new_position
            self.chess_set.board.set_figure(new_position, self)

        def remove_figure():
            for piece in self.chess_set.pieces:
                if piece.position == attacked.position:
                    self.chess_set.pieces.remove(piece)
                    print(f"{len(self.chess_set.pieces)} piece(s) remained")

        def move_method(condition):
            if condition:
                move_figure()
                self.first_move = False
                print("first move = ", self.first_move)
            else:
                print(
                    f"Wrong move! You choose {type(self).__name__.lower()} on position {self.position}")
                return "wrong"

        def attack_method(condition):
            if condition:
                remove_figure()
                move_figure()

                print("Your " + self.__class__.__name__ + " killed enemy's {0!r} at".format(attacked), attacked.position)
            else:
                print("Cannot attack! Make another move")
                return "again"

        def white_attack_condition(x1, y1, x2, y2):
            return x2 == chr(ord(x1) + 1) and y2 == str(int(y1) + 1) or \
                   x2 == chr(ord(x1) - 1) and y2 == str(int(y1) + 1)

        def black_attack_condition(x1, y1, x2, y2):
            return x2 == chr(ord(x1) - 1) and y2 == str(int(y1) - 1) or \
                   x2 == chr(ord(x1) + 1) and y2 == str(int(y1) - 1)

        def white_condition2(x1, y1, x2, y2):
            return x2 == x1 and y2 == str(int(y1) + 1)

        def black_condition2(x1, y1, x2, y2):
            return x2 == x1 and y2 == str(int(y1) - 1)

        def white_condition(x1, y1, x2, y2):
            return x2 == x1 and y2 == str(int(y1) + 1) or x2 == x1 and y2 == str(int(y1) + 2)

        def black_condition(x1, y1, x2, y2):
            return x2 == x1 and y2 == str(int(y1) - 1) or x2 == x1 and y2 == str(int(y1) - 2)

        attacked = self.chess_set.board.positions[new_position].resident

        if attacked != None:
            print("сработал attack")
            if self.color == "white":
                attack_method(white_attack_condition(x1, y1, x2, y2))
            else:
                attack_method(black_attack_condition(x1, y1, x2, y2))

        else:
            if self.first_move == False:
                print("сработал second move")
                if self.color == "white":
                    move_method(white_condition2(x1, y1, x2, y2))
                else:
                    move_method(black_condition2(x1, y1, x2, y2))

            if self.first_move == True:
                print("сработал first move")
                if self.color == "white":
                    move_method(white_condition(x1, y1, x2, y2))
                else:
                    move_method(black_condition(x1, y1, x2, y2))

        if self.color == "black":
            self.chess_set.board.print_chessboard()
        else:
            self.chess_set.board.print_chessboard_b()


    def move_check(self):
        x1, y1 = self.position[0], self.position[1]
        if self.color == "white":
            new_pos = x1 + str(int(y1) + 1)
            if self.chess_set.board.positions[new_pos].resident != None:
                return False
            else:
                return True
        else:
            new_pos = x1 + str(int(y1) - 1)
            if self.chess_set.board.positions[new_pos].resident != None:
                return False
            else:
                return True

    def attack_check(self):
        x1, y1 = self.position[0], self.position[1]
        if self.color == "white":
            supposed_pos = [chr(ord(x1) + 1) + str(int(y1) + 1), chr(ord(x1) - 1) + str(int(y1) + 1)]
            print("supposed_pos =", supposed_pos)
            new_pos = [pos for pos in supposed_pos if pos in self.chess_set.board.positions]
            print("new_pos =", new_pos)
            l = []
            for pos in new_pos:
                l.append([self.chess_set.board.positions[pos].resident == None])
            if all(l):
                return False
            else:
                return True
        else:
            supposed_pos = [chr(ord(x1) - 1) + str(int(y1) - 1), chr(ord(x1) + 1) + str(int(y1) - 1)]
            new_pos = [pos for pos in supposed_pos if pos in self.chess_set.board.positions]
            print("new_pos =", new_pos)
            l = []
            for pos in new_pos:
                l.append(self.chess_set.board.positions[pos].resident == None)
            if all(l):
                return False
            else:
                return True


if __name__ == '__main__':
    pass





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