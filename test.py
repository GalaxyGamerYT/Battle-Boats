import os, csv

def folderCheck(path: str) -> list:
    """Checks for a folder and returns the content of the folder."""
    if not os.path.exists(path):
        os.mkdir(path)
    content = os.listdir(path)
    return content

def saveGame(ships: list, board: list, name: str):
    folderCheck(os.path.join("saves",name))
    
    # File paths
    playerShipsPath = os.path.join("saves",name,"playerShips.csv")
    enemyShipsPath = os.path.join("saves",name,"enemyShips.csv")
    boardPath = os.path.join("saves",name,"board.csv")
    
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
    
    # Board file
    with open(boardPath,"w",newline='') as f:
        csvwriter = csv.writer(f)
        for row in board:
            csvwriter.writerow(row)
    f.close()

a = [[(1,1),(2,2)],[(3,3),(4,4)]]
b = [["",""],["S","H"],["",""],["M","S"],["H","M"],["",""],["","H"],["S","M"]]
name = "Save2"

saveGame(a,b,name)
