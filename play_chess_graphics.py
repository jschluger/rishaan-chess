#!/usr/bin/env python
""" pygame.examples.pawn

This simple example is used for the line-by-line tutorial
that comes with pygame. It is based on a 'popular' web banner.
Note there are comments here, but for the full explanation,
follow along in the tutorial.
"""
"""Testing GitHub"""
# Import Modules
import os
import pygame as pg
from pygame.compat import geterror
import chess
import random, time
from wireless import Wireless

if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

X_OFFSET = 0  ## 2
Y_OFFSET = 0  ## 6
SQUARE_W = 50
SQUARE_H = 50

BOARD_WIDTH = SQUARE_W * 8
BOARD_HEIGHT = SQUARE_H * 8

PIECE_WIDTH = 50
PIECE_HEIGHT = 50


# functions to create our resources
def load_image(name, colorkey=None):
    fullname = os.path.join(data_dir, name)
    try:
        image = pg.image.load(name).convert_alpha()
    except pg.error:
        print("Cannot load image:", fullname)
        raise SystemExit(str(geterror()))
    # image = image.convert()
    # if colorkey is not None:
    #     if colorkey == -1:
    #         colorkey = image.get_at((0, 0))
    #     image.set_colorkey(colorkey, pg.RLEACCEL)
    return image, image.get_rect()


def load_sound(name):
    class NoneSound:
        def play(self):
            pass

    if not pg.mixer or not pg.mixer.get_init():
        return NoneSound()

    fullname = os.path.join(data_dir, name)
    sound = pg.mixer.Sound(fullname)


    return sound

# Set volume for background music
volume_input = input('What volume would you like your music at (Between 0 and 0.1): ')
volume = float(volume_input)
pg.mixer.music.set_volume(volume)

# Start playing background music
pg.mixer.init()
pg.mixer.music.load('Chess-Music.mp3')
pg.mixer.music.play(-1)


class Piece(pg.sprite.DirtySprite):
    def __init__(self, image_name, my_x, my_y):
        pp = board_pixel(my_x, my_y)
        pg.sprite.DirtySprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image(image_name, -1)
        # self.image = self.image.convert_alpha()
        self.image = pg.transform.scale(self.image,
                                        (PIECE_WIDTH, PIECE_HEIGHT))
        self.imagename = image_name
        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = pp[0], pp[1]
        self.move = 10
        self.clicked = 0
        # put piece at my_x, my_y in board

    def update(self):
        """ Method called when updating a sprite. """
        """ ## Means that that line has to be uncommented"""
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        # print(pg.mouse.get_pressed())
        # print(self.imagename)
        pass

    def _walk(self):
        """move the monkey across the screen, and turn at the ends, leftover"""
        newpos = self.rect.move((self.move, 0))
        # print("self.move", self.move, "self.area", self.area)
        if not self.area.contains(newpos):
            if self.rect.left < self.area.left or self.rect.right > self.area.right:
                self.move = -self.move
                newpos = self.rect.move((self.move, 0))
                self.image = pg.transform.flip(self.image, 1, 0)
        self.rect = newpos


class Bpawn():
    def __init__(self, my_x, my_y, logGame):
        self.graphicPiece = Piece("black_pawn.png", my_x, my_y)
        self.logicalPiece = chess.BPawn(my_x, my_y, logGame)


class Wpawn():
    def __init__(self, my_x, my_y, logGame):
        self.graphicPiece = Piece("white_pawn.png", my_x, my_y)
        self.logicalPiece = chess.WPawn(my_x, my_y, logGame)


class Wknight():
    def __init__(self, my_x, my_y, logGame):
        self.graphicPiece = Piece("white_knight.png", my_x, my_y)
        self.logicalPiece = chess.Knight(my_x, my_y, True, logGame)


class Bknight():
    def __init__(self, my_x, my_y, logGame):
        self.graphicPiece = Piece("black_knight.png", my_x, my_y)
        self.logicalPiece = chess.Knight(my_x, my_y, False, logGame)


