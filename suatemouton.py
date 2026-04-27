from interface import *
from fltk import *

cree_fenetre(width, height)

start_game = draw_main_menu(width, height)
if start_game:
    game(character, lst_blocks, goal)


ferme_fenetre()