class Piece:
    def __init__(self, chess_set, color, position):
        self.color = color
        self.chess_set = chess_set
        self.position = self.chess_set.board.set_figure(position, self)
        # self.id = type(self).__name__.lower() + "_" + self.position

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
            print(self.position)
            self.chess_set.board.set_figure(new_position, self)

        attacked = self.chess_set.board.positions[new_position].resident

        if attacked != None:
            print("attack")
            if self.color == "white":
                if x2 == chr(ord(x1) + 1) and y2 == str(int(y1) + 1) or \
                        x2 == chr(ord(x1) - 1) and y2 == str(int(y1) + 1):
                    # self.chess_set.pieces.remove(piece) for piece in self.chess_set.pieces if piece.position == attacked.position
                    for piece in self.chess_set.pieces:
                        if piece.position == attacked.position:
                            self.chess_set.pieces.remove(piece)
                            print(f"{len(self.chess_set.pieces)} piece(s) remained")
                    move_figure()

                    print("Your " + self.__class__.__name__ + " killed enemy's {0!r}".format(attacked))
                else:
                    print("Cannot attack! Make another move")
                    return "again"
            else:
                if x2 == chr(ord(x1) - 1) and y2 == str(int(y1) - 1) or \
                        x2 == chr(ord(x1) + 1) and y2 == str(int(y1) - 1):
                    # self.chess_set.pieces.remove(piece) for piece in self.chess_set.pieces if piece.position == attacked.position
                    for piece in self.chess_set.pieces:
                        if piece.position == attacked.position:
                            self.chess_set.pieces.remove(piece)
                            print(len(self.chess_set.pieces))
                    move_figure()

                    print("Your " + self.__class__.__name__ + " killed enemy's {0!r}".format(attacked))
                else:
                    print("Cannot attack! Make another move")
                    return "again"

        else:
            print("first move")

            if self.first_move == True:
                if self.color == "white":
                    if x2 == x1 and y2 == str(int(y1) + 1) or x2 == x1 and y2 == str(int(y1) + 2):
                        move_figure()
                        self.first_move = False
                    else:
                        print(f"Wrong move! You choose {type(self).__name__.lower()} on position {self.position}")
                        return "wrong"
                else:
                    if x2 == x1 and y2 == str(int(y1) - 1) or x2 == x1 and y2 == str(int(y1) - 2):
                        move_figure()
                        self.first_move = False
                    else:
                        print(f"Wrong move! You choose {type(self).__name__.lower()} on position {self.position}")
                        return "wrong"



            elif self.first_move == False:
                print("second move")



                if self.color == "white":
                    if x2 == x1 and y2 == str(int(y1) + 1):
                        move_figure()
                    else:
                        print(f"Wrong move! You choose {type(self).__name__.lower()} on position {self.position}")
                        return "wrong"
                else:
                    if x2 == x1 and y2 == str(int(y1) - 1):
                        move_figure()
                    else:
                        print(f"Wrong move! You choose {type(self).__name__.lower()} on position {self.position}")
                        return "wrong"


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