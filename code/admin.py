import os
from colorama import *
from termcolor import *

from settings import *
from support import linear

init(autoreset=True)

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
                    # File paths
                    playerShipsPath = os.path.join(SAVEGAMEPATH,game,"playerShips.csv")
                    enemyShipsPath = os.path.join(SAVEGAMEPATH,game,"enemyShips.csv")
                    playerBoardPath = os.path.join(SAVEGAMEPATH,game,"playerBoard.csv")
                    enemyBoardPath = os.path.join(SAVEGAMEPATH,game,"enemyBoardGame.csv")
                    playerGuessessPath = os.path.join(SAVEGAMEPATH,game,"playerGuessess.csv")
                    enemyGuessessPath = os.path.join(SAVEGAMEPATH,game,"enemyGuessess.csv")
                    
                    os.remove(playerShipsPath)
                    os.remove(enemyShipsPath)
                    os.remove(playerBoardPath)
                    os.remove(enemyBoardPath)
                    os.remove(playerGuessessPath)
                    os.remove(enemyGuessessPath)
                    os.removedirs(os.path.join(SAVEGAMEPATH,game))
                    run = False
                else:
                    print(f"{Fore.RED}{game} Isn't a saved game.")
            else:
                print(f"{Fore.RED} There isn't any saved games avaliable.")
                run = False
    else:
        print(f"{Fore.RED}'{SAVEGAMEPATH}' doesn't exist.")
        run = False
