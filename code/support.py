import os, csv
from random import randint
from colorama import *

from settings import *

def generateEnemyCoords() -> list:
    """
    Generate a list of enemy ship coordinates.
    @returns the list of enemy ship coordinates
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
    Given an array and a value, return the index of the value in the array. If the value is not in the array, return -1.
    @param arr - the array to search for the value in.
    @param x - the value to search for in the array.
    @return the index of the value in the array.
    """
    for index,i in enumerate(arr):
        if i == x:
            return index
    return -1

def extendedLinear(arr: list, x) -> int:
    """
    Given an array and a value, return the index of the value in the array. If the value is not in the array, return -1.
    @param arr - the array to search for the value in.
    @param x - the value to search for.
    @return the index of the value in the array.
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
    @returns the content of the folder.
    """
    if not os.path.exists(path):
        os.mkdir(path)
    content = os.listdir(path)
    return content

def generatePlayerCoords(board: list) -> list:
    """
    Generate the player's board and allow them to place their ships.
    @param board - the board for the player to play on
    @returns the board with the ships added
    """
    shipsCreated = 0
    ships = []
    while shipsCreated <= SHIPAMOUNT:
        #print("\033c")
        clearWindow()
        updatePlayerBoard(ships,board)
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
    Save the game to the save game folder.
    @param ships - the player's ships           
    @param board - the player's board           
    @param name - the name of the game           
    @param guesses - the player's guesses           
    """
    # Checks for game folder and creates it.
    folderCheck(os.path.join(SAVEGAMEPATH,name))
    
    # File paths
    playerShipsPath = os.path.join(SAVEGAMEPATH,name,"playerShips.csv")
    enemyShipsPath = os.path.join(SAVEGAMEPATH,name,"enemyShips.csv")
    playerBoardPath = os.path.join(SAVEGAMEPATH,name,"playerBoard.csv")
    enemyBoardPath = os.path.join(SAVEGAMEPATH,name,"enemyBoard.csv")
    playerGuessessPath = os.path.join(SAVEGAMEPATH,name,"playerGuessess.csv")
    enemyGuessessPath = os.path.join(SAVEGAMEPATH,name,"enemyGuessess.csv")
    
    # Player Ships File
    with open(playerShipsPath,"w",newline='') as f:
        csvwriter = csv.writer(f)
        for ship in ships[0]:
            csvwriter.writerow(ship)
    f.close()
    
    # Enemy Ships File
    with open(enemyShipsPath,"w",newline='') as f:
        csvwriter = csv.writer(f)
        for ship in ships[1]:
            csvwriter.writerow(ship)
    f.close()
    
    # Player Guessess File
    with open(playerGuessessPath,"w",newline='') as f:
        csvwriter = csv.writer(f)
        for ship in guesses[0]:
            csvwriter.writerow(ship)
    f.close()
    
    # Enemy Guessess File
    with open(enemyGuessessPath,"w",newline='') as f:
        csvwriter = csv.writer(f)
        for ship in guesses:
            csvwriter.writerow(ship)
    f.close()
    
    # Player Board File
    with open(playerBoardPath,"w",newline='') as f:
        csvwriter = csv.writer(f)
        for row in board[0]:
            csvwriter.writerow(row)
    f.close()
    
    # Enemy Board File
    with open(enemyBoardPath,"w",newline='') as f:
        csvwriter = csv.writer(f)
        for row in board[1]:
            csvwriter.writerow(row)

def loadGame(name: str) -> list:
    """
    Load the game from the save folder.
    @param name - the name of the game to load
    @returns the game data
    """
    ships = [[],[]]
    board = [[],[]]
    guessess = [[],[]]
    
    # File paths
    playerShipsPath = os.path.join(SAVEGAMEPATH,name,"playerShips.csv")
    enemyShipsPath = os.path.join(SAVEGAMEPATH,name,"enemyShips.csv")
    playerBoardPath = os.path.join(SAVEGAMEPATH,name,"playerBoard.csv")
    enemyBoardPath = os.path.join(SAVEGAMEPATH,name,"enemyBoard.csv")
    playerGuessessPath = os.path.join(SAVEGAMEPATH,name,"playerGuessess.csv")
    enemyGuessessPath = os.path.join(SAVEGAMEPATH,name,"enemyGuessess.csv")
    
    # Player Ships File
    with open(playerShipsPath,"r") as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            ships[0].append(row)
    f.close()
    
    # Enemy Ships File
    with open(enemyShipsPath,"r") as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            ships[1].append(row)
    f.close()
    
    # Player Guesses File
    with open(playerGuessessPath,"r") as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            guessess[0].append(row)
    f.close()
    
    # Enemy Guesses File
    with open(enemyGuessessPath,"r") as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            guessess[1].append(row)
    f.close()
    
    # Player Board File
    with open(playerBoardPath,"r") as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            board[0].append(row)
    f.close()
    
    # Enemy Board File
    with open(enemyBoardPath,"r") as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            board[1].append(row)
    
    data = [ships, board, guessess]
    
    return data

def drawPlayerGrid(board: list) -> None:
    """
    Draw the board with the pieces in the correct place.
    @param board - the board to draw
    """
    colouredBoard = board
    
    for rowIndex,row in enumerate(board):
        for colIndex,col in enumerate(row):
            if col == "O":
                colouredBoard[rowIndex][colIndex] = f"{Fore.BLUE}O{Fore.RESET}"
            elif col == "H":
                colouredBoard[rowIndex][colIndex] = f"{Fore.YELLOW}H{Fore.RESET}"
            elif col == "S":
                colouredBoard[rowIndex][colIndex] = f"{Fore.RED}S{Fore.RESET}"
            elif col == "M":
                colouredBoard[rowIndex][colIndex] = f"{Fore.GREEN}M{Fore.RESET}"
    
    print()
    print(Fore.MAGENTA+"         ---Your Board---")
    print()
    print("   │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 1 │ {board[0][0]} │ {board[1][0]} │ {board[2][0]} │ {board[3][0]} │ {board[4][0]} │ {board[5][0]} │ {board[6][0]} │ {board[7][0]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 2 │ {board[0][1]} │ {board[1][1]} │ {board[2][1]} │ {board[3][1]} │ {board[4][1]} │ {board[5][1]} │ {board[6][1]} │ {board[7][1]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 3 │ {board[0][2]} │ {board[1][2]} │ {board[2][2]} │ {board[3][2]} │ {board[4][2]} │ {board[5][2]} │ {board[6][2]} │ {board[7][2]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 4 │ {board[0][3]} │ {board[1][3]} │ {board[2][3]} │ {board[3][3]} │ {board[4][3]} │ {board[5][3]} │ {board[6][3]} │ {board[7][3]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 5 │ {board[0][4]} │ {board[1][4]} │ {board[2][4]} │ {board[3][4]} │ {board[4][4]} │ {board[5][4]} │ {board[6][4]} │ {board[7][4]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 6 │ {board[0][5]} │ {board[1][5]} │ {board[2][5]} │ {board[3][5]} │ {board[4][5]} │ {board[5][5]} │ {board[6][5]} │ {board[7][5]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 7 │ {board[0][6]} │ {board[1][6]} │ {board[2][6]} │ {board[3][6]} │ {board[4][6]} │ {board[5][6]} │ {board[6][6]} │ {board[7][6]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 8 │ {board[0][7]} │ {board[1][7]} │ {board[2][7]} │ {board[3][7]} │ {board[4][7]} │ {board[5][7]} │ {board[6][7]} │ {board[7][7]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")

def updatePlayerBoard(ships: list, board: list, guessess: list = []) -> list:
    """
    Update the player board with the ships and guesses.
    @param ships - the ships on the board           
    @param board - the board to update           
    @param guessess - the guesses on the board           
    @return The updated board           
    """
    for ship in ships:
        board[int(ship[0])][int(ship[1])] = "O"
    
    for guess in guessess:
        if linear(ships, guess) != -1:
            board[int(guess[0])][int(guess[1])] = "S"
        else:
            board[int(guess[0])][int(guess[1])] = "M"
    
    drawPlayerGrid(board)
    return board

def drawEnemyGrid(board: list) -> None:
    """
    Draw the enemy grid. This is a helper function for the main function.
    @param board - the board to draw
    """
    colouredBoard = board
    
    for rowIndex,row in enumerate(board):
        for colIndex,col in enumerate(row):
            if col == "H":
                colouredBoard[rowIndex][colIndex] = f"{Fore.YELLOW}H{Fore.RESET}"
            elif col == "S":
                colouredBoard[rowIndex][colIndex] = f"{Fore.RED}S{Fore.RESET}"
            elif col == "M":
                colouredBoard[rowIndex][colIndex] = f"{Fore.GREEN}M{Fore.RESET}"
    
    print()
    print(Fore.CYAN+"         ---Opponents Board---")
    print()
    print("   │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 1 │ {board[0][0]} │ {board[1][0]} │ {board[2][0]} │ {board[3][0]} │ {board[4][0]} │ {board[5][0]} │ {board[6][0]} │ {board[7][0]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 2 │ {board[0][1]} │ {board[1][1]} │ {board[2][1]} │ {board[3][1]} │ {board[4][1]} │ {board[5][1]} │ {board[6][1]} │ {board[7][1]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 3 │ {board[0][2]} │ {board[1][2]} │ {board[2][2]} │ {board[3][2]} │ {board[4][2]} │ {board[5][2]} │ {board[6][2]} │ {board[7][2]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 4 │ {board[0][3]} │ {board[1][3]} │ {board[2][3]} │ {board[3][3]} │ {board[4][3]} │ {board[5][3]} │ {board[6][3]} │ {board[7][3]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 5 │ {board[0][4]} │ {board[1][4]} │ {board[2][4]} │ {board[3][4]} │ {board[4][4]} │ {board[5][4]} │ {board[6][4]} │ {board[7][4]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 6 │ {board[0][5]} │ {board[1][5]} │ {board[2][5]} │ {board[3][5]} │ {board[4][5]} │ {board[5][5]} │ {board[6][5]} │ {board[7][5]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 7 │ {board[0][6]} │ {board[1][6]} │ {board[2][6]} │ {board[3][6]} │ {board[4][6]} │ {board[5][6]} │ {board[6][6]} │ {board[7][6]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 8 │ {board[0][7]} │ {board[1][7]} │ {board[2][7]} │ {board[3][7]} │ {board[4][7]} │ {board[5][7]} │ {board[6][7]} │ {board[7][7]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")

def updateEnemyBoard(ships: list, board: list, guessess: list) -> list:
    """
    Update the enemy board with the latest guesses.
    @param ships - the list of ships on the board           
    @param board - the enemy board           
    @param guessess - the list of guesses           
    @return The updated enemy board           
    """
    for guess in guessess:
        if linear(ships,guess) != -1:
            board[int(guess[0])][int(guess[1])] = "S"
        else:
            board[int(guess[0])][int(guess[1])] = "M"
    drawEnemyGrid(board)
    return board

def clearWindow():
    """
    Clear the console window. This is used to make the console window clear when we are           
    printing the results of the training. This is because the console window is not cleared when           
    the program is running. This is a simple function that clears the console window.           
    """
    os.system('cls')
