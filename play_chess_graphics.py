#!/usr/bin/env python
""" pygame.examples.pawn

This simple example is used for the line-by-line tutorial
that comes with pygame. It is based on a 'popular' web banner.
Note there are comments here, but for the full explanation,
follow along in the tutorial.
"""

# Import Modules
import os
import pygame as pg
from pygame.compat import geterror
import chess
import random

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


# functions to create our resources
def load_image(name, colorkey=None):
    fullname = os.path.join(data_dir, name)
    try:
        image = pg.image.load(name)
    except pg.error:
        print("Cannot load image:", fullname)
        raise SystemExit(str(geterror()))
    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)
    return image, image.get_rect()


def load_sound(name):
    class NoneSound:
        def play(self):
            pass

    if not pg.mixer or not pg.mixer.get_init():
        return NoneSound()
    fullname = os.path.join(data_dir, name)
    try:
        sound = pg.mixer.Sound(fullname)
    except pg.error:
        print("Cannot load sound: %s" % fullname)
        raise SystemExit(str(geterror()))
    return sound


class Piece(pg.sprite.Sprite):
    def __init__(self, image_name, my_x, my_y):
        pp = board_pixel(my_x, my_y)
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image(image_name, -1)
        self.image = pg.transform.scale(self.image,
                                        (BOARD_WIDTH // 8, BOARD_HEIGHT // 8))
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


def board_pixel(x, y):
    """0,0 is Top Left Corner"""
    """board coord to pixel coord"""
    result = (x * SQUARE_W + X_OFFSET, y * SQUARE_H + Y_OFFSET)
    return result


def pixel_board(x, y):
    """pixel coord to board coord"""
    result = (int((x - X_OFFSET) / SQUARE_W), int((y - Y_OFFSET) / SQUARE_H))
    return result


def main():
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
    bpawn = Bpawn(0, 6, logGame)
    wpawn = Wpawn(0, 1, logGame)
    allsprites = pg.sprite.RenderPlain(
        (bpawn.graphicPiece, wpawn.graphicPiece))
    all_pieces = [bpawn, wpawn]
    # Main Loop
    print(logGame)
    play_turn(True, logGame, clock, screen, background, allsprites, all_pieces)
    pg.quit()


def play_turn(color, logGame, clock, screen, background, allsprites,
              all_pieces):
    going = True
    holding = False
    while going:
        clock.tick(60)
        # Handle Input Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                going = False

        # Actual Code starts
        if pg.mouse.get_pressed()[0]:  # If mouse pressed
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
                    # ToDo: Highlight the valid moves on the board

            else:  # What to do if holding a piece
                if (x_boardpos, y_boardpos) in valid_moves:

                    logGame.board[last_x_boardpos][last_y_boardpos] = None

                    logGame.board[x_boardpos][y_boardpos] = piece

                    piece.x = x_boardpos
                    piece.y = y_boardpos

                else:
                    holding = False

                # ToDo: Stop highlighting valid moves

        # Draw Everything
        update_piece_positions(all_pieces)
        screen.blit(background, (0, 0))
        if holding:
            for valid_move in valid_moves:
                loc = board_pixel(valid_move[0], valid_move[1])
                rect = (loc[0], loc[1], SQUARE_W, SQUARE_H)
                screen.fill((189, 209, 255), rect=rect)
        allsprites.draw(screen)
        pg.display.flip()


def update_piece_positions(all_pieces):
    for piece in all_pieces:
        real_location = board_pixel(piece.logicalPiece.x, piece.logicalPiece.y)
        # print(
        #     f'piece.graphicPiece.rect.topleft: {piece.graphicPiece.rect.topleft}'
        # )
        # print(f'real_location: {real_location}')
        if piece.graphicPiece.rect.topleft != real_location:
            piece.graphicPiece.rect.topleft = real_location


# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()
