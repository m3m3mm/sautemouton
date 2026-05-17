from const_values import *
from fltk import *
from physique import *
from info import goal
from time import sleep
from collections import deque


SOLVER_STEP = 0.3

def solver_step(character, lst_blocks):
    """moves the character for the solver"""
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
    """almost a same function as "step", but for the solver"""

    max_steps = 1000

    for _ in range(max_steps):
        old_pos = character["position"]
        solver_step(character, lst_blocks)
        if character["position"] == old_pos:
            character["velocity"] = (0, 0)
            return
    character["velocity"] = (-1, -1)  # for is_valid_state



def get_velocities():
    """gets a list of all possible velocities with a step of 2 to limit the amount of variations"""
    velocities = []
    step = 2
    for vx in range(int(-vmax), vmax + 1, step):
        for vy in range(-vmax, vmax + 1, step):
            if math.sqrt(vx ** 2 + vy ** 2) <= vmax:
                velocities.append((vx, vy))
    return velocities

global_velocities = get_velocities()

def roundup_pos(position):
    """rounds up the position due to unlimited amount of possible positions"""
    return (int(position[0]) // POSITION_R, int(position[1]) // POSITION_R)

def is_grounded(character, lst_blocks):
    """checks if the character is on the floor if the velocity is 0.
    if not - tells us that the character is either stuck in the air or stuck to a wall from the side"""

    x, y = character['position']
    below = {'position': (x, y + 1), 'velocity': (0, 0)}
    return collision(below, lst_blocks) is not None


def is_valid_state(character, lst_blocks):
    """tells us if the character is in a valid position (not outside the window given, stuck or smth)"""

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


def dfs(start_character, lst_blocks, goal):
    """Iterative DFS pathfinder. Returns list of (vx, vy) moves to reach goal, or None."""
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



def bfs(start_character, lst_blocks, goal):
    """BFS - only change is deque instead of list"""
    visited = set()
    # очередь вместо стека - единственное отличие от DFS
    queue = deque([
        ({'position': start_character['position'], 'velocity': (0, 0)}, [])
    ])

    while queue:
        char_state, path = queue.popleft()  # popleft, а не pop

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

            queue.append((new_char, path + [(vx, vy)]))

    return None