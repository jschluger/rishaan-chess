from chess import *
from pprint import pprint

if __name__ == '__main__':
    game = ChessGame()
    pawn = WPawn(1, 1, game)

    print('Printing the Chess Board')
    print(game)

    # User clicks on the pawn
    options = pawn.get_valid_moves()
    print("Possible valid moves are ", options)

    target_x, target_y = options[1]
    pawn.move(target_x, target_y)

    # Todo: Add more test cases to complete testing WPawn's get_valid_moves
