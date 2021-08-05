from chess import *
from pprint import pprint

if __name__ == '__main__':
    game = ChessGame()
    for x in range(8):
        WPawn(x, 1, game)
        BPawn(x, 6, game)

    while True:
        print("\n---------------------------------")
        print(game)
        print("turn is ", game.turn)
        print("pick up a piece (enter the coordinates):")
        print("x:")
        x = int(input().strip())
        print("y: ")
        y = int(input().strip())
        piece = game.board[x][y]
        print('found piece ', piece)
        if piece is None:
            continue
        if piece.color != game.turn:
            print(
                f"turn is {game.turn} but you picked up a {piece.color} colored piece"
            )
            continue
        moves = piece.get_valid_moves()
        print('valid moves are ', moves)
        if len(moves) == 0:
            print("try moving a different piece, no valid moves found")
            continue

        print("where do you want to move? (enter the coordinates)")
        print("x:")
        x = int(input().strip())
        print("y: ")
        y = int(input().strip())

        if (x, y) not in moves:
            print(
                f"trying to move to ({x},{y}), which is not currently a valid move"
            )
            print("try moving to a different space")
            continue

        piece.move(x, y)
        game.turn = not game.turn
