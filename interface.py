from fltk import *
from affichage import *
from info import *
from physique import *

def game(character, lst_blocks): #TODO: add "goal" later
    """loop of the game which uses all the functions"""
    click = None
    draw_character(character)
    draw_blocks(lst_blocks)
    #draw_final_object(goal)
    while True:
        ev = attend_ev()

        # added game end on clicking "X"
        if type_ev(ev) == "Quitte":
            break

        if type_ev(ev) == 'ClicGauche':
            x = abscisse(ev)
            y = ordonnee(ev)
            click = (x, y)
            efface("vector")

        if type_ev(ev) == 'ClicDroit':
            if click is not None:
                vx, vy = click_to_velocity(character, click)
                character["velocity"] = (vx, vy)
                efface("vector")
                simulate(character, lst_blocks) # without this line mouton/barashek won't move
                click = None
                if victory(character,goal):
                    print("You won!") #placeholder for win message

        efface('mouton')
        draw_character(character)

        if click is not None:
            ligne(character['position'][0], character['position'][1], x, y,epaisseur = 2, tag = "vector")
        mise_a_jour()

