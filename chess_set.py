from chess_board import ChessBoard
from abc import ABC, abstractmethod


class Piece_set:
    def __init__(self, board, pieces: list):
        self.board = board
        self.pieces = pieces


class Piece(ABC):
    def __init__(self, board, color, position):
        self.color = color
        self.chess_board = board
        self.position = position
        self.chess_board.positions[position] = self

    def __repr__(self):
        return __class__.__name__

    @abstractmethod
    def move(self, new_position):
        pass

    @abstractmethod
    def attack(self, figure):
        pass

    def remove(self):
        self.position = None


class Pawn(Piece):
    def __init__(self, board, color, position):
        super().__init__(board, color, position)
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

    def move(self, new_position):
        if new_position in self.chess_board.positions:
            x1, y1 = self.position
            x2, y2 = new_position
            while self.first_move == True:
                if x2 == x1 and y2 == str(int(y1) + 1) or  x2 == x1 and y2 == str(int(y1) + 2):
                    print(self.position, new_position)
                    self.chess_board.positions[self.position] = None
                    self.position = new_position
                    print(self.position)
                self.first_move = False

                if x2 == x1 and y2 == str(int(y1) + 1):
                    print(self.position, new_position)
                    self.chess_board.positions[self.position] = None
                    self.position = new_position
                else:
                    print("Wrong move! Choose the right one.")
                self.chess_board.positions[new_position] = self

    def attack(self, pos):
        if pos in self.chess_board.positions:
            x1, y1 = self.position
            x2, y2 = pos[0], pos[1]
            if self.chess_board.positions[pos] != None:
                if x2 == chr(ord(x1) + 1) and y2 == str(int(y1) + 1) or \
                        x2 == chr(ord(x1) - 1) and y2 == str(int(y1) + 1):
                    self.chess_board.positions[self.position] = None
                    self.chess_board.positions[pos].remove()
                    print("Your " + self.__class__.__name__ + " killed enemy's {0!r}".format(self.chess_board.positions[pos]))
                    self.position = pos
                    self.chess_board.positions[pos] = self

if __name__ == '__main__':
    my_board = ChessBoard("set1")

    p = Pawn(my_board, "white", "c1")
    print(p.position)
    my_board.print_chessboard()

    p.move("c3")
    my_board.print_chessboard()



    # print(p.__dict__)
    print(p.position)
    p.move("c4")
    my_board.print_chessboard()
    p.move("c5")
    my_board.print_chessboard()
    p2 = Pawn(my_board, "black", "b6")
    my_board.print_chessboard()

    p.attack("b6")
    my_board.print_chessboard()



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