from chess import *
from pprint import pprint

if __name__ == '__main__':
    game = ChessGame()
    pawns = []
    for x in range(8):
        new_pawn = WPawn(x, 1, game)
        pawns.append(new_pawn)
    # print('Printing the Chess Board')
    # print(game)

    print('Running test cases...')
    print(0, pawns[0].get_valid_moves())  # should return [(0,2),(0,3)]
    print('\t should return [(0,2),(0,3)]')
    print(1, pawns[1].get_valid_moves())  # should return [(1,2),(1,3)]
    print('\t should return [(1,2),(1,3)]')

    test_bpawn1 = BPawn(3, 3, game)

    # print('Printing the Chess Board')
    # print(game)

    print(2, pawns[3].get_valid_moves())  # should return [(3,2)]
    print('\t should return [(3,2)]')

    test_bpawn1 = BPawn(5, 2, game)

    # print('Printing the Chess Board')
    # print(game)

    top_pawn = WPawn(5, 7, game)
    print('Printing the Chess Board before top_pawn.top_row("Queen")')
    print(game)
    top_pawn.top_row("Queen")
    print('Printing the Chess Board after top_pawn.top_row("Queen")')
    print(game)

    # Todo: Add more test cases to complete testing WPawn's get_valid_moves
