import os
import pygame as pg
from pygame.compat import geterror
import chess
import random, time
from wireless import Wireless
import play_chess_graphics
pg.init()

graphics = play_chess_graphics.main('self')

def button(msg, x, y, w, h, ic, ac, surf, action1 =None):
    mouse_position = pg.mouse.get_pos()
    click_tuple = pg.mouse.get_pressed()
    click = list(click_tuple)
    print(click)

    if x+w > mouse_position[0] > x and y+h > mouse_position[1] > y:
        pg.draw.rect(surf, ac,(x,y,w,h))
        if pg.MOUSEBUTTONDOWN and action1 != None:
            action1()
    else:
        pg.draw.rect(surf, ic, (x, y, w, h))

    font = pg.font.Font('calibri-bold-italic.ttf', 20)
    text = font.render(msg, True, (255, 255, 255))
    surf.blit(text, (x + 20, y + 5))
    pg.display.update()

def Lobby_Screen(action =None):
    screen = pg.display.set_mode((800, 600))
    background = pg.image.load('Intro-Background.jpg')
    pg.display.set_caption('PyChess')
    screen.blit(background, (0, 0))
    pg.display.flip()
    button('PLAY', 367, 421, 100, 25, (0, 0, 0), (107, 107, 107), screen, action)
    pg.display.update()

while True:
    Lobby_Screen(graphics)