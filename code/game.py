from time import sleep

from settings import *
from support import *

class Game:
    """
    The game function of the game. This function has the game.
    """
    def __init__(self, ships: list, board: list, guesses: list, name: str):
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
        self.sunkShips = [0,0]
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
            posX = input("X coordinate[1,8]: ")
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
        Run the game. This is the main function of the game. It will run until the game is over.
        @param self - the game object itself
        """
        clearWindow()
        print("         ====GAME=BOARD====")
        updateEnemyBoard(self.ships[1], self.board[1], self.guesses[0])
        updatePlayerBoard(self.ships[0], self.board[0], self.guesses[1])
        input(Fore.MAGENTA+"Press ENTER to start...")
        
        while not self.gameOver:
            clearWindow()
            updateEnemyBoard(self.ships[1], self.board[1], self.guesses[0])
            self.generatePlayerGuess()
            clearWindow()
            updateEnemyBoard(self.ships[1], self.board[1], self.guesses[0])
            self.checkSunkShips(self.guesses[0],self.ships[1],self.sunkShips[0])
            saveGame(self.ships,self.board,self.name,self.guesses)
            self.generateEnemyGuess()
            sleep(1)
            clearWindow()
            updatePlayerBoard(self.ships[0], self.board[0], self.guesses[1])
            self.checkSunkShips(self.guesses[1],self.ships[0],self.sunkShips[1])
            saveGame(self.ships,self.board,self.name,self.guesses)
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
        
        saveGame(self.ships,self.board,self.name,self.guesses)
        input(Fore.MAGENTA+"Press ENTER to go back to menu...")
