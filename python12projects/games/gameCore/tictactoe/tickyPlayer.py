class Player:
    def __init__(self, name,letter):
        self._name = name
        self.points = 0
        self.letter = letter

    @property
    def name(self):
        return self._name

class HumanPlayer(Player):
    def __init__(self, name, letter):
        super().__init__(name, letter)
        self.withdrawed = False

    def withdraw(self):
        self.withdrawed = True
        pass
    
    def makeMove(self,gameBoard):
        usrInput = input("Enter a number from(0-8)")
        gameBoard[usrInput] = self.letter

class ComputerPlayer(Player):
    def __init__(self, name, letter):
        super().__init__(name, letter)

    def makeMove(self, gameBoard):
        import random
        index = random.choice([i for i in range(9)])
        gameBoard[index] = self.letter


