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
        self.sunkShips = [0,0]
    
    def menu(self):
        """
        The main menu for the game. This is where the user can choose to either start a new game, resume a game, or quit.
        @param self - the object itself
        """
        while True:
            self.saves = listdir(SAVEGAMEPATH)
            #print("\033c")
            clearWindow()
            self.printTitle()
            if self.saves:
                print("=======MENU=======\nOption 1: Resume Game\nOption 2: New Game\nOption 3: Instructions\nOption 4: Quit\n==================\nChoose an option[1-4]:")
            else:
                print("=======MENU=======\n"+colored("Option 1: Resume Game","grey")+"\nOption 2: New Game\nOption 3: Instructions\nOption 4: Quit\n==================\nChoose an option[1-4]:")
            choice = input()
            try:
                choice = int(choice)
            except:
                print(f"{Fore.RED}{choice} Is not a valid option")
                sleep(1)
            else:
                if choice == 1:
                    if self.saves:
                        sleep(1)
                        self.resumeGame()
                    else:
                        print("There is no saved game\nStarting new game")
                        sleep(1)
                        self.newGame()
                elif choice == 2:
                    sleep(1)
                    self.newGame()
                elif choice == 3:
                    self.instructions()
                    sleep(1)
                elif choice == 4:
                    print("Quit")
                    exit()
                else:
                    print(f"{Fore.RED}{choice} Is not a valid option")
                    sleep(1)
    
    def printTitle(self):
        """
        Print the title of the program.
        """
        print(f"{Fore.CYAN} ______     ______     ______   ______   __         ______        ______     ______     ______     ______   ______     ")
        print(f"{Fore.CYAN}/\  == \   /\  __ \   /\__  _\ /\__  _\ /\ \       /\  ___\      /\  == \   /\  __ \   /\  __ \   /\__  _\ /\  ___\    ")
        print(f"{Fore.CYAN}\ \  __<   \ \  __ \  \/_/\ \/ \/_/\ \/ \ \ \____  \ \  __\      \ \  __<   \ \ \/\ \  \ \  __ \  \/_/\ \/ \ \___  \   ")
        print(f"{Fore.CYAN} \ \_____\  \ \_\ \_\    \ \_\    \ \_\  \ \_____\  \ \_____\     \ \_____\  \ \_____\  \ \_\ \_\    \ \_\  \/\_____\  ")
        print(f"{Fore.CYAN}  \/_____/   \/_/\/_/     \/_/     \/_/   \/_____/   \/_____/      \/_____/   \/_____/   \/_/\/_/     \/_/   \/_____/  ")
    
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
                self.sunkShips = data[3]
                self.run()
            sleep(1)
        sleep(1)
    
    def instructions(self):
        """
        Instructions for the game.
        @param self - the game object itself
        """
        clearWindow()
        if self.saves:
            print("You have a choice, you can either make a "+colored("new game","blue",attrs=["bold"])+" or "+colored("resume","blue",attrs=["bold"])+" a game.\n")
        else:
            print("You have to make a "+colored("new game","blue",attrs=["bold"])+".\n")
        print(colored("--New Game--","cyan",attrs=["bold"])+"\n")
        print(f"{Fore.MAGENTA}1.{Fore.RESET} Set a name for the game.\n{Fore.MAGENTA}2.{Fore.RESET} Set 5 ship coordinates. X=[A-H], Y=[1-8]\n{Fore.MAGENTA}3.{Fore.RESET} Your opponent sets their boats.\n{Fore.MAGENTA}4.{Fore.RESET} Then follow {Fore.CYAN}Main Game{Fore.RESET}.\n")
        if self.saves:
            print(colored("---Resume---","cyan",attrs=["bold"])+"\n")
            print(f"{Fore.MAGENTA}1.{Fore.RESET} Choose the saved game from a list.\n{Fore.MAGENTA}2.{Fore.RESET} Then follow {Fore.CYAN}Main Game{Fore.RESET}.\n")
        print(colored("-Main--Game-","cyan",attrs=["bold"])+"\n")
        print(f"{Fore.MAGENTA}1.{Fore.RESET} You select the coordinate that you want to shoot at.\n{Fore.MAGENTA}2.{Fore.RESET} Your opponent chooses their coordinates.\n{Fore.MAGENTA}3.{Fore.RESET} The first to sink all of the oppositions ships win.\n")
        input("Press ENTER to continue...")

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
                saveGame(self.ships, self.board, self.saveName, self.guesses, self.sunkShips)
                self.run()
            else:
                print(f"{Fore.RED}{self.saveName} Is already a saved game.")
                sleep(1)
                break

    def run(self):
        """
        Run the game.
        @param self - the game object itself.
        """
        game = Game(self.ships, self.board, self.guesses,self.saveName,self.sunkShips)
        game.run()

if __name__ == "__main__":
    """
    The main function that runs the entire program. It is the entry point for the program.
    """
    main = Main()
    main.menu()
