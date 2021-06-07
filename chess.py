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
    self.board = [[None] * 8] * 8

    """
    Invariants: 
    * (self.turn == True)  <==> White's Turn
    * (self.turn == False) <==> Black's Turn
    """
    self.turn = True
    self.place_pieces()


    def place_pieces(self):
      self.board[1][2] = Piece()

class Piece():
  def __init__(self):
    """
    Invariants: 
    * 
    """
    self.possible_moves = _____________

    """
    Invariants: 
    * 
    """
    self.possible_takes = _____________

