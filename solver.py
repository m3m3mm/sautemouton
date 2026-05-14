from const_values import *
from fltk import *
from physique import *
from info import goal
from time import sleep

SOLVER_STEP = 0.3

def solver_step(character, lst_blocks):
    current_x, current_y = character["position"]
    vx, vy  = character["velocity"]
    new_x = current_x + SOLVER_STEP * vx
    new_y = current_y + SOLVER_STEP * vy

    new_vx = vx + SOLVER_STEP * gravity_x
    new_vy = vy + SOLVER_STEP * gravity_y

    character["position"] = (new_x, new_y)
    character["velocity"] = (new_vx, new_vy)

    hit(character, lst_blocks)

def solver_simulate(character, lst_blocks):
    max_steps = 1000

    for _ in range(max_steps):
        old_pos = character["position"]
        solver_step(character, lst_blocks)
        if character["position"] == old_pos:
            character["velocity"] = (0, 0)
            return
    character["velocity"] = (-1, -1)  # for is_valid_state



def get_velocities():
    velocities = []
    step = 2
    for vx in range(int(-vmax), vmax + 1, step):
        for vy in range(-vmax, vmax + 1, step):
            velocities.append((vx, vy))
    return velocities

global_velocities = get_velocities()

def roundup_pos(position):
    return (int(position[0]) // POSITION_R, int(position[1]) // POSITION_R)

def is_grounded(character, lst_blocks):

    x, y = character['position']
    below = {'position': (x, y + 1), 'velocity': (0, 0)}
    return collision(below, lst_blocks) is not None


def is_valid_state(character, lst_blocks):
    vx, vy = character['velocity']
    if (vx, vy) != (0, 0):
        return False

    if collision(character, lst_blocks) is not None:
        return False

    x, y = character['position']
    if x < 0 or y < 0 or x > width or y > height:
        return False

    # if the sheep is not on ground, but stuck in the air (glued to a wall or smth)
    if not is_grounded(character, lst_blocks):
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
