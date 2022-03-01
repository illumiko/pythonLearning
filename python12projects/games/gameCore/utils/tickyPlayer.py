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

    # unused
    def withdraw(self):
        self.withdrawed = True
        pass
   
    def makeMove(self,gameBoard,letter):
    # taking usr input for index of spot in game baord
        usrInput = int(input("Enter a number from(0-8)"))
        # check if the usr input is on top of taken spot or not
        while gameBoard[usrInput] != "_":
            print("[[The square you selected has already been used]]")
            # asking for new usr input index
            usrInput = int(input("Enter a number from(0-8)"))
            # breaking loop when usr input spot is of epmty spot
            if gameBoard[usrInput] == "_":
                gameBoard[usrInput] = letter
                break
        # what happens when index is empty spot
        gameBoard[usrInput] = letter
        print(f"[[{self.name} moved to {usrInput}]]")
        return [int(usrInput),str(letter)]

class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def makeMove(self, gameBoard,letter):
        import random
        # talking a random index from (0-8) as spot on game baord
        index = random.choice([i for i in range(9)])
        # handling when index is not an empty spot
        while gameBoard[index] != "_":
            index = random.choice([i for i in range(9)])
            # breaking out of loop when empty spot found
            if gameBoard[index] == "_":
                gameBoard[index] = letter
                print('found')

        # what happens when index is empty spot
        gameBoard[index] = letter
        # printing move details
        print(f"[[{self.name} moved to {index}]]")
            
        return [int(index),str(letter)]



