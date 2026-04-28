from interface import *
from fltk import *
import pygame

cree_fenetre(width, height)

pygame.mixer.init()
pygame.mixer.music.load('Moonpetal.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

start_game, selected_level = draw_main_menu(width, height)
if start_game:
    game(character, lst_blocks, goal)
else:
    character, lst_blocks, goal = open_file(selected_level)
    game(character, lst_blocks, goal)


ferme_fenetre()