class Wrook():
    def __init__(self, my_x, my_y, logGame):
        self.graphicPiece = Piece("white_rook.png", my_x, my_y)
        self.logicalPiece = chess.Rook(my_x, my_y, True,
                                       logGame)  # This isn't defined yet


class Brook():
    def __init__(self, my_x, my_y, logGame):
        self.graphicPiece = Piece("black_rook.png", my_x, my_y)
        self.logicalPiece = chess.Rook(my_x, my_y, False,
                                       logGame)  # This isn't defined yet


class BBishop():
    def __init__(self, my_x, my_y, logGame):
        self.graphicPiece = Piece("black_bishop.png", my_x, my_y)
        self.logicalPiece = chess.Bishop(my_x, my_y, False, logGame)


class WBishop():
    def __init__(self, my_x, my_y, logGame):
        self.graphicPiece = Piece("white_bishop.png", my_x, my_y)
        self.logicalPiece = chess.Bishop(my_x, my_y, True, logGame)


class WQueen():
    def __init__(self, my_x, my_y, logGame):
        self.graphicPiece = Piece("white_queen.png", my_x, my_y)
        self.logicalPiece = chess.Queen(my_x, my_y, True, logGame)


class BQueen():
    def __init__(self, my_x, my_y, logGame):
        self.graphicPiece = Piece("black_queen.png", my_x, my_y)
        self.logicalPiece = chess.Queen(my_x, my_y, False, logGame)


class WKing():
    def __init__(self, my_x, my_y, logGame):
        self.graphicPiece = Piece("white_king.png", my_x, my_y)
        self.logicalPiece = chess.King(my_x, my_y, True, logGame)


class BKing():
    def __init__(self, my_x, my_y, logGame):
        self.graphicPiece = Piece("black_king.png", my_x, my_y)
        self.logicalPiece = chess.King(my_x, my_y, False, logGame)


def board_pixel(x, y):
    """0,0 is Top Left Corner"""
    """board coord to pixel coord"""
    result = (x * SQUARE_W + X_OFFSET, y * SQUARE_H + Y_OFFSET)
    return result


def pixel_board(x, y):
    """pixel coord to board coord"""
    result = (int((x - X_OFFSET) / SQUARE_W), int((y - Y_OFFSET) / SQUARE_H))
    return result


