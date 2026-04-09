from ctypes.wintypes import tagMSG
from info import *
from fltk import rectangle, cercle


def draw_blocks(lst_blocks):
    """draws blocks"""
    for block in lst_blocks:
        x1, y1 = block[0]
        x2, y2 = block[1]
        rectangle(x1, y1, x2, y2)


def draw_final_object(goal):
    """draws final object that character needs to reach"""
    x1, y1 = goal[0]
    x2, y2 = goal[1]
    rectangle(x1, y1, x2, y2)


def draw_character(character):
    """draws character"""
    x, y = character['position']
    cercle(x, y, 15, remplissage="red", tag="mouton")

