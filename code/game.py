import pygame
from settings import *
from support import *
from intro import Intro

class Game:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.ships = None
        
        self.intro = Intro()
    
    def update(self, menuChoice):
        """Updates the game."""
        if menuChoice == 1:
            self.loadGame()
        elif menuChoice == 2:
            self.newGame()
        elif menuChoice == 3:
            self.intro()
    
    def loadGame(self):
        """Loads a saved game."""
        pass
    
    def newGame(self):
        """Creates a new game."""
        self.ships = SHIPS