def main(mode):
    # Set up the logistics
    logGame = chess.ChessGame()

    # Set up the Graphics
    """this function is called when the program starts.
      it initializes everything it needs, then runs in
      a loop until the function returns."""
    # Initialize Everything
    pg.init()
    screen = pg.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
    pg.display.set_caption("Chess")
    pg.mouse.set_visible(1)

    # Create The Backgound
    # background = pg.Surface(screen.get_size())
    # background = background.convert()
    # background.fill((167, 199, 178))
    background = pg.image.load("chess board3.png")
    background = pg.transform.scale(background, (BOARD_WIDTH, BOARD_HEIGHT))
    screen.blit(background, (0, 0))

    # Display The Background
    # screen.blit(background, (0, 0))
    # pg.display.flip()

    # Prepare Game Objects
    clock = pg.time.Clock()
    # whiff_sound = load_sound("whiff.wav")
    # punch_sound = load_sound("punch.wav")
    x_offset = 2
    y_offset = 6
    square_w = 50
    square_h = 50
    bpawn1 = Bpawn(0, 6, logGame)
    bpawn2 = Bpawn(1, 6, logGame)
    bpawn3 = Bpawn(2, 6, logGame)
    bpawn4 = Bpawn(3, 6, logGame)
    bpawn5 = Bpawn(4, 6, logGame)
    bpawn6 = Bpawn(5, 6, logGame)
    bpawn7 = Bpawn(6, 6, logGame)
    bpawn8 = Bpawn(7, 6, logGame)
    wpawn1 = Wpawn(0, 1, logGame)
    wpawn2 = Wpawn(1, 1, logGame)
    wpawn3 = Wpawn(2, 1, logGame)
    wpawn4 = Wpawn(3, 1, logGame)
    wpawn5 = Wpawn(4, 1, logGame)
    wpawn6 = Wpawn(5, 1, logGame)
    wpawn7 = Wpawn(6, 1, logGame)
    wpawn8 = Wpawn(7, 1, logGame)
    bknight1 = Bknight(1, 7, logGame)
    bknight2 = Bknight(6, 7, logGame)
    wknight1 = Wknight(1, 0, logGame)
    wknight2 = Wknight(6, 0, logGame)
    wrook1 = Wrook(0, 0, logGame)
    wrook2 = Wrook(7, 0, logGame)
    brook1 = Brook(0, 7, logGame)
    brook2 = Brook(7, 7, logGame)
    bbishop1 = BBishop(2, 7, logGame)
    bbishop2 = BBishop(5, 7, logGame)
    wbishop1 = WBishop(2, 0, logGame)
    wbishop2 = WBishop(5, 0, logGame)
    wqueen1 = WQueen(3, 0, logGame)
    bqueen1 = BQueen(3, 7, logGame)
    wking1 = WKing(4, 0, logGame)
    bking1 = BKing(4, 7, logGame)
    # Did it!

    all_pieces = [
        bpawn1, wpawn1, bpawn2, wpawn2, bpawn3, wpawn3, bpawn4, wpawn4, bpawn5,
        wpawn5, bpawn6, wpawn6, bpawn7, wpawn7, bpawn8, wpawn8, bknight1,
        bknight2, wknight1, wknight2, wrook1, wrook2, brook1, brook2, bbishop1,
        bbishop2, wbishop1, wbishop2, wqueen1, bqueen1, wking1, bking1
    ]
    if mode != 'self':
        wireless = Wireless(mode)
    else:
        wireless = None   

    if mode == 'server':
        my_team = True
    elif mode == 'client':
        my_team = False
    else:
        my_team = None

    # Main Loop
    print(logGame)
    play_turn(True, logGame, clock, screen, background, all_pieces, wireless, 0, my_team)
    pg.quit()

# Draw Everything
def draw(all_pieces, screen, background, logGame, holding=False, valid_moves=None):
    all_pieces = update_piece_positions(all_pieces)

    screen.blit(background, (0, 0))
    if holding:
        for valid_move in valid_moves:
            loc = board_pixel(valid_move[0], valid_move[1])
            rect = (loc[0], loc[1], SQUARE_W, SQUARE_H)
            screen.fill((189, 209, 255), rect=rect)

    # Highlighting at risk pieces
    for row in logGame.board:
        for test_piece in row:
            if test_piece is not None and isinstance(test_piece, chess.King) and test_piece.is_threatened():
                loc = board_pixel(test_piece.x, test_piece.y)
                rect = (loc[0], loc[1], SQUARE_W, SQUARE_H)
                screen.fill((217, 83, 74), rect=rect)


    allsprites = pg.sprite.RenderPlain(
        [piece.graphicPiece for piece in all_pieces])
    allsprites.draw(screen)
    pg.display.flip()

    return all_pieces


