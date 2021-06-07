from pprint import pprint


class ChessGame():
    def __init__(self):
        """
    Invariants:
    * self.board[x][y] contains the piece on square (x,y)
    * self.board has 2 kings (unless game over)
    * every piece that hasn't been taken is somewhere in self.board
    * if there is no piece on square (x,y), then self.board[x][y] == None
    """
        self.board = [[None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None]]
        """
    Invariants: 
    * (self.turn == True)  <==> White's Turn
    * (self.turn == False) <==> Black's Turn
    """
        self.turn = True


class WPawn():
    def __init__(self, x, y, game):
        self.x = x
        self.y = y
        self.game = game
        game.board[x][y] = self

    def get_valid_moves(self):
        want_to_check = [(self.x, self.y + 1), (self.x + 1, self.y + 1),
                         (self.x - 1, self.y + 1)]
        print('want_to_check[0]', want_to_check[0])
        result = []
        if self.game.board[want_to_check[0][0]][want_to_check[0][1]] == None:
            result.append(want_to_check[0])

        # ToDo (Rishaan's HW): finish writing this method to consider the rest of
        # the cases, and append any more valid places this pawn can move to result

        print('going to return', result)
        return result
