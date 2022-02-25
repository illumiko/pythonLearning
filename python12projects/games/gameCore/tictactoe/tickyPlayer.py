class Player:
    def __init__(self, name,letter):
        self._name = name
        self.points = 0
        self.withdrawed = False
        self.letter = letter

    @property
    def name(self):
        return self._name

"""""
    def withdraw(self):
        pass
    
    def makeMove(self,gameBoard):
        usrInput = input("Enter a number from(0-8)")
        gameBoard[usrInput] = self.letter
"""""
class HumanPlayer(Player):
    def __init__(self, name, letter):
        super().__init__(name, letter)

    def withdraw(self):
        self.withdrawed = True
        pass
    
    def makeMove(self,gameBoard):
        usrInput = input("Enter a number from(0-8)")
        gameBoard[usrInput] = self.letter

class ComputerPlayer(Player):
    def __init__(self, name, letter):
        super().__init__(name, letter)

