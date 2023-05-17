import sys
import pygame
from pygame import *
import os

# Definir los estados
MENU = 0
SELECT = 1
SELECT1 = 2
SELECT2 = 3
SELECT3 = 4
SELECT4 = 5
SELECT5 = 6
SELECT6 = 7
COMBATE = 8
COMBATE1 = 9

# Constantes del juego
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 728
SONIDO_DIR = "sonidos"
IMG_DIR = "imagenes"

# ------------------------------
# Cargar imágenes y sonidos
# ------------------------------
def load_image(nombre, dir_imagen, alpha=False):
    # Encontramos la ruta completa de la imagen
    ruta = os.path.join(dir_imagen, nombre)
    try:
        image = pygame.image.load(ruta)
    except:
        print("Error, no se puede cargar la imagen: " + ruta)
        sys.exit(1)
    # Comprobar si la imagen tiene "canal alpha" (como los png)
    if alpha is True:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image


def load_sound(nombre, dir_sonido):
    ruta = os.path.join(dir_sonido, nombre)
    # Intentar cargar el sonido
    try:
        sonido = pygame.mixer.Sound(ruta)
    except (pygame.error) as message:
        print("No se pudo cargar el sonido:", ruta)
        sonido = None
    return sonido
# ------------------------------
# Funciones para cada estado
# ------------------------------

def show_menu(screen):
    sonido_titulo = load_sound('Titulo.ogg', SONIDO_DIR)
    sonido_titulo.play()
    inicio = load_image("Inicio.png", IMG_DIR, alpha=False).convert()
    screen.blit(inicio, (0, 0))
    myFont = font.SysFont("Stencil", 30)
    iniciar = Rect(512-75, 600, 150, 40)
    draw.rect(screen, (0, 0, 0), iniciar, 0)
    texto = myFont.render("INICIAR", True, (255, 255, 0))
    screen.blit(texto, (512-60, 600))
    pygame.display.flip()
    return sonido_titulo

def play_game(screen):
    select = load_image("fondoselect.PNG", IMG_DIR, alpha=False).convert()
    screen.blit(select, (0, 0))
    prim = load_image("052_2.png", IMG_DIR, alpha=True).convert_alpha()
    screen.blit(prim, (120, 180))
    seg = load_image("088_1.png", IMG_DIR, alpha=True).convert_alpha()
    screen.blit(seg, (350, 190))
    ter = load_image("080s_2.png", IMG_DIR, alpha=True).convert_alpha()
    screen.blit(ter, (135, 365))
    cuart = load_image("122_1.png", IMG_DIR, alpha=True).convert_alpha()
    screen.blit(cuart, (350, 350))
    quint = load_image("131_1.png", IMG_DIR, alpha=True).convert_alpha()
    screen.blit(quint, (145, 550))
    sex = load_image("150s_1.png", IMG_DIR, alpha=True).convert_alpha()
    screen.blit(sex, (365, 535))
    pygame.display.flip()


def primera_select_meowth(screen):
    meowth = load_image("meowth.png", IMG_DIR, alpha=True).convert_alpha()
    screen.blit(meowth, (575, 153))
    pygame.display.flip()

def primera_select_grimer(screen):
    grimer = load_image("grimer.png", IMG_DIR, alpha=True).convert_alpha()
    screen.blit(grimer, (550, 153))
    pygame.display.flip()

def segunda_select_slowbro(screen):
    slowbro = load_image("slowbro.png", IMG_DIR, alpha=True).convert_alpha()
    screen.blit(slowbro, (570, 332))
    pygame.display.flip()

def segunda_select_mrmime(screen):
    mrmime = load_image("mrmime.png", IMG_DIR, alpha=True).convert_alpha()
    screen.blit(mrmime, (530, 338))
    pygame.display.flip()

def tercera_select_lapras(screen):
    lapras = load_image("lapras.png", IMG_DIR, alpha=True).convert_alpha()
    screen.blit(lapras, (530, 508))
    pygame.display.flip()

def tercera_select_mewtwo(screen):
    mewtwo = load_image("mewtwo.png", IMG_DIR, alpha=True).convert_alpha()
    screen.blit(mewtwo, (590, 522))
    pygame.display.flip()

def combate(screen):
    fondo = load_image("fondocombate1.png", IMG_DIR, alpha=True).convert_alpha()
    screen.blit(fondo, (0, 0))
    disco1 = load_image("disco.png", IMG_DIR, alpha=True).convert_alpha()
    screen.blit(disco1, (145, 380))
    screen.blit(disco1, (600, 155))
    pok1 = load_image("meocomb.png", IMG_DIR, alpha=True).convert_alpha()
    screen.blit(pok1, (75, 150))
    pok2 = load_image("grimercomb.png", IMG_DIR, alpha=True).convert_alpha()
    screen.blit(pok2, (520, 0))
    pygame.display.flip()

def combate1(screen):
    fondo = load_image("fondocombatelucha.png", IMG_DIR, alpha=True).convert_alpha()
    screen.blit(fondo, (0, 0))
    disco1 = load_image("disco.png", IMG_DIR, alpha=True).convert_alpha()
    screen.blit(disco1, (145, 380))
    screen.blit(disco1, (600, 155))
    pok1 = load_image("meocomb.png", IMG_DIR, alpha=True).convert_alpha()
    screen.blit(pok1, (75, 150))
    pok2 = load_image("grimercomb.png", IMG_DIR, alpha=True).convert_alpha()
    screen.blit(pok2, (520, 0))
    pygame.display.flip()

# Función principal para controlar el estado
def game_loop():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Pokemon')
    state = MENU
    while True:
        for event in pygame.event.get():
            if state == MENU:
                algo = show_menu(screen)
                iniciar = Rect(512 - 75, 600, 150, 40)
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if iniciar.collidepoint(mouse.get_pos()):
                        state = SELECT
                        algo.stop()

            if state == SELECT:
                play_game(screen)
                selmeowth = Rect(145-50, 205-50, 120, 120)
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if selmeowth.collidepoint(mouse.get_pos()):
                        state = SELECT1
                        primera_select_meowth(screen)
                selgrimer = Rect(375, 205, 120, 120)
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if selgrimer.collidepoint(mouse.get_pos()):
                        state = SELECT2
                        primera_select_grimer(screen)

            if state == SELECT1 or state == SELECT2:
                selslowbro = Rect(145, 375, 120,120)
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if selslowbro.collidepoint(mouse.get_pos()):
                        state = SELECT3
                        segunda_select_slowbro(screen)
                selmrmime = Rect(325, 325, 120, 120)
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if selmrmime.collidepoint(mouse.get_pos()):
                        state = SELECT4
                        segunda_select_mrmime(screen)

            if state == SELECT3 or state == SELECT4:
                sellapras = Rect(145, 550, 120, 120)
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if sellapras.collidepoint(mouse.get_pos()):
                        state = SELECT5
                        tercera_select_lapras(screen)
                selmewtwo = Rect(375, 550, 120, 120)
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if selmewtwo.collidepoint(mouse.get_pos()):
                        state = SELECT6
                        tercera_select_mewtwo(screen)

            if state == SELECT5 or state == SELECT6:
                avance = Rect(874, 0, 150, 150)
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if avance.collidepoint(mouse.get_pos()):
                        state = COMBATE
                        combate(screen)

            if state == COMBATE:
                lucha = Rect(512, 546, 258, 80)
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if lucha.collidepoint(mouse.get_pos()):
                        state = COMBATE1
                        combate1(screen)

            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == '__main__':
    game_loop()