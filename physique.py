import math
from const_values import *
from info import character, lst_blocks, goal
from fltk import *
from affichage import draw_character

def click_to_velocity(character, click):
    """click_vers_vitesse assigns the character a velocity that corresponds to the
    vector from its current position to the click"""
    x_of_character = character["position"][0]
    y_of_character = character["position"][1]

    x_of_click, y_of_click = click

    """ from click to character for physics because our x,y is inversed in fltk (y goes down and x goes right) """
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
    c_bottom = y + HEIGHT

    for bloc in lst_blocks:
        b_left, b_top, b_right, b_bottom = bloc

        if (c_right  > b_left  and
            c_left   < b_right and
            c_bottom > b_top   and
            c_top    < b_bottom):
            return bloc  # collision

    return None  # no collision

# print(collision(character, lst_blocks))
"""to check if the character hit anything and push him out of it"""
def hit(character, lst_blocks):
    block_hit = collision(character, lst_blocks)

    if block_hit is None:
        return

    b_left, b_top, b_right, b_bottom = block_hit
    x, y = character["position"]
    vx, vy = character["velocity"]

    if vy >= 0:
        """we count if the mouton is in the block from the top"""
        overlap_y = (y + HEIGHT) - b_top
        """we put the mouton on the top of the block to let him stand on it for the next move"""
        new_y = b_top - HEIGHT
    else:
        """we count if the mouton is in the block from the bottom"""
        overlap_y = b_bottom - y
        """we put the mouton on the bottom of the block to fall"""
        new_y = b_bottom

    if vx >= 0:
        """we check whether the mouton is in the block from the left"""
        overlap_x = (x + WIDTH) - b_left

        new_x = b_left - WIDTH
    else:
        """we count if the mouton is in the block from the right"""
        overlap_x = b_right - x

        new_x = b_right

    """if the mouton is more in the block from the side, than from the top or bottom, we change his x"""
    if overlap_x < overlap_y:
        character["position"] = (new_x, y)
        character["velocity"] = (0, vy)
    else:
        """if the mouton is in the block more from the top or bottom, we change his y"""
        character["position"] = (x, new_y)
        if vy > 0:
            character["velocity"] = (0, 0)
        else:
            character["velocity"] = (vx, 0)


"""to move the character"""
def step(character, lst_blocks): #TODO: figure out what a step() should return and how to work with it
    current_x, current_y = character["position"]
    vx, vy  = character["velocity"]
    new_x = current_x + STEP * vx
    new_y = current_y + STEP * vy

    new_vx = vx + STEP * gravity_x
    new_vy = vy + STEP * gravity_y

    character["position"] = (new_x, new_y)
    character["velocity"] = (new_vx, new_vy)

    hit(character, lst_blocks)

"""basically a loop for step(), but if more complex - does a simulation of a launch of our mouton"""
def simulate(character, lst_blocks):
    while True:
        old_pos = character["position"]
        step(character, lst_blocks)

        efface("mouton")
        efface("vector")
        draw_character(character)
        mise_a_jour()

        if character["position"] == old_pos:
            return


def victory(character, goal):
    x, y = character["position"]
    c_left = x
    c_right = x + WIDTH
    c_top = y
    c_bottom = y + HEIGHT

    g_left, g_top, g_right, g_bottom = goal

    if (c_right > g_left and
            c_left < g_right and
            c_bottom > g_top and
            c_top < g_bottom):
        return True  # collision
    else:
        return False



