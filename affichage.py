from ctypes.wintypes import tagMSG
from info import *
from fltk import rectangle, cercle, texte, image, remplissage


def draw_blocks(lst_blocks):
    """draws blocks"""
    for block in lst_blocks:
        x1, y1, x2, y2 = block
        rectangle(x1, y1, x2, y2, remplissage="red")
        image(x1, y1, "block.png", largeur = x2 - x1,
              hauteur = y2 - y1, ancrage="nw")


def draw_final_object(goal):
    """draws final object that character needs to reach"""
    x1, y1, x2, y2 = goal
    rectangle(x1, y1, x2, y2, remplissage="white")


def draw_character(character):
    """draws character"""
    x, y = character['position']
    cercle(x, y, 15, remplissage="red", tag="mouton")


def draw_victory_menu(height, width):
    """draws victory menu"""
    rectangle(100, 130, width-100, height-130, remplissage="red", tag="victory")
    texte(120, 195, "You won!", taille=10, tag="victory")


def create_design():
    """creates design"""
    image(0, 0, "background.ppm", ancrage="nw")

def draw_main_menu():
    """draws main menu"""
