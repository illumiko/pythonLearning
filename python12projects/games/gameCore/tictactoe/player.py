import math
import random

class Player:
    def __init__(self, letter) -> None:
        # letter is X or 0
        self.letter = letter
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)

    def get_move(self,game):
        square = random.choice(game.availableMoves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)
    def get_move(self,game):
        validSpaces = False
        val = None
        while not validSpaces:
            square = input(self.letter + "'s turn. Input(0-8)")
            try:
                val = int(square)
                if val not in game.availableMoves():
                    raise ValueError
                validSpaces = True
            except ValueError:
                print("Invalid move, Try again")
        return val


