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
    image(x + WIDTH / 2, y + HEIGHT / 2, "design/wooly.png", largeur = 30, hauteur = 30, ancrage="center", tag="mouton")


def draw_victory_menu(height, width):
    """draws victory menu"""
    efface_tout()
    efface('mouton')
    image(0, 0, 'design/winmenu.png', largeur = 345, hauteur = 400, ancrage='nw', tag='victory')

    # button Main menu
    m_x1, m_y1, m_x2, m_y2 = 85, 290, 260, 330
    rectangle(m_x1, m_y1, m_x2, m_y2,
              remplissage="#6b2737", couleur="#e07a5f",
              epaisseur=2, tag="victory")
    texte((m_x1 + m_x2) // 2, (m_y1 + m_y2) // 2,
          "Main Menu", couleur="white", taille=13,
          ancrage="center", tag="victory")

    # button Play Again
    r_x1, r_y1, r_x2, r_y2 = 85, 340, 260, 380
    rectangle(r_x1, r_y1, r_x2, r_y2,
              remplissage="#2d6a4f", couleur="#52b788",
              epaisseur=2, tag="victory")
    texte((r_x1 + r_x2) // 2, (r_y1 + r_y2) // 2,
          "Play Again", couleur="white", taille=13,
          ancrage="center", tag="victory")

    return (m_x1, m_y1, m_x2, m_y2), (r_x1, r_y1, r_x2, r_y2)


def draw_pause_menu():
    """draws pause overlay with resume and main menu buttons, returns their rects"""
    image(172, 200,
              "design/pause_menu.png",
              largeur=250,
              hauteur=250,
              ancrage="center",
              tag="pause_overlay")

    r_x1, r_y1, r_x2, r_y2 = 127, 176, 220, 212
    m_x1, m_y1, m_x2, m_y2 = 127, 220, 220, 255

    return (r_x1, r_y1, r_x2, r_y2), (m_x1, m_y1, m_x2, m_y2)


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

    #cercle(310, 370, 15, couleur='red')
    image(310, 370, 'design/hint.png', largeur=33, hauteur=33, ancrage='center', tag='hints')

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
                    efface('start')
                    efface('levels')
                    #rectangle(67, 198, 177, 240, remplissage='red')
                    #rectangle(67, 249, 177, 290, remplissage='red')
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
            elif 295 <= click[0] <= 322:
                if 355 <= click[1] <= 385:
                    image(60, 60,'design/controls.png',largeur = 224, hauteur = 280, ancrage='nw', tag='controls')
                    event_hint = attend_ev()
                    if type_ev(event_hint) == 'ClicGauche':
                        click_hint = (abscisse(event_hint), ordonnee(event_hint))
                        if 295 <= click_hint[0] <= 322:
                            if 355 <= click_hint[1] <= 385:
                                efface('controls')
