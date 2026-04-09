import math
from const_values import *


def click_to_velocity(character, click):
    """click_vers_vitesse assigns the character a velocity thatt corresponds to the
    vector from its current position to the click"""
    x_of_character = character["position"][0]
    y_of_character = character["position"][1]

    x_of_click, y_of_click= click

    dx = x_of_character - x_of_click
    dy = y_of_character - y_of_click

    vector_length = math.sqrt(dx**2 + dy**2)

    if vector_length == 0:
        return 0, 0
    elif vector_length <= vmax:
        return dx, dy
    else:
        return dx / vector_length * vmax, dy / vector_length * vmax



def collision(personnage, lst_blocs):
    pass

def victory(personnage, lst_blocs):
    pass

def step():
    """pas"""
    pass