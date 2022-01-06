from pprint import pprint
from copy import copy, deepcopy


def off_board(x, y):
    retVal = x < 8 and y < 8 and x >= 0 and y >= 0
    return retVal


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
            y = 7 - y
            line = f"y={y} : "
            for x in range(8):
                line += str(self.board[x][y]) + "\t\t"
            retVal = line + "\n\n" + retVal
        retVal += "\t"
        for x in range(8):
            retVal += "..\t\t"
        retVal += "\n\t"
        for x in range(8):
            retVal += f"x={x}\t\t"
        return retVal

    def WPMC(self, piece_x, piece_y, move_x, move_y):
        """
        "Would Put Me in Check?"
        Returns True if moving the piace at (piece_x, piece_y) to (move_x, move_y) 
        would put their own team in check, and False otherwise.
        """
        # In this copy of the board (self), if we moved the piece currently at (piece_x, piece_y)
        # to (move_x, move_y), would the team self.board[cur_x][cur_y].color be in check?

        # Move the piece
        piece = self.board[piece_x][piece_y]
        piece.move(move_x, move_y)

        # Find our king
        for row in self.board:
            for piece in row:
                if piece is not None and piece.color == self.turn and isinstance(
                        piece, King):
                    our_king = piece
                    break

        # Let the opponent play their turn
        self.turn = not self.turn
        for row in self.board:
            for piece in row:
                if piece is not None and piece.color == self.turn:
                    # will run for each piece on the opponent's team (opponent of our_king)
                    moves = piece.get_valid_moves(only_round_one=True)
                    for move in moves:
                        if move == (our_king.x, our_king.y):
                            # They can take the king!
                            return True

        return False


class LogPiece():
    def __init__(self, color, x, y, game):
        self.x = x
        self.y = y
        self.game = game
        game.board[x][y] = self
        """
        Invariants: 
        * (self.color == True)  <==> White
        * (self.color == False) <==> Black
        """
        self.color = color
        self.taken = False
        self.moved = []

        self.extra_direct_conditions = None


    # (target_x, target_y) must be something returned by self.get_valid_moves()
    def move(self, target_x, target_y):
        self.game.board[self.x][self.y] = None
        self.moved.append((target_x,target_y))
        if self.game.board[target_x][target_y] != None:
            self.game.board[target_x][target_y].taken = True
        self.game.board[target_x][target_y] = self

        self.x = target_x
        self.y = target_y


    """Returns True if piece has moved in entire game and False if not"""
    def has_moved(self):
        if len(self.moved) == 0:
            return False
        else:
            return True
    def get_valid_moves(self, only_round_one=False):
        # Round 1: find valid moves based on rules for how the pieces can move
        print(f'get_valid_moves for piece {self}')
        retVal = self.cp_get_valid_moves()
        print(f'Valid moves from cp_get_valid_moves:  {retVal}')
        list2 = self.direct_get_valid_moves()
        print(f'Valid moves from direct_get_valid_moves:  {list2}')
        retVal.extend(list2)

        # Round 2: remove moves that would put your own team in check
        if only_round_one == False:
            retVal = list(
                filter(
                    lambda move: not deepcopy(self.game).WPMC(
                        self.x, self.y, move[0], move[1]), retVal))

        # IN other words (Round 2)...
        # for move in retVal:
        #     copy_of_game = deepcopy(self.game)
        #     if in copy_of_game, it would put me in check to move the piece at self.x, self.y to move[0] move[1]:
        #         remove this move from retVal

        return retVal

    def cp_get_valid_moves(self):
        retVal = []
        for direction in self.cp_to_check:
            dx, dy = direction
            check_x = self.x + dx
            check_y = self.y + dy
            for step in range(8):
                if check_x < 8 and check_y < 8 and check_x >= 0 and check_y >= 0:  # On the board
                    if self.game.board[check_x][check_y] == None:  # Spot empty
                        retVal.append((check_x, check_y))
                    elif self.game.board[check_x][check_y] != None and \
                         self.game.board[check_x][check_y].color != self.color: # Spot contains enemy piece
                        retVal.append((check_x, check_y))
                        break
                    else:  # Spot contains own piece
                        break
                else:  # Off the board
                    break
                check_x = check_x + dx
                check_y = check_y + dy

            # Break to here

        return retVal

    def direct_get_valid_moves(self):
        retVal = []
        for i, (dx, dy) in enumerate(self.direct_to_check):
            if self.x + dx < 8 and self.y + dy < 8 and self.x + dx >= 0 and self.y + dy >= 0:
                if self.game.board[self.x + dx][self.y + dy] == None or (
                        self.game.board[self.x + dx][self.y + dy] != None
                        and self.game.board[self.x + dx][self.y + dy].color !=
                        self.color):
                    if self.extra_direct_conditions is None:
                        retVal.append((self.x + dx, self.y + dy))
                    else:
                        extra_condition = self.extra_direct_conditions[i](
                            self.x + dx, self.y + dy)
                        if extra_condition:
                            retVal.append((self.x + dx, self.y + dy))

        return retVal


