from time import sleep

from settings import *
from support import *

class Game:
    """
    The game function of the game. This function has the game.
    """
    def __init__(self, ships: list, board: list, guesses: list, name: str, sunkShips: list):
        """
        Initialize the player class.
        @param ships - the ships the player has been given           
        @param board - the board the player is playing on           
        @param guesses - the guesses the player has made           
        @param name - the name of the player           
        """
        self.name = name
        self.ships = ships
        self.board = board
        self.guesses = guesses
        self.sunkShips = sunkShips
        self.gameOver = False
    
    def checkSunkShips(self, guess: list, ships: list, sunkShips: int) -> int:
        """
        Check if the guess is a hit or miss. If it is a hit, check if the ship has been sunk.
        @param guess - the guess from the player.
        @param ships - the list of ships.
        @param sunkShips - the number of sunk ships.
        @return The number of sunk ships.
        """
        for ship in ships:
            search = linear(guess,ship)
            if search != -1:
                sunkShips += 1
        if self.sunkShips == SHIPAMOUNT:
            self.gameOver = True
        return sunkShips
    
    def generateEnemyGuess(self):
        """
        Generate a random guess for the enemy.
        @returns the guess
        """
        guessed = False
        while not guessed:
            pos = (randint(0,GRIDSIZE-1),randint(0,GRIDSIZE-1))
            if linear(self.guesses[1],pos) == -1:
                self.guesses[1].append(pos)
                print(f"The enemy has guessed {pos[0]+1},{pos[1]+1}")
                guessed = True
    
    def generatePlayerGuess(self):
        """
        Generate a guess for the player. The player can only guess once.
        @returns the guess
        """
        guessed = False
        while not guessed:
            posX = input("Input the X coordinate[A-H]: ").upper()
            try:
                xCoordConvert[posX]
            except:
                print(f"{Fore.RED}{posX} Isn't a valid x coordinate.")
            else:
                posX = xCoordConvert[posX]
                if posX >=0 and posX <= GRIDSIZE-1:
                    posY = input("Input the y corrdinate[A-H]: ")
                    try:
                        int(posY)
                    except:
                        print(f"{Fore.RED}{posY} Isn't a valid y coordinate.")
                    else:
                        posY = int(posY)-1
                        if posY >= 0 and posY <= GRIDSIZE-1:
                            pos = (posX,posY)
                            print(pos)
                            if linear(self.guesses[0], pos) == -1:
                                self.guesses[0].append(pos)
                                guessed = True
                            else:
                                print(f"{Fore.RED}{pos} has already been used.")
                        else:
                            print(f"{Fore.RED}{posY} Isn't a valid y coordinate.")
                else:
                    print(f"{Fore.RED}{posX} Isn't a valid x coordinate.")
    
    def run(self):
        """
        Run the game. This is the main function for the game. It will run until either the player or the enemy has won.
        @param self - the game object itself
        """
        clearWindow()
        print("         ====GAME=BOARD====")
        updateEnemyBoard(self.ships[1], self.board[1], self.guesses[0])
        updatePlayerBoard(self.ships[0], self.board[0], self.guesses[1])
        input(Fore.MAGENTA+"Press ENTER to start...")
        
        while self.sunkShips[0] < 5 or self.sunkShips[1] < 5:
            clearWindow()
            updateEnemyBoard(self.ships[1], self.board[1], self.guesses[0])
            self.generatePlayerGuess()
            clearWindow()
            updateEnemyBoard(self.ships[1], self.board[1], self.guesses[0])
            self.checkSunkShips(self.guesses[0],self.ships[1],self.sunkShips[0])
            saveGame(self.ships,self.board,self.name,self.guesses,self.sunkShips)
            
            updatePlayerBoard(self.ships[0], self.board[0], self.guesses[1])
            sleep(1)
            self.generateEnemyGuess()
            sleep(1)
            clearWindow()
            updatePlayerBoard(self.ships[0], self.board[0], self.guesses[1])
            self.checkSunkShips(self.guesses[1],self.ships[0],self.sunkShips[1])
            saveGame(self.ships,self.board,self.name,self.guesses,self.sunkShips)
            
            sleep(1)
            clearWindow()
            print("         ====GAME=BOARD====")
            updateEnemyBoard(self.ships[1], self.board[1], self.guesses[0])
            updatePlayerBoard(self.ships[0], self.board[0], self.guesses[1])
            input(Fore.MAGENTA+"Press ENTER to continue...")
        
        if self.sunkShips[0] == 5:
            print("You Won!")
        elif self.sunkShips[1] == 5:
            print("Your Opponent Won!")
        
        saveGame(self.ships,self.board,self.name,self.guesses,self.sunkShips)
        input(Fore.MAGENTA+"Press ENTER to go back to menu...")
        os.removedirs(os.path.join(SAVEGAMEPATH,self.name))
