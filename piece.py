class Piece:
    def __init__(self, chess_set, color, position):
        self.color = color
        self.chess_set = chess_set
        self.position = position
        self.id = type(self).__name__.lower() + "_" + self.position
        self.chess_set.board.set_figure(position, self)

    def __repr__(self):
        return __class__.__name__

    def move(self, new_position, x1, y1, x2, y2):
        pass

    def remove(self):
        self.position.resident = None


class Pawn(Piece):
    def __init__(self, set, color, position):
        super().__init__(set, color, position)
        self.first_move = True


    def __repr__(self):
        return self.color + " " + __class__.__name__


    # def second_move(self, new_position):
    #     if new_position in self.chess_board.positions:
    #         x1, y1 = self.position
    #         x2, y2 = new_position
    #         if x2 == x1 and y2 == str(int(y1) + 1):
    #             print(self.position, new_position)
    #             self.chess_board.positions[self.position] = None
    #             self.position = new_position
    #         else:
    #             print("Wrong move! Choose the right one.")
    #     self.chess_board.positions[new_position] = self
    #
    #
    # def move(self, new_position):
    #     if new_position in self.chess_board.positions:
    #         x1, y1 = self.position
    #         x2, y2 = new_position
    #         if x2 == x1 and y2 == str(int(y1) + 1) or  x2 == x1 and y2 == str(int(y1) + 2):
    #             print(self.position, new_position)
    #             self.chess_board.positions[self.position] = None
    #             self.position = new_position
    #             print(self.position)
    #         else:
    #             print("Wrong move! Choose the right one.")
    #         self.chess_board.positions[new_position] = self
    #         self.move = self.second_move

    def move(self, new_position, x1, y1, x2, y2):
        if self.chess_set.board.positions[new_position].resident != None:
            if x2 == chr(ord(x1) + 1) and y2 == str(int(y1) + 1) or \
                    x2 == chr(ord(x1) - 1) and y2 == str(int(y1) + 1):
                self.chess_set.board.positions[self.position].clear()
                self.chess_set.board.positions[new_position].clear()
                print("Your " + self.__class__.__name__ + " killed enemy's {0!r}".format(
                    self.chess_set.board.positions[new_position].resident))
                self.position = new_position
                self.chess_set.board.set_figure(new_position, self)

        if self.first_move == True:
            if x2 == x1 and y2 == str(int(y1) + 1) or x2 == x1 and y2 == str(int(y1) + 2):
                self.chess_set.board.positions[self.position].clear()
                self.position = new_position
                self.chess_set.board.set_figure(new_position, self)
                self.first_move = False
            else:
                print("Wrong move! Choose the right one.")


        elif self.first_move == False:
            if x2 == x1 and y2 == str(int(y1) + 1):
                self.chess_set.board.positions[self.position].clear()
                self.position = new_position
                self.chess_set.board.set_figure(new_position, self)
            else:
                print("Wrong move! Choose the right one.")

        self.id = type(self).__name__.lower() + "_" + self.position

        if self.color == "black":
            self.chess_set.board.print_chessboard()
        else:
            self.chess_set.board.print_chessboard_b()


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