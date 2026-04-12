import math
from const_values import *
from info import character, lst_blocks


def click_to_velocity(character, click):
    """click_vers_vitesse assigns the character a velocity thatt corresponds to the
    vector from its current position to the click"""
    x_of_character = character["position"][0]
    y_of_character = character["position"][1]

    x_of_click, y_of_click= click

    """from click to character for physics"""
    dx = x_of_click - x_of_character
    dy = y_of_click - y_of_character

    vector_length = math.sqrt(dx**2 + dy**2)

    if vector_length == 0:
        return 0, 0
    elif vector_length <= vmax:
        return dx, dy
    else:
        return dx / vector_length * vmax, dy / vector_length * vmax


""" with this function we check if the character model 
(all of his rectangle sides) is in collision with any of the blocks in our lst_blocks"""

def collision(character, lst_blocks):
    x, y = character["position"]
    c_left   = x
    c_right  = x + WIDTH
    c_top    = y
    c_bottom = y + HEIGTH

    for bloc in lst_blocks:
        b_left, b_top, b_right, b_bottom = bloc

        if (c_right  > b_left  and
            c_left   < b_right and
            c_bottom > b_top   and
            c_top    < b_bottom):
            return bloc  # collision

    return None  # no collision

print(collision(character, lst_blocks))

def victory(character, lst_blocks):
    pass

def step():
    """pas"""
    pass