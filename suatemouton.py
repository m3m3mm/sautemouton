from interface import *
from fltk import *
import pygame

cree_fenetre(width, height)

pygame.mixer.init()
pygame.mixer.music.load('Moonpetal.mp3')
pygame.mixer.music.play(-1)

start_game = draw_main_menu(width, height)
if start_game:
    game(character, lst_blocks, goal)


ferme_fenetre()