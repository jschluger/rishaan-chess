from chess import *
from pprint import pprint

if __name__ == '__main__':
    print('test main')
    game = ChessGame()
    pawn1 = WPawn(1, 1, game)
    pprint(game.board)

    pawn1.get_valid_moves()
