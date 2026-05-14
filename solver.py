from const_values import *
from fltk import *
from physique import *
from info import goal
from time import sleep

def solver_step(character, lst_blocks):
    current_x, current_y = character["position"]
    vx, vy  = character["velocity"]
    new_x = current_x + STEP * vx
    new_y = current_y + STEP * vy

    new_vx = vx + STEP * gravity_x
    new_vy = vy + STEP * gravity_y

    character["position"] = (new_x, new_y)
    character["velocity"] = (new_vx, new_vy)

    hit(character, lst_blocks)

def solver_simulate(character, lst_blocks):
    max_steps = 1000
    steps = 0

    while steps < max_steps:

        for _ in range(max_steps):
            old_pos = character["position"]
            solver_step(character, lst_blocks)
            if character["position"] == old_pos:
                character["velocity"] = (0, 0)
                return
        character["velocity"] = (-1, -1)  # for is_valid_state


def get_velocities():
    velocities = []
    step = 3
    for vx in range(-vmax, vmax + 1, step):
        for vy in range(-vmax, vmax + 1, step):
            velocities.append((vx, vy))
    return velocities

global_velocities = get_velocities()

def roundup_pos(position):
    return (int(position[0]) // POSITION_R, int(position[1]) // POSITION_R)

def is_valid_state(character, lst_blocks):
    x, y = character['position']
    vx, vy = character['velocity']

    # if the sheep is still moving
    if (vx, vy) != (0, 0):
        return False

    # if the sheep is stuck in a wall/block
    if collision(character, lst_blocks) is not None:
        return False

    # if SOMEHOW our sheep is out of bounds
    if x < 0 or y < 0 or x > width or y > height:
        return False

    return True

"""DFS solution"""

def dfs(start_character, lst_blocks, goal):
    visited = set()
    # now we're saving it in stack, not with recursion,
    # no mutation, only copies + no pop/append - branches out
    stack = [
        ({'position': start_character['position'], 'velocity': (0, 0)}, [])
    ]

    while stack:
        char_state, path = stack.pop()

        if victory(char_state, goal):
            return path

        pos = roundup_pos(char_state['position'])
        if pos in visited:
            continue
        visited.add(pos)

        for vx, vy in global_velocities:
            new_char = {
                'position': char_state['position'],
                'velocity': (vx, vy)
            }
            solver_simulate(new_char, lst_blocks)

            if not is_valid_state(new_char, lst_blocks):
                continue

            stack.append((new_char, path + [(vx, vy)]))

    return None
