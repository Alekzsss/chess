from itertools import count


class Player:
    _number = count(1)
    _colors = {"1": "white", "2": "black"}
    _names = []

    def __init__(self, chess_set):
        self.number = next(self._number)
        self.name = input(f"Player {self.number} enter your name: ")
        while len(self.name) < 1 or " " in self.name or self.name in self._names:
            self.name = input(f"Player {self.number} enter right name: ")
        self._names.append(self.name)
        self.chess_set = chess_set

        if len(self._colors) == 1:
            for i in self._colors:
                self.color = self._colors[i]
        else:
            # def a():
            #     print("Choose your color:", end="\n\n")
            #     print("white - '1'")
            #     print("black - '2'")
            color_num = input("""
Choose your color:

white - "1"
black - "2"
""")
            while color_num not in self._colors:
                print("Oops, missprint!")
                color_num = input("Choose another color")
            else:
                self.color = self._colors.pop(color_num)


        self.user_pieces = {piece for piece in self.chess_set.pieces if self.color == piece.color}
        # print(self.user_pieces)
        if self.number == 1:
            print(f"'{self.name}' you are playing on {self.color} side.", "\n")
        else:
            print(f"'So you {self.name}' playing on {self.color} side.", "\n")

    def __repr__(self):
        return self.name

    _first_call = True

    def make_move(self):
        if self._first_call == True:
            print(f"Your turn {self.name}({self.color})")
        else:
            print("Try another one")

        def print_board():
            if self.color == "black":
                self.chess_set.board.print_chessboard()
            else:
                self.chess_set.board.print_chessboard_b()

        piece_position = input("Enter piece position :")
        piece_positions = [piece.position for piece in self.user_pieces]
        # print([piece.position for piece in self.user_pieces])
        while piece_position not in piece_positions:
            piece_position = input("It's not your piece or position mismatch. Enter right piece position :")
        else:
            def pos_to_go():
                # print('func "pos_to_go"')
                position_to_go = input("Choose position to go:")
                while position_to_go not in self.chess_set.board.positions:
                    position_to_go = input("Position out of board! Choose another position:")
                while position_to_go in piece_positions:
                    position_to_go = input("Oops there is your piece. Choose another position:")
                return position_to_go

            # print("check move = ", self.chess_set.board.positions[piece_position].resident.move_check())
            if self.chess_set.board.positions[piece_position].resident.move_check() != False:
                # print(piece_position)
                # print("3")
                # print("feedback")
                feedback = self.chess_set.move(piece_position, pos_to_go())
                # print("feedback = ", feedback)
                while feedback == "again":
                    # print(f"{self.name} сработал 'again'")
                    self._first_call = False
                    if self.make_move() != False:
                        self._first_call = True

                # print("между wrong и False")
                while feedback == "wrong":
                    # print("сработал wrong")
                    feedback = self.chess_set.move(piece_position, pos_to_go())
                print_board()


            else:
                print("You cannot move")
                # print("check attack = ", self.chess_set.board.positions[piece_position].resident.attack_check())
                if self.chess_set.board.positions[piece_position].resident.attack_check() != False:
                    advice = input("""
You can attack or choose another figure:
                        
    1 - to attack
    2 - to choose another piece
    """)

                    if advice == "1":
                        self.chess_set.move(piece_position, pos_to_go())
                        print_board()
                    else:
                        self.make_move()
                else:
                    print("You cannot attack")
                    self.make_move()


if __name__ == '__main__':
    pass