class Game:
    def __init__(self):
        self.gameBoard = self.makeBoard(False)

    @staticmethod
    def makeBoard(num=False):
        if num:
            return [str(i) for i in range(9) ]
        else:
            return ["_" for i in range(9) ]

    @staticmethod
    def printBoard(board):
        segment = [board[i*3:(i+1)*3] for i in range(3)]
        for i in range(3):
            print(" | " +" | ".join(segment[i])+" | ")
            



test = Game()
print(test.printBoard(test.makeBoard(True)))

        

