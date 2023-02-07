from os import listdir
from sys import exit
from time import sleep
from colorama import *
from termcolor import *

from settings import *
from support import *
from game import Game

init(autoreset=True)

class Main:
    def __init__(self):
        """
        Initialize the game state.
        """
        self.saves = []
        self.ships = NEWSHIPS
        self.board = NEWBOARD
        self.saveName = ""
        self.guesses = []

    def menu(self):
        """
        The menu for the game. It has the options to resume a game, start a new game, view the instructions, and quit.
        @param self - the game itself
        """
        while True:
            self.saves = listdir(SAVEGAMEPATH)
            if self.saves:
                print("=======MENU=======\nOption 1: Resume Game\nOption 2: New Game\nOption 3: Instructions\nOption 4: Quit\n==================\nChoose an option[1-4]:")
            else:
                print(f"=======MENU=======\n"+colored("Option 1: Resume Game","grey")+"\nOption 2: New Game\nOption 3: Instructions\nOption 4: Quit\n==================\nChoose an option[1-4]:")
            choice = input()
            try:
                choice = int(choice)
            except:
                print(f"{Fore.RED}{choice} Is not a valid option")
                sleep(.5)
            else:
                if choice == 1:
                    if self.saves:
                        sleep(.5)
                        self.resumeGame()
                    else:
                        print("There is no saved game\nStarting new game")
                        sleep(.5)
                        self.newGame()
                elif choice == 2:
                    sleep(.5)
                    self.newGame()
                elif choice == 3:
                    print("Instructions")
                    sleep(.5)
                elif choice == 4:
                    print("Quit")
                    exit()
                else:
                    print(f"{Fore.RED}{choice} Is not a valid option")
                    sleep(.5)

    def resumeGame(self):
        """
        Prints the saves and prompts the user to choose a save to load. Once the user has chosen a save, the game will resume.
        @param self - the game object itself
        """
        run = True
        while run:
            print("====Game=Saves====")
            for files in self.saves:
                print("-",files)
            print("==================")
            print("Choose a game save to load:")
            self.saveName = input()
            print(self.saves)
            if linear(self.saves,self.saveName) != -1:
                run = False
                data = loadGame(self.saveName)
                self.ships = data[0]
                self.board = data[1]
                self.guessess = data[2]
                self.run()
            sleep(.5)
        sleep(.5)
    
    def instructions(self):
        """Instructions"""
        pass

    def newGame(self):
        """
        New Game.
        """
        run = True
        while run:
            print("Choose the name of the game save:")
            self.saveName = input()
            if linear(self.saves,self.saveName) == -1:
                run = False
                self.ships[0] = generatePlayerCoords()
                self.ships[1] = generateEnemyCoords()
                saveGame(self.ships, self.board, self.saveName, self.guesses)
                print(self.ships)
                self.run()
            sleep(.5)
        sleep(.5)

    def run(self):
        """
        Run the game. This is the main function for the game. It will run until the game is over.
        @param self - the game object itself.
        """
        self.game = Game(self.ships, self.board, self.guesses)

if __name__ == "__main__":
    """
    The main function that runs the entire program. It is the entry point for the program.
    """
    main = Main()
    main.menu()
