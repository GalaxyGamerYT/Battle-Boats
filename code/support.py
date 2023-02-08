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

def generatePlayerCoords(board: list) -> list:
    """
    Generate the coordinates for the players ships.
    @returns the list of coordinates for the players ships.
    """
    shipsCreated = 0
    ships = [[]]
    while shipsCreated <= SHIPAMOUNT:
        print("\033c")
        updatePlayerBoard(ships[0],board)
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
                            ships[0].append(pos)
                            shipsCreated += 1
                        else:
                            print(f"{Fore.RED}{pos} has already been used.")
                    else:
                        print(f"{Fore.RED}{posY} Isn't a valid y coordinate.")
            else:
                print(f"{Fore.RED}{posX} Isn't a valid x coordinate.")
    return ships[0]

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
    playerBoardPath = os.path.join(SAVEGAMEPATH,name,"playerBoard.csv")
    enemyBoardPath = os.path.join(SAVEGAMEPATH,name,"enemyBoardGame.csv")
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
            csvwriter.writerow(f)

def loadGame(name: str) -> list:
    """
    Loads a saved game.
    @param name - the name of the game to load
    @returns the data of the game
    """
    ships = [[],[]]
    board = [[],[]]
    guessess = [[],[]]
    
    # File paths
    playerShipsPath = os.path.join(SAVEGAMEPATH,name,"playerShips.csv")
    enemyShipsPath = os.path.join(SAVEGAMEPATH,name,"enemyShips.csv")
    playerBoardPath = os.path.join(SAVEGAMEPATH,name,"playerBoard.csv")
    enemyBoardPath = os.path.join(SAVEGAMEPATH,name,"enemyBoardGame.csv")
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
    Draw the board in the terminal.
    @param board - the board to draw
    """
    colouredBoard = board
    
    for rowIndex,row in enumerate(board):
        for colIndex,col in enumerate(row):
            if col == "O":
                colouredBoard[rowIndex][colIndex] = f"{Fore.BLUE}O{Fore.RESET}"
            elif col == "H":
                colouredBoard[rowIndex][colIndex] = f"{Fore.YELLO}H{Fore.RESET}"
            elif col == "S":
                colouredBoard[rowIndex][colIndex] = f"{Fore.RED}S{Fore.RESET}"
    
    print("====GAME=BOARD====")
    print(Fore.MAGENTA+"         ---Your Board---")
    print()
    print("   │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 1 │ {board[0][0]} │ {board[0][1]} │ {board[0][2]} │ {board[0][3]} │ {board[0][4]} │ {board[0][5]} │ {board[0][6]} │ {board[0][7]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 2 │ {board[1][0]} │ {board[1][1]} │ {board[1][2]} │ {board[1][3]} │ {board[1][4]} │ {board[1][5]} │ {board[1][6]} │ {board[1][7]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 3 │ {board[2][0]} │ {board[2][1]} │ {board[2][2]} │ {board[2][3]} │ {board[2][4]} │ {board[2][5]} │ {board[2][6]} │ {board[2][7]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 4 │ {board[3][0]} │ {board[3][1]} │ {board[3][2]} │ {board[3][3]} │ {board[3][4]} │ {board[3][5]} │ {board[3][6]} │ {board[3][7]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 5 │ {board[4][0]} │ {board[4][1]} │ {board[4][2]} │ {board[4][3]} │ {board[4][4]} │ {board[4][5]} │ {board[4][6]} │ {board[4][7]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 6 │ {board[5][0]} │ {board[5][1]} │ {board[5][2]} │ {board[5][3]} │ {board[5][4]} │ {board[5][5]} │ {board[5][6]} │ {board[5][7]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 7 │ {board[6][0]} │ {board[6][1]} │ {board[6][2]} │ {board[6][3]} │ {board[6][4]} │ {board[6][5]} │ {board[6][6]} │ {board[6][7]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 8 │ {board[7][0]} │ {board[7][1]} │ {board[7][2]} │ {board[7][3]} │ {board[7][4]} │ {board[7][5]} │ {board[7][6]} │ {board[7][7]} │")
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
        if linear(guessess,ship) != -1:
            board[ship[0]][ship[1]] = "H"
        else:
            board[ship[0]][ship[1]] = "M"
    drawPlayerGrid(board)
    return board

def drawEnemyGrid(board: list) -> None:
    """
    Draw the enemy grid. This is a pretty simple function, but it's a good example of how to use the colours.
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
    
    print("====GAME=BOARD====")
    print()
    print(Fore.CYAN+"         ---Opponents Board---")
    print()
    print("   │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 1 │ {board[0][0]} │ {board[0][1]} │ {board[0][2]} │ {board[0][3]} │ {board[0][4]} │ {board[0][5]} │ {board[0][6]} │ {board[0][7]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 2 │ {board[1][0]} │ {board[1][1]} │ {board[1][2]} │ {board[1][3]} │ {board[1][4]} │ {board[1][5]} │ {board[1][6]} │ {board[1][7]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 3 │ {board[2][0]} │ {board[2][1]} │ {board[2][2]} │ {board[2][3]} │ {board[2][4]} │ {board[2][5]} │ {board[2][6]} │ {board[2][7]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 4 │ {board[3][0]} │ {board[3][1]} │ {board[3][2]} │ {board[3][3]} │ {board[3][4]} │ {board[3][5]} │ {board[3][6]} │ {board[3][7]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 5 │ {board[4][0]} │ {board[4][1]} │ {board[4][2]} │ {board[4][3]} │ {board[4][4]} │ {board[4][5]} │ {board[4][6]} │ {board[4][7]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 6 │ {board[5][0]} │ {board[5][1]} │ {board[5][2]} │ {board[5][3]} │ {board[5][4]} │ {board[5][5]} │ {board[5][6]} │ {board[5][7]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 7 │ {board[6][0]} │ {board[6][1]} │ {board[6][2]} │ {board[6][3]} │ {board[6][4]} │ {board[6][5]} │ {board[6][6]} │ {board[6][7]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")
    print(f" 8 │ {board[7][0]} │ {board[7][1]} │ {board[7][2]} │ {board[7][3]} │ {board[7][4]} │ {board[7][5]} │ {board[7][6]} │ {board[7][7]} │")
    print("───┼───┼───┼───┼───┼───┼───┼───┼───┼")

def updateEnemyBoard(ships: list, board: list, guessess: list) -> list:
    """
    Update the enemy board with the current guesses. If the guess is a hit, change the board to "H" indicating a hit. If the guess is a miss, change the board to "M" indicating a miss.
    @param ships - the ships that have been sunk since the last update.
    @param board - the enemy board.
    @param guessess - the current guesses.
    @return The updated enemy board.
    """
    for ship in ships:
        if linear(guessess,ship) != -1:
            board[ship[0]][ship[1]] = "H"
        else:
            board[ship[0]][ship[1]] = "M"
    drawEnemyGrid(board)
    return board
