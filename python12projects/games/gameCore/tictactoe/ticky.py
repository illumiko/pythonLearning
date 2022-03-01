class Game:
    def __init__(self,player1,player2):
        self.gameBoard = self.makeBoard(False)
        self.player1 = player1
        self.player2 = player2
        self.winner = None

    @staticmethod
    def makeBoard(num=False):
        if num:
            return [str(i) for i in range(9) ]
        else:
            return ["_" for i in range(9) ]

    @staticmethod
    def formattedBoard(board):
        segment = [board[i*3:(i+1)*3] for i in range(3)]
        for i in range(3):
            print(" | " +" | ".join(segment[i])+" | ")

    def avaliableMoves(self):
        return self.gameBoard.count("_")

    def checkWin(self,gameBoard,val):
        rowWins = gameBoard[(val[0]//3)*3:((val[0]//3)+1)*3]
        colWin = [gameBoard[(val[0]%3)+i*3] for i in range(3)]
        if all(x == val[1] for x in colWin):
            # print("WIN")
            self.winner = True
            print(val[1], "Wins")
        if all(x == val[1] for x in rowWins):
            # print("WIN row")
            self.winner = True
            print(val[1], "Wins")
            
        # no diagonal win am lazy with that
        
    # Game function
    def play(self,printBoard=True,):
        import time
        playingBoard = self.gameBoard

        if printBoard:
            self.formattedBoard(self.makeBoard(True))
            print("")
            # self.formattedBoard(playingBoard)

        # Game loop
        while self.avaliableMoves() != 0 and self.winner != True:
            # player 2 turn 
            self.checkWin(playingBoard,self.player2.makeMove(playingBoard,"X"))
            # Print baord in between
            if printBoard:
                time.sleep(.4)
                self.formattedBoard(playingBoard)
            # player 1 turn
            self.checkWin(playingBoard,self.player1.makeMove(playingBoard,"O"))
        



def startGame(player1,player2,enablePrintBoard=True):
    InitializaGame = Game(player1,player2)
    InitializaGame.play(enablePrintBoard)

# print(test.printBoard(test.makeBoard(False)))

        

