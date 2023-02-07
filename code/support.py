import os, csv
from random import randint
from colorama import *

from settings import *

def generateEnemyCoords() -> list:
    """
    Generates the coords for the enemy's ships.
    @return The coords for the enemy's ships.
    """
    shipsCreated = 0
    ships = []
    while shipsCreated <= SHIPAMOUNT:
        pos = (randint(0,GRIDSIZE-1),randint(0,GRIDSIZE-1))
        if linear(ships, pos) == -1:
            ships.append(pos)
            shipsCreated += 1
    return ships

def linear(arr: list, x) -> int:
    """
    Searches the array for the value of 'x'.
    @param arr - the array to search for 'x' in.
    @param x - the value to search for in the array.
    @return the index of 'x' in the array.
    """
    for index,i in enumerate(arr):
        if i == x:
            return index
    return -1

def extendedLinear(arr: list, x) -> int:
    """
    Searches the array for the value of 'x' in a 2D array.
    @param arr - the array to search for 'x' in.
    @param x - the value to search for in the array.
    @return the index of the value 'x' in the array.
    """
    for a in arr:
        for index, b in enumerate(a):
            if b == x:
                return index
    return -1

def folderCheck(path: str) -> list:
    """
    Check if a folder exists. If not, create it.
    @param path - the path to the folder we are checking for.
    @returns the contents of the folder.
    """
    if not os.path.exists(path):
        os.mkdir(path)
    content = os.listdir(path)
    return content

def generatePlayerCoords() -> list:
    """
    Generate the coordinates for the players ships.
    @returns the list of coordinates for the players ships.
    """
    shipsCreated = 0
    ships = []
    while shipsCreated <= SHIPAMOUNT:
        posX = input("Input the x coordinate[1-8]: ")
        try:
            int(posX)
        except:
            print(f"{Fore.RED}{posX} Isn't a valid x coordinate.")
        else:
            posX = int(posX)-1
            if posX >=0 and posX <= GRIDSIZE-1:
                posY = input("Input the y corrdinate[1-8]: ")
                try:
                    int(posY)
                except:
                    print(f"{Fore.RED}{posY} Isn't a valid y coordinate.")
                else:
                    posY = int(posY)-1
                    if posY >= 0 and posY <= GRIDSIZE-1:
                        pos = (posX,posY)
                        print(pos)
                        if linear(ships, pos) == -1:
                            ships.append(pos)
                            shipsCreated += 1
                        else:
                            print(f"{Fore.RED}{pos} has already been used.")
                    else:
                        print(f"{Fore.RED}{posY} Isn't a valid y coordinate.")
            else:
                print(f"{Fore.RED}{posX} Isn't a valid x coordinate.")
    return ships

def saveGame(ships: list, board: list, name: str, guesses: list) -> None:
    """
    Saves the game files.
    @param ships - the ships of the player and enemy ships.
    @param board - the board of the game.
    @param name - the name of the game.
    @param guesses - the guesses of the player.
    """
    # Checks for game folder and creates it.
    folderCheck(os.path.join(SAVEGAMEPATH,name))
    
    # File paths
    playerShipsPath = os.path.join(SAVEGAMEPATH,name,"playerShips.csv")
    enemyShipsPath = os.path.join(SAVEGAMEPATH,name,"enemyShips.csv")
    boardPath = os.path.join(SAVEGAMEPATH,name,"board.csv")
    miscPath = os.path.join(SAVEGAMEPATH,name,"misc.csv")
    
    # Player Ships file
    with open(playerShipsPath,"w",newline='') as f:
        csvwriter = csv.writer(f)
        for ship in ships[0]:
            csvwriter.writerow(ship)
    f.close()
    
    # Enemy Ships file
    with open(enemyShipsPath,"w",newline='') as f:
        csvwriter = csv.writer(f)
        for ship in ships[1]:
            csvwriter.writerow(ship)
    f.close()
    
    # Misc file
    with open(miscPath,"w",newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(guesses)
    f.close()
    
    # Board file
    with open(boardPath,"w",newline='') as f:
        csvwriter = csv.writer(f)
        for row in board:
            csvwriter.writerow(row)
    f.close()

def loadGame(name: str) -> list:
    """
    Loads a saved game.
    @param name - the name of the game to load
    @returns the data of the game
    """
    ships = [[],[]]
    board = []
    guessess = []
    
    # File paths
    playerShipsPath = os.path.join(SAVEGAMEPATH,name,"playerShips.csv")
    enemyShipsPath = os.path.join(SAVEGAMEPATH,name,"enemyShips.csv")
    boardPath = os.path.join(SAVEGAMEPATH,name,"board.csv")
    miscPath = os.path.join(SAVEGAMEPATH,name,"misc.csv")
    
    # Player Ships file
    with open(playerShipsPath,"r") as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            ships[0].append(row)
    f.close()
    
    # Enemy Ships file
    with open(enemyShipsPath,"r") as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            ships[1].append(row)
    f.close()
    
    # Misc file
    with open(miscPath,"r") as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            guessess.append(row)
    f.close()
    
    # Board file
    with open(boardPath,"r") as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            board.append(row)
    f.close()
    
    data = [ships, board, guessess]
    
    return data