def play_turn(color, logGame, clock, screen, background, all_pieces, wireless, counter, my_team):
    # whites turn <==> color == True    -> Next play_turn needs color=False
    # blacks turn <==> color == False   -> Next play_turn needs color=True
    # Problem: logGame.turn is not up to date
    #Replicating our opponents turn 
    
    # Start our own turn
    logGame.turn = color

    # Detect checkmate
    if logGame.in_checkmate(color):
        exit(f'{"Black" if color else "White"} wins!')

    if wireless != None:
        if (my_team == False and counter % 2 == 0) or (my_team == True and counter % 2 == 1):
            all_pieces = draw(all_pieces, screen, background, logGame)
            recieved = wireless.recv_message()

            last_x_boardpos, last_y_boardpos = recieved[0]
            x_boardpos, y_boardpos = recieved[1]

            piece = logGame.board[last_x_boardpos][last_y_boardpos]
            piece.move(x_boardpos, y_boardpos)
            # Check what piece is actually on the board
            real_piece = logGame.board[x_boardpos][y_boardpos]

            if piece != real_piece:
                # We just swapped out a pawn on the top row
                # piece is the old pawn
                # real_piece is the new replacement

                # Filter the pawn out of all_pieces
                all_pieces = list(filter(lambda z: z.logicalPiece != piece, all_pieces))

                if real_piece.color:
                    all_pieces.append( WQueen(x_boardpos, y_boardpos, logGame) )
                else:
                    all_pieces.append( BQueen(x_boardpos, y_boardpos, logGame) )
            
            counter += 1
            play_turn(not color, logGame, clock, screen, background, all_pieces, wireless, counter, my_team)
            return
            
        #####################   
    

    going = True
    holding = False
    valid_moves = None 
    last_click_time = 0
    while going:
        clock.tick(60)
        # Handle Input Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                going = False

        # Actual Code starts
        if pg.mouse.get_pressed(
        )[0] and time.time() - last_click_time >= 1:  # If mouse pressed
            last_click_time = time.time()
            x_pixelpos, y_pixelpos = pg.mouse.get_pos()
            print('\nPixel pos is', x_pixelpos, y_pixelpos)
            x_boardpos, y_boardpos = pixel_board(x_pixelpos, y_pixelpos)
            print('Board pos is', x_boardpos, y_boardpos)

            if not holding:  # What to do if not holding a piece
                piece = logGame.board[x_boardpos][y_boardpos]
                last_x_boardpos = x_boardpos
                last_y_boardpos = y_boardpos

                print('found piece', piece)
                if piece is not None and color == piece.color:
                    valid_moves = piece.get_valid_moves()
                    holding = True
                    print('Valid Moves are', valid_moves)
                    # I think we did it

            else:  # What to do if holding a piece
                if (x_boardpos, y_boardpos) in valid_moves:

                    piece.move(x_boardpos, y_boardpos)

                    # Pause background music
                    pg.mixer.music.pause()
                    # Load and play click sound
                    placement_audio = pg.mixer.Sound('Chess_Piece_Audio.wav')
                    placement_audio.play()
                    # Unpause background music
                    pg.mixer.music.unpause()

                    # Check what piece is actually on the board
                    real_piece = logGame.board[x_boardpos][y_boardpos]

                    if piece != real_piece:
                        # We just swapped out a pawn on the top row
                        # piece is the old pawn
                        # real_piece is the new replacement

                        # Filter the pawn out of all_pieces
                        all_pieces = list(filter(lambda z: z.logicalPiece != piece, all_pieces))

                        if real_piece.color:
                            all_pieces.append( WQueen(x_boardpos, y_boardpos, logGame) )
                        else:
                            all_pieces.append( BQueen(x_boardpos, y_boardpos, logGame) )

                    # We just moved the piece
                    going = False
                    print(f'all_pieces has {len(all_pieces)} pieces')
                else:

                    holding = False

        all_pieces = draw(all_pieces, screen, background, logGame, holding=holding, valid_moves=valid_moves)
        
    if wireless != None:
        message = ((last_x_boardpos, last_y_boardpos), (x_boardpos, y_boardpos))
        # message[0] is the old position (message[0][1] is the y coordinate of the old position)
        # message[1] is the new position (message[1][0] is the x coordinate of the new position)
        sent = wireless.send_message(message)
    
    counter += 1
    play_turn(not color, logGame, clock, screen, background, all_pieces, wireless, counter, my_team)

def update_piece_positions(pieces):
    # Should return the updated list of all_pieces
    pieces = list(filter(lambda piece: not piece.logicalPiece.taken, pieces))

    for piece in pieces:
        real_location = board_pixel(piece.logicalPiece.x, piece.logicalPiece.y)
        if piece.graphicPiece.rect.topleft != real_location:
            piece.graphicPiece.rect.topleft = real_location
    return pieces


# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    mode = input('Which game mode (server, client, self) would you like to play in: ')
    if mode == 'server' or mode == 'SERVER' or mode == 'Server':
        mode = 'server'
    elif mode == 'self' or mode == 'SELF' or mode == 'Self':
        mode = 'self'
    else:
        mode = 'client'
    main(mode)