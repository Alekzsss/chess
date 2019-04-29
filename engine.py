from player import Player
from chess_set import Chess_set

def main():
    my_set = Chess_set()
    pl1 = Player(my_set)
    pl2 = Player(my_set)

    my_set.board.print_chessboard()

    while pl1.user_pieces and pl2.user_pieces:
        if pl1.color == "white":
            pl1.make_move()
            pl2.make_move()
        else:
            pl2.make_move()
            pl1.make_move()
if __name__ == '__main__':
    main()