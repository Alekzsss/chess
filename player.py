from itertools import count


class Player:
    _number = count(1)
    _colors = ["white", "black"]
    _names = []

    def __init__(self, chess_set):
        self.number = next(self._number)
        self.name = None
        self.color = None
        self.chess_set = chess_set
        self.pl_pieces = [piece for piece in self.chess_set.pieces if self.color == piece.color]

        self.chess_set.players.append(self)
        print(f"'{self.name}' you are playing on {self.color} side.", "\n") if self.number == 1 \
            else print(f"'So you {self.name}' playing on {self.color} side.", "\n")  # print notification message to
        # players
        self.move_history = []

    # @property
    # def pl_pieces(self):
    #     return [piece for piece in self.chess_set.pieces if self.color == piece.color]

    @property
    def pieces_positions(self):
        return [piece.position for piece in self.pl_pieces]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        while not value:
            message = f"Player {self.number} enter your name: "
            while True:
                try:
                    value = input(message)
                    if " " in value or value in self._names:
                        raise Exception
                except:
                    print("Choose another name)")
                    message = f"Player {self.number} enter right name: "
                else:
                    break
        self._name = value
        self._names.append(self._name)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        while not value:
            if len(self._colors) == 1:
                value = self._colors[0]
                self._color = value
            else:
                while True:
                    try:
                        color_num = int(input('Choose your color:\n\nwhite - "1"\nblack - "2"\n'))
                        if color_num not in (1, 2):
                            raise Exception
                    except:
                        print("Oops, missprint!")
                    else:
                        break
                value = self._colors.pop(color_num - 1)
                self._color = value

    def __repr__(self):
        return self.name

    @property
    def king(self):
        return [piece for piece in self.pl_pieces if type(piece).__name__ == "King"][0]

    @property
    def army_pos(self):
        return [piece.position for piece in self.pl_pieces]

    @property
    def army_move_pos(self):
        all_pos = set()
        for piece in self.pl_pieces:
            if type(piece).__name__ != "King":
                all_pos.update(piece.move_positions())
        return all_pos

    @property
    def army_attack_pos(self):
        all_pos = set()
        for piece in self.pl_pieces:
            if type(piece).__name__ != "King":
                all_pos.update(piece.attack_positions())
        return all_pos

    @property  # return enemy`s all pieces
    def enemy_army(self):
        return set(self.chess_set.pieces) - set(self.pl_pieces)

    @property  # return all positions of enemy`s pieces
    def all_enemy_pos(self):
        all_enemy_pos = set()
        for piece in self.enemy_army:
            all_enemy_pos.add(piece.position)
        return all_enemy_pos

    @property  # return all positions that are under enemy`s attack
    def enemy_attack_pos(self):
        all_pos = set()
        for piece in self.enemy_army:
            all_pos.update(piece.attack_positions())
        return all_pos

    @property  # return all positions that enemy can move on
    def enemy_move_pos(self):
        all_pos = set()
        for piece in self.enemy_army:
            all_pos.update(piece.move_positions())
        return all_pos

    def make_move(self):
        # check for CHECK or CHECKMATE
        check_makers = [piece for piece in self.enemy_army if self.king.position in piece.attack_positions()]
        while True:
            try:
                if len(check_makers) == 1:
                    check_maker = [p for p in check_makers][0]
                    # print("check_maker.position = ", check_maker.position)
                    # print("self.king.position in all_enemy_attack_pos = ", self.king.position in self.enemy_attack_pos)
                    # print("self.king.move_positions() - all_enemy_attack_pos == set()", self.king.move_positions() - self.enemy_attack_pos == set())
                    # print("self.king.move_positions() = ", self.king.move_positions())
                    # print("enemy army")
                    # for piece in self.enemy_army:
                    #     print(type(piece).__name__, "=", piece.attack_positions())
                    # print("self.king.move_positions() = ", self.king.move_positions(), "self.army_move_pos = ", self.army_move_pos)
                    # print("self.king.move_positions() & self_army_move_pos = ", self.king.move_positions() & self.army_move_pos)
                    # print("check_maker.position = ", check_maker.position, ", self.army_attack_pos = ", self.army_attack_pos)
                    # for piece in self.pl_pieces:
                    #     if type(piece).__name__ != "King":
                    #         print(type(piece).__name__, "=", piece.attack_positions())
                    # print("check_maker.position in self_army_attack_pos = ", check_maker.position in self.army_attack_pos)
                    # print("type(check_maker).__name__ = ", type(check_maker).__name__)
                    if self.king.position in self.enemy_attack_pos and \
                            self.king.move_positions() - self.enemy_attack_pos == set() and \
                            type(check_maker).__name__ == "Knight" and \
                            check_maker.position not in self.army_attack_pos:
                        raise ValueError
                    elif self.king.position in self.enemy_attack_pos and \
                            self.king.move_positions() - self.enemy_attack_pos == set() and \
                            check_maker.position not in self.king.attack_positions() and \
                            check_maker.position not in self.army_attack_pos and\
                            not check_maker.obstacles(self.king.position, self.enemy_move_pos):
                        raise ValueError
                    elif self.king.position in self.enemy_attack_pos:
                        raise KeyError
                elif len(check_makers) > 1:
                    check_makers_pos = set()
                    for piece in check_makers:
                        check_makers_pos.update(piece.position())
                    closest_enemy = self.king.attack_positions() & check_makers_pos
                    if self.king in self.enemy_attack_pos and \
                        closest_enemy == set() and \
                        self.king.move_positions() - self.enemy_attack_pos == set():
                        raise ValueError
                    elif self.king in self.enemy_attack_pos and \
                        self.king.move_positions() - self.enemy_attack_pos == set() and \
                        closest_enemy != set() and \
                        closest_enemy.rear_cover(self.enemy_army):
                        raise ValueError
                    elif self.king.position in self.enemy_attack_pos:
                        raise KeyError
            except ValueError:
                print("CHECKMATE!!!")
                self.pl_pieces = []
                return
            except KeyError:
                print(f"CHECK!!!\n{self.name} you need to hide your king!")
                self.chess_set.move_piece(self)
                return
            else:
                break
        print('Yet no "Check"')

        print(f"Your turn {self.name}({self.color})\n")
        # delegate move function to class "chess_set"
        self.chess_set.move_piece(self)


if __name__ == '__main__':
    pass