class WPawn(LogPiece):
    def __init__(self, x, y, game):
        super().__init__(True, x, y, game)
        self.cp_to_check = []

        self.direct_to_check = [(1, 1), (-1, 1), (0, 1), (0, 2)]
        self.extra_direct_conditions = [
            lambda x, y: self.game.board[x][y] != None,
            lambda x, y: self.game.board[x][y] != None,
            lambda x, y: self.game.board[x][y] == None,
            lambda x, y: self.y == 1 and self.game.board[x][
                y - 1] == None and self.game.board[x][y] == None
        ]

    def __str__(self):
        return "WPawn"

    # Call to switch out this pawn for a piece of type `piece_type`
    # when the pawn has reached the top row.
    def top_row(self, piece_type):
        if piece_type == "Queen":
            Queen(self.x, self.y, self.game)


class BPawn(LogPiece):
    def __init__(self, x, y, game):
        super().__init__(False, x, y, game)
        self.cp_to_check = []

        self.direct_to_check = [(1, -1), (-1, -1), (0, -1), (0, -2)]
        self.extra_direct_conditions = [
            lambda x, y: self.game.board[x][y] != None,
            lambda x, y: self.game.board[x][y] != None,
            lambda x, y: self.game.board[x][y] == None,
            lambda x, y: self.y == 6 and self.game.board[x][
                y + 1] == None and self.game.board[x][y] == None
        ]

    def __str__(self):
        return "BPawn"

    # Call to switch out this pawn for a piece of type `piece_type`
    # when the pawn has reached the top row.
    def top_row(self, piece_type):
        if piece_type == "Queen":
            BQueen(self.x, self.y, self.game)


class Rook(LogPiece):
    def __init__(self, x, y, color, game):
        super().__init__(color, x, y, game)
        self.cp_to_check = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.direct_to_check = []

        def __str__(self):
            return f"{'W' if self.color else 'B'}Rook"


class Knight(LogPiece):
    def __init__(self, x, y, color, game):
        super().__init__(color, x, y, game)
        self.direct_to_check = [
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
        ]
        self.cp_to_check = []

    def __str__(self):
        return f"{'W' if self.color else 'B'}Knight"

    # Return a list of the current (x,y) coordinates that this piece can move to
    # on this turn.
    # def get_valid_moves(self):
    #     retVal = []
    #     for (dx, dy) in self.to_check:
    #         if self.x + dx < 8 and self.y + dy < 8 and self.x + dx >= 0 and self.y + dy >= 0:
    #             if self.game.board[self.x + dx][self.y + dy] == None or (
    #                     self.game.board[self.x + dx][self.y + dy] != None
    #                     and self.game.board[self.x + dx][self.y + dy].color !=
    #                     self.color):
    #                 retVal.append((self.x + dx, self.y + dy))

    #     return retVal

    # Call to switch out this pawn for a piece of type `piece_type`
    # when the pawn has reached the top row.
    def top_row(self, piece_type):
        raise NotImplementedError()  # Do we need to implement this?


class Bishop(LogPiece):
    def __init__(self, x, y, color, game):
        super().__init__(color, x, y, game)
        self.direct_to_check = []
        self.cp_to_check = [(1, 1), (-1, 1), (-1, -1), (1, -1)]

    def __str__(self):
        return f"{'W' if self.color else 'B'}Bishop"


class Queen(LogPiece):
    def __init__(self, x, y, color, game):
        super().__init__(color, x, y, game)
        self.direct_to_check = []
        self.cp_to_check = [(1, 1), (-1, 1), (-1, -1), (1, -1), (1, 0), (0, 1),
                            (-1, 0), (0, -1)]

    def __str__(self):
        return f"{'W' if self.color else 'B'}Queen"


class King(LogPiece):
    def __init__(self, x, y, color, game):
        super().__init__(color, x, y, game)

        self.direct_to_check = [(1, 1), (-1, 1), (-1, -1), (1, -1), (1, 0),
                                (0, 1), (-1, 0), (0, -1)]
        self.cp_to_check = []

    def get_valid_moves(self, only_round_one=False):
        # Round 1: find valid moves based on rules for how the pieces can move
        print(f'get_valid_moves for piece {self}')
        retVal = self.cp_get_valid_moves()
        print(f'Valid moves from cp_get_valid_moves:  {retVal}')
        list2 = self.direct_get_valid_moves()
        print(f'Valid moves from direct_get_valid_moves:  {list2}')
        retVal.extend(list2)
        # Finding castling
        if self.has_moved() is not True:
            if self.game.board[self.x + 1][self.y] == None and self.game.board[self.x + 2][self.y] == None:
                rook = self.game.board[self.x + 3][self.y]
                if rook != None:
                    if rook.has_moved() is not True:
                        retVal.append((self.x + 2, self.y))
        # Round 2: remove moves that would put your own team in check
        if only_round_one == False:
            retVal = list(
                filter(
                    lambda move: not deepcopy(self.game).WPMC(
                        self.x, self.y, move[0], move[1]), retVal))

        # IN other words (Round 2)...
        # for move in retVal:
        #     copy_of_game = deepcopy(self.game)
        #     if in copy_of_game, it would put me in check to move the piece at self.x, self.y to move[0] move[1]:
        #         remove this move from retVal

        return retVal
    def __str__(self):
        return f"{'W' if self.color else 'B'}King"
