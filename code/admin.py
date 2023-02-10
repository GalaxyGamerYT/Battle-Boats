import os
from colorama import *
from termcolor import *
from time import sleep

from settings import *
from support import linear, clearWindow

init(autoreset=True)

def deleteGameFiles():
    """
    Delete the game files from the save directory.
    """
    clearWindow()

    run = True

    while run:
        if os.path.exists(SAVEGAMEPATH):
            saves = os.listdir(SAVEGAMEPATH)
            while run:
                if saves:
                    print("====Game=Saves====")
                    for files in saves:
                        print("-",files)
                    print("==================")
                    print("Choose a game save to delete:")
                    game = input()
                    if linear(saves,game) != -1:
                        os.removedirs(os.path.join(SAVEGAMEPATH,game))
                        print(f"{game} has been deleted.")
                        sleep(1)
                        clearWindow()
                        run = False
                    else:
                        print(f"{Fore.RED}{game} Isn't a saved game.")
                else:
                    print(f"{Fore.RED} There isn't any saved games avaliable.")
                    run = False
        else:
            print(f"{Fore.RED}'{SAVEGAMEPATH}' doesn't exist.")
            run = False

if __name__ == "__main__":
    deleteGameFiles()
