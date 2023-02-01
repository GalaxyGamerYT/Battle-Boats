import pygame
pygame.font.init()

WIDTH, HEIGHT = 1280, 720
FPS = 60

SAVEGAMEPATH = "saves"

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Menu Settings
FONT = pygame.font.Font("joystix.ttf",30)
OPTIONDEFAULTCOLOUR = (255, 255, 255)
NOSAVESOPTIONCOLOUR = (184, 184, 184)

GAMEARRAY = [
    [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1)],
    [(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(8,2)],
    [(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(7,3),(8,3)],
    [(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4),(8,4)],
    [(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(7,5),(8,5)],
    [(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6),(8,6)],
    [(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),(8,7)],
    [(1,8),(2,8),(3,8),(4,8),(5,8),(6,8),(7,8),(8,8)]
]

SHIPS = [[],[]]
