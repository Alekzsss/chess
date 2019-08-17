from player import Player
from chess_set import ChessSet


def main():
    my_set = ChessSet()
    pl1 = Player(my_set)
    pl2 = Player(my_set)
    my_set.board.print_board()

    attacking, defending = pl1, pl2
    while attacking.pl_pieces and defending.pl_pieces:
        if attacking.color == "white":
            attacking.make_move()
            if defending.pl_pieces:
                defending.make_move()
            else:
                print("Congratulations '{}' is a winner!".format(attacking.name))
                print('\t\t\t"GAME OVER"')
                break
        else:
            attacking, defending = pl2, pl1


if __name__ == '__main__':
    main()
