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
        old_pos = character["position"]

        solver_step(character, lst_blocks)

        if character["position"] == old_pos:
            return

        steps += 1

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

"""DFS solution"""

def dfs(character, lst_blocks, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    if victory(character, goal):
        return path[:] # returning the path if won

    pos = roundup_pos(character["position"])
    if pos in visited:
        return None
    visited.add(pos)

    for vx, vy in global_velocities:
        saved_pos = character["position"]
        saved_v =  character["velocity"]

        character["velocity"] = (vx,vy)
        solver_simulate(character, lst_blocks)

        path.append((vx,vy))
        result = dfs(character,lst_blocks,goal,visited,path)
        if result is not None:
            return result
        path.pop()

        character["position"] = saved_pos
        character["velocity"] = saved_v

    return None
