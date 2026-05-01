from affichage import *
from physique import *
from const_values import *

def game(character, lst_blocks, goal):
    """loop of the game which uses all the functions"""
    click = None

    history = [character["position"]] # for backspace functionality we need the history of our positions

    create_design()
    draw_character(character)
    draw_blocks(lst_blocks)
    draw_final_object(goal)
    while True:
        ev = attend_ev()

        # added game end on clicking "X"
        if type_ev(ev) == "Quitte":
            break

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
                simulate(character, lst_blocks) # without this line mouton/barashek won't move
                history.append(character["position"]) # saving positions

                click = None
                if victory(character,goal):
                    draw_victory_menu(height, width)
                    print("You won!") #placeholder for win message

        if type_ev(ev) == 'Touche':
            if touche(ev) == 'BackSpace':
                if len(history) > 1:  # we check if is possible to go back
                    history.pop()
                    character["position"] = history[-1]
                    character["velocity"] = (0, 0)
                    efface("shadow_of_step")
                    efface("mouton")
                    draw_character(character)

        efface('mouton')
        draw_character(character)

        if click is not None:
            cx, cy = character['position'][0] + WIDTH / 2, character['position'][1] + HEIGHT / 2
            dx = x - cx
            dy = y - cy
            dist = math.sqrt(dx ** 2 + dy ** 2)

            if dist > vmax:
                dx = dx / dist * vmax * 3
                dy = dy / dist * vmax * 3

            ex, ey = cx + dx, cy + dy  # endpoint стрелки

            ligne(cx, cy, ex, ey, epaisseur=4, tag="vector", couleur="white")
            fleche(cx, cy, ex, ey, epaisseur=3, tag="vector", couleur="white")

        mise_a_jour()

