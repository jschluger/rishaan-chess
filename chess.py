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

    def __str__(self):
        retVal = ""
        for y in range(8):
            line = f"y={y} : "
            for x in range(8):
                line += str(self.board[x][y]) + "\t"
            retVal = line + "\n" + retVal
        retVal += "\t"
        for x in range(8):
            retVal += "..\t"
        retVal += "\n\t"
        for x in range(8):
            retVal += f"x={x}\t"
        return retVal


class WPawn():
    def __init__(self, x, y, game):
        self.x = x
        self.y = y
        self.game = game
        game.board[x][y] = self
        """
        Invariants: 
        * (self.color == True)  <==> White
        * (self.color == False) <==> Black
        """
        self.color = True

    def __str__(self):
        return "WPawn"

    # Return a list of the current (x,y) coordinates that this piece can move to
    # on this turn.
    def get_valid_moves(self):
        retVal = []
        if self.game.board[self.x][self.y + 1] == None:
            retVal.append((self.x, self.y + 1))

        if self.y == 1 and \
            self.game.board[self.x][self.y + 1] == None and \
                 self.game.board[self.x][self.y + 2] == None:
            retVal.append((self.x, self.y + 2))

        if self.game.board[self.x+1][self.y+1] != None and \
            self.game.board[self.x+1][self.y+1].color == False:
            retVal.append((self.x + 1, self.y + 1))

        if self.game.board[self.x-1][self.y+1] != None and \
            self.game.board[self.x-1][self.y+1].color == False:
            retVal.append((self.x - 1, self.y + 1))

        return retVal

    # Call to switch out this pawn for a piece of type `piece_type`
    # when the pawn has reached the top row.
    def top_row(self, piece_type):
        if piece_type == "Queen":
            WQueen(self.x, self.y, self.game)

    # (target_x, target_y) must be something returned by self.get_valid_moves()
    def move(self, target_x, target_y):
        self.game.board[self.x][self.y] = None
        self.game.board[target_x][target_y] = self
        self.x = target_x
        self.y = target_y


class BPawn():
    def __init__(self, x, y, game):
        self.x = x
        self.y = y
        self.game = game
        game.board[x][y] = self
        """
        Invariants: 
        * (self.color == True)  <==> White
        * (self.color == False) <==> Black
        """
        self.color = False

    def __str__(self):
        return "BPawn"


class WQueen():
    def __init__(self, x, y, game):
        self.x = x
        self.y = y
        self.game = game
        game.board[x][y] = self
        """
        Invariants: 
        * (self.color == True)  <==> White
        * (self.color == False) <==> Black
        """
        self.color = False

    def __str__(self):
        return "WQueen"

    # Return a list of the current (x,y) coordinates that this piece can move to
    # on this turn.
    def get_valid_moves(self):
        retVal = []
        # Todo for Homework
        return retVal