from interface import *
from fltk import *
import pygame
from const_values import *

cree_fenetre(width, height)

pygame.mixer.init()
pygame.mixer.music.load('Moonpetal.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

# main loop: menu -> game -> menu -> ...
while True:
    efface_tout()
    start_game, selected_level = draw_main_menu(width, height)

    character, lst_blocks, goal = open_file(selected_level)

    result = game(character, lst_blocks, goal)

    if result == "quit":
        break

    # result == "menu": restart background music and go back to main menu
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Moonpetal.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)


ferme_fenetre()