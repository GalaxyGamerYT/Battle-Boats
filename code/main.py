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
    """
    The main function of the game. This function will run the game.
    """
    def __init__(self):
        """
        Initialize the game. Create the save folder and the game objects.
        """
        folderCheck(SAVEGAMEPATH)
        self.saves = []
        self.ships = NEWSHIPS
        self.board = NEWBOARD
        self.saveName = ""
        self.guesses = [[],[]]

    def menu(self):
        """
        The main menu for the game. This is where the user can choose to either start a new game, resume a game, or quit.
        @param self - the object itself
        """
        while True:
            self.saves = listdir(SAVEGAMEPATH)
            #print("\033c")
            clearWindow()
            if self.saves:
                print("=======MENU=======\nOption 1: Resume Game\nOption 2: New Game\nOption 3: Instructions\nOption 4: Quit\n==================\nChoose an option[1-4]:")
            else:
                print("=======MENU=======\n"+colored("Option 1: Resume Game","grey")+"\nOption 2: New Game\nOption 3: Instructions\nOption 4: Quit\n==================\nChoose an option[1-4]:")
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
        Prints the saves to the screen and allows the user to choose one to load.
        @returns the name of the save to load
        """
        run = True
        while run:
            #print("\033c")
            clearWindow()
            print("====Game=Saves====")
            for files in self.saves:
                print("-",files)
            print("==================")
            print("Choose a game save to load:")
            name = input()
            if linear(self.saves,name) != -1:
                self.saveName = name
                run = False
                data = loadGame(self.saveName)
                self.ships = data[0]
                self.board = data[1]
                self.guessess = data[2]
                self.run()
            sleep(.5)
        sleep(.5)
    
    def instructions(self):
        """
        Instructions for the user to use the program.
        @param self - the object itself, used to access the class's attributes.
        """
        pass

    def newGame(self):
        """
        This function is used to create a new game. It will ask the user for a name for the game, and if the name is not already in use, it will create a new game.
        @param self - the game object itself
        @returns nothing
        """
        run = True
        while run:
            #print("\033c")
            clearWindow()
            print("Choose the name of the game save:")
            self.saveName = input()
            if linear(self.saves,self.saveName) == -1:
                run = False
                self.ships[0] = generatePlayerCoords(self.board[0])
                self.ships[1] = generateEnemyCoords()
                saveGame(self.ships, self.board, self.saveName, self.guesses)
                print(self.ships)
                self.run()
            else:
                print(f"{Fore.RED}{self.saveName} Is already a saved game.")
                sleep(.5)
                break

    def run(self):
        """
        Run the game.
        @param self - the game object itself.
        """
        game = Game(self.ships, self.board, self.guesses,self.saveName)
        game.run()

if __name__ == "__main__":
    """
    The main function that runs the entire program. It is the entry point for the program.
    """
    main = Main()
    main.menu()
