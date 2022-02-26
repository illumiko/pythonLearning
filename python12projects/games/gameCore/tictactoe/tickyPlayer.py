class Player:
    def __init__(self, name):
        self._name = name
        self.points = 0

    @property
    def name(self):
        return self._name

class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.withdrawed = False

    def withdraw(self):
        self.withdrawed = True
        pass
   
    def makeMove(self,gameBoard,letter):
        usrInput = int(input("Enter a number from(0-8)"))
        while gameBoard[usrInput] != "_":
            print("The square you selected has already been used")
            usrInput = int(input("Enter a number from(0-8)"))
            gameBoard[usrInput] = letter
        else:
            gameBoard[usrInput] = letter
        return letter

class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def makeMove(self, gameBoard,letter):
        import random
        index = random.choice([i for i in range(9)])
        while gameBoard[index] != "_":
            index = random.choice([i for i in range(9)])
            gameBoard[index] = letter
        else:
            gameBoard[index] = letter
        return letter



