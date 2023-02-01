import pygame, sys
from os import listdir

from settings import *
from debug import debug
from game import Game
from support import drawText

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Battle Boats")
        pygame.display.set_icon(pygame.image.load("graphics/icon.ico"))

        self.clock = pygame.time.Clock()

        # Menu
        self.menu = Menu(self.clock)
        self.menuChoice = self.menu.run()
        
        self.game = Game()

    def run(self):
        """Running and handling the game."""
        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill("black")
            self.game.update(self.menuChoice)
            pygame.display.update()

class Menu:
    def __init__(self, clock):
        self.screen = pygame.display.get_surface()      
        self.running = True
        self.clock = clock
        self.saves = listdir(SAVEGAMEPATH)
        
        self.run()
    
    def drawMenu(self):
        """Draws the menu."""
        drawText("Press key for option:", x=WIDTH//2, y=(HEIGHT//2)-70)
        if self.saves:
            drawText("1: Resume Game", x=WIDTH//2, y=(HEIGHT//2)-30)
        else:
            drawText("1: Resume Game", x=WIDTH//2, y=(HEIGHT//2)-30, colour=NOSAVESOPTIONCOLOUR)
        drawText("2: New Game", x=WIDTH//2, y=(HEIGHT//2))
        drawText("3: Instructions", x=WIDTH//2, y=(HEIGHT//2)+30)
        drawText("4: Quit", x=WIDTH//2, y=(HEIGHT//2)+70)
    
    def run(self) -> int:
        """Running and handling the menu. Returns an integer of the choice."""
        while self.running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_1 and self.saves) or (event.key == pygame.K_KP1 and self.saves):
                        print(1)
                        self.running = False
                        return 1
                    elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        print(2)
                        self.running = False
                        return 2
                    elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                        print(3)
                        self.running = False
                        return 3
                    elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                        print(4)
                        self.running = False
                        pygame.quit()
                        sys.exit()
            self.drawMenu()
            pygame.display.update()

if __name__ == "__main__":
    main = Main()
    main.run()
