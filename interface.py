import pygame.mixer

from affichage import *
from physique import *
from const_values import *
from solver import *


def _in_rect(x, y, rect):
    """returns True if click (x, y) is inside rect (x1, y1, x2, y2)"""
    x1, y1, x2, y2 = rect
    return x1 <= x <= x2 and y1 <= y <= y2


def _redraw_game(character, lst_blocks, goal):
    """redraws the full game screen from scratch"""
    efface_tout()
    create_design()
    draw_blocks(lst_blocks)
    draw_final_object(goal)
    draw_character(character)


def _handle_pause(character, lst_blocks, goal):
    """shows pause menu and waits for player choice, returns 'resume', 'menu' or 'quit'"""
    resume_rect, menu_rect = draw_pause_menu(width, height)
    mise_a_jour()

    while True:
        ev = attend_ev()

        if type_ev(ev) == "Quitte":
            return "quit"

        # pressing Esc again resumes the game
        if type_ev(ev) == 'Touche' and touche(ev) == 'Escape':
            efface("pause_overlay")
            return "resume"

        if type_ev(ev) == 'ClicGauche':
            x, y = abscisse(ev), ordonnee(ev)
            if _in_rect(x, y, resume_rect):
                efface("pause_overlay")
                return "resume"
            if _in_rect(x, y, menu_rect):
                return "menu"

        mise_a_jour()

def game(character, lst_blocks, goal):
    """loop of the game which uses all the functions"""
    click = None
    game_state = "playing"
    history = [character["position"]]  # for backspace functionality we need the history of our positions
    victory_btn_rect = None

    create_design()
    draw_character(character)
    draw_blocks(lst_blocks)
    draw_final_object(goal)

    while True:
        ev = attend_ev()

        # added game end on clicking "X"
        if type_ev(ev) == "Quitte":
            break

        # Esc opens the pause menu during gameplay
        if type_ev(ev) == 'Touche' and touche(ev) == 'Escape':
            if game_state == "playing":
                result = _handle_pause(character, lst_blocks, goal)
                if result == "quit":
                    return "quit"
                if result == "menu":
                    return "menu"
                # resume: redraw the game without the pause overlay
                _redraw_game(character, lst_blocks, goal)
                game_state = "playing"
            continue

        # on the victory screen only the main menu button is active
        if game_state == "victory":
            if type_ev(ev) == 'ClicGauche' and victory_btn_rect is not None:
                x, y = abscisse(ev), ordonnee(ev)
                menu_rect, replay_rect = victory_btn_rect
                if _in_rect(x, y, menu_rect):
                    return "menu"
                if _in_rect(x, y, replay_rect):
                    return "replay"
            mise_a_jour()
            continue

        if game_state == "playing":
            if type_ev(ev) == 'ClicGauche':
                efface("shadow_of_step")
                x = abscisse(ev)
                y = ordonnee(ev)
                click = (x, y)
                efface("vector")

            if type_ev(ev) == 'ClicDroit':
                jump = pygame.mixer.Sound('jump.mp3')
                jump.set_volume(0.3)
                jump.play(0)
                if click is not None:
                    vx, vy = click_to_velocity(character, click)
                    character["velocity"] = (vx, vy)
                    efface("vector")
                    simulate(character, lst_blocks)  # without this line mouton/barashek won't move
                    history.append(character["position"])  # saving positions

                    click = None
                    if victory(character, goal):

                        pygame.mixer.music.stop()
                        pygame.mixer.music.load('Wooly Victory.mp3')
                        pygame.mixer.music.set_volume(0.3)
                        pygame.mixer.music.play(-1)

                        menu_rect, replay_rect = draw_victory_menu(height, width)
                        victory_btn_rect = (menu_rect, replay_rect)
                        game_state = "victory"



            if type_ev(ev) == 'Touche':
                if touche(ev) == 'BackSpace':
                    if len(history) > 1:  # we check if is possible to go back
                        history.pop()
                        character["position"] = history[-1]
                        character["velocity"] = (0, 0)
                        efface("shadow_of_step")
                        efface("mouton")
                        draw_character(character)

                if touche(ev) == 'l':
                    saved_pos = character["position"]
                    saved_v = character["velocity"]

                    print("Solving with DFS ...")

                    dolly = {"position": saved_pos, "velocity": (0, 0)}

                    path = dfs(dolly, lst_blocks, goal)

                    character["position"] = saved_pos
                    character["velocity"] = saved_v

                    if path is None:
                        print("Solution not found!")

                    else:
                        print("Solution found")

                        efface("solver_path")
                        efface("solver_character")

                        dolly = {"position": saved_pos,"velocity": (0, 0)}

                        for vx, vy in path:
                            dolly["velocity"] = (vx, vy)

                            while True:
                                old_pos = dolly["position"]

                                solver_step(dolly, lst_blocks)

                                x, y = dolly["position"]

                                cercle(x + WIDTH / 2,y + HEIGHT / 2, 3, couleur="yellow", remplissage="yellow", tag="solver_path")

                                efface("solver_character")

                                cercle(x + WIDTH / 2, y + HEIGHT / 2, WIDTH / 2, couleur="orange", remplissage="orange", tag="solver_character")

                                mise_a_jour()

                                sleep(0.01)

                                if dolly["position"] == old_pos:
                                    break
                if touche(ev) == 'k':
                    saved_pos = character["position"]
                    saved_v = character["velocity"]

                    print("Solving with BFS ...")

                    dolly = {"position": saved_pos, "velocity": (0, 0)}

                    path = bfs(dolly, lst_blocks, goal)

                    character["position"] = saved_pos
                    character["velocity"] = saved_v

                    if path is None:
                        print("Solution not found!")

                    else:
                        print("Solution found")

                        efface("solver_path")
                        efface("solver_character")

                        dolly = {"position": saved_pos,"velocity": (0, 0)}

                        for vx, vy in path:
                            dolly["velocity"] = (vx, vy)

                            while True:
                                old_pos = dolly["position"]

                                solver_step(dolly, lst_blocks)

                                x, y = dolly["position"]

                                cercle(x + WIDTH / 2,y + HEIGHT / 2, 3, couleur="yellow", remplissage="yellow", tag="solver_path")

                                efface("solver_character")

                                mise_a_jour()

                                sleep(0.01)

                                if dolly["position"] == old_pos:
                                    break
        efface('mouton')
        draw_character(character)

        if click is not None:
            cx = character['position'][0] + WIDTH / 2
            cy = character['position'][1] + HEIGHT / 2
            dx = click[0] - cx
            dy = click[1] - cy
            dist = math.sqrt(dx ** 2 + dy ** 2)

            if dist > 0:
                visual_len = min(dist, MAX_ARROW_PX)
                ex = cx + (dx / dist) * visual_len
                ey = cy + (dy / dist) * visual_len
                ligne(cx, cy, ex, ey, epaisseur=4, tag="vector", couleur="white")
                fleche(cx, cy, ex, ey, epaisseur=3, tag="vector", couleur="white")

        mise_a_jour()

