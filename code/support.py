import pygame

from settings import *

def drawText(text: str, x: int = WIDTH//2, y: int = HEIGHT//2, font = FONT, colour: tuple = OPTIONDEFAULTCOLOUR):
        """Draws text to the screen"""
        screen = pygame.display.get_surface()
        textSurf = font.render(text, True, colour)
        textRect = textSurf.get_rect(center = (x,y))
        screen.blit(textSurf,textRect)

def generateEnemyCoords() -> list:
        """Generates the coords for the enemy's ship."""
        pass

def generatePlayerCoords() -> list:
        """Generates the coords for the player's ship."""
        pass

def linear(arr: list, x) -> int:
        """Searches the array for the value of 'x'"""
        pass
