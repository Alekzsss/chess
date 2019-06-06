from player import Player
from chess_set import ChessSet


def main():
    my_set = ChessSet()
    pl1 = Player(my_set)
    pl2 = Player(my_set)
    my_set.board.print_board()

    while pl1.user_pieces and pl2.user_pieces:
        if pl1.color == "white":
            pl1.make_move()
            if pl2.user_pieces:
                pl2.make_move()
            else:
                break
        else:
            pl2.make_move()
            if pl1.user_pieces:
                pl1.make_move()
            else:
                break
    message = "Congratulations '{}' is a winner!"
    if pl1.user_pieces:
        print(message.format(pl1.name))
    else:
        print(message.format(pl2.name))
    print('\t\t\t"GAME OVER"')


if __name__ == '__main__':
    main()