from const_values import WIDTH, HEIGHT
from info import *
from fltk import *



def draw_blocks(lst_blocks):
    """draws blocks"""
    for block in lst_blocks:
        x1, y1, x2, y2 = block
        #rectangle(x1, y1, x2, y2, remplissage="red")
        image(x1, y1, "design/block.png", largeur = x2 - x1,
              hauteur = y2 - y1, ancrage="nw")


def draw_final_object(goal):
    """draws final object that character needs to reach"""
    x1, y1, x2, y2 = goal
    #rectangle(x1, y1, x2, y2, remplissage="white")
    image(x1, y1, 'design/chest.png', largeur = x2 - x1, hauteur = y2 - y1, ancrage="nw")



def draw_character(character):
    """draws character"""
    x, y = character['position']
    cercle(x + WIDTH / 2, y + HEIGHT / 2, WIDTH / 2, remplissage="red", tag="mouton")


def draw_victory_menu(height, width):
    """draws victory menu"""
    rectangle(100, 130, width-100, height-130, remplissage="red", tag="victory")
    texte(120, 195, "You won!", taille=10, tag="victory")


def create_design():
    """creates design"""
    image(0, 0, "design/background.ppm", ancrage="nw")

def draw_main_menu(width, height):
    """draws main menu"""
    image(width / 2, height / 2,
          "design/main_menu.png",
          largeur=width,
          hauteur=height,
          ancrage="center", tag="main_menu")
    #rectangle(50, 170, 190, 220, remplissage="red")
    image(width/7, height/2 - 30, 'design/startgame.png', largeur=140, hauteur=50 , ancrage="nw", tag="start")
    image(width/7, height/2 + 40, 'design/option.png', largeur=140, hauteur=50 , ancrage="nw", tag="levels")

    while True:

        ev = attend_ev()

        if type_ev(ev) == "Quitte":
            break
        if type_ev(ev) == 'ClicGauche':
            click = (abscisse(ev), ordonnee(ev))
            if (width/7) <= click[0] <= (width/7 + 140):
                if (height/2-30) <= click[1] <= (height/2 + 20):
                    print('started isb true')
                    started = True
                    selected_level = 'niveau_info.txt'
                    return started, selected_level
                elif (height/2+40) <= click[1] <= (height/2 + 90):
                    print('nado sdelat levels')
                    efface('start')
                    efface('levels')
                    rectangle(67, 198, 177, 240, remplissage='red')
                    rectangle(67, 249, 177, 290, remplissage='red')
                    image(width/7, height/2 - 30, 'design/levels.png', largeur=140, hauteur=160 , ancrage="nw", tag="levels")

                    ev2 = attend_ev()
                    if type_ev(ev2) == 'ClicGauche':
                        click = (abscisse(ev2), ordonnee(ev2))
                        if 67 <= click[0] <= 177:
                            if 198 <= click[1] <= 240:
                                print('first level')
                                started = True
                                selected_level = 'niveau_info.txt'
                                return started, selected_level
                            else:
                                print('second level')
                                started = True
                                selected_level = 'second_level.txt'
                                return started, selected_level







