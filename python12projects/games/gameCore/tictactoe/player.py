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
        pass

class HumanPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)
    def get_move(self,game):
        pass
