class Game:
    """
    Initialize the game state.
    @param ships - the number of ships to be placed on the board.
    @param board - the board size.
    @param guessess - the number of guesses the player has.
    """
    def __init__(self, ships, board, guessess):
        """
        Initialize the game state.
        @param ships - the number of ships in the game.
        @param board - the size of the board.
        @param guessess - the number of guesses the player has.
        """
        self.ships = ships
        self.board = board
        self.guessess = guessess
