from ctypes.wintypes import tagMSG
from info import *
from fltk import rectangle, cercle


def draw_blocks(lst_blocks):
    """draws blocks"""
    for block in lst_blocks:
        x1, y1, x2, y2 = block
        rectangle(x1, y1, x2, y2, remplissage="green")


def draw_final_object(goal):
    """draws final object that character needs to reach"""
    x1, y1, x2, y2 = goal
    rectangle(x1, y1, x2, y2, remplissage="white")


def draw_character(character):
    """draws character"""
    x, y = character['position']
    cercle(x, y, 15, remplissage="red", tag="mouton")

