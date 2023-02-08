from settings import *
from support import *

class Game:
    """
    Initialize the game state.
    @param ships - the number of ships to be placed on the board.
    @param board - the board size.
    @param guessess - the number of guesses the player has.
    """
    def __init__(self, ships: list, board: list, guesses: list):
        """
        Initialize the game state.
        @param ships - the number of ships in the game.
        @param board - the size of the board.
        @param guessess - the number of guesses the player has.
        """
        self.ships = ships
        self.board = board
        self.guesses = guesses
        self.sunkShips = [0,0]
        self.gameOver = False
    
    def checkSunkShips(self,guess: list, ships: list, sunkShips: int) -> int:
        for ship in ships:
            search = linear(guess,ship)
            if search != -1:
                sunkShips += 1
        if self.sunkShips == SHIPAMOUNT:
            self.gameOver = True
        return sunkShips
    
    def generateEnemyGuess(self):
        """
        Generate a random guess for the enemy. If the guess is already in the list of guesses,
        generate a new guess.
        @param self - the object itself, used to access the guesses list.
        """
        guessed = False
        while not guessed:
            pos = (randint(0,GRIDSIZE-1),randint(0,GRIDSIZE-1))
            if linear(self.guesses,pos) == -1:
                self.guesses.append(pos)
                guessed = True
    
    def generatePlayerGuess(self):
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
                                shipsCreated += 1
                            else:
                                print(f"{Fore.RED}{pos} has already been used.")
                        else:
                            print(f"{Fore.RED}{posY} Isn't a valid y coordinate.")
                else:
                    print(f"{Fore.RED}{posX} Isn't a valid x coordinate.")
    
    def run(self):
        updatePlayerBoard(self.ships[0], self.board[0], self.guesses)
        self.guesses[1] = self.generateEnemyGuess()
        self.checkSunkShips()
        input(Fore.MAGENTA+"Press ENTER to continue...")
