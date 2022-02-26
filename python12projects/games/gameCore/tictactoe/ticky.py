from tickyPlayer import HumanPlayer,ComputerPlayer
class Game:
    def __init__(self,player1,player2):
        self.gameBoard = self.makeBoard(False)
        self.player1 = player1
        self.player2 = player2

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

    def checkWin(self,gameBoard,letter):
        rowWins = gameBoard[(letter//3)*3:((letter//3)+1)*3]
        colWin = [gameBoard[col_ind+i*3] for i in range(3)]

        pass

    def play(self,printBoard=True,):
        import time
        playingBoard = self.gameBoard
        if printBoard:
            self.formattedBoard(self.makeBoard(True))
            print("")
            self.formattedBoard(playingBoard)

        letter = "X"
        while self.avaliableMoves() != 0:
            self.player1.makeMove(playingBoard,letter)
            if letter == "X":
                letter = "O"
            else:
                letter = "X"
            self.player2.makeMove(playingBoard,letter)
            if printBoard:
                time.sleep(.4)
                self.formattedBoard(playingBoard)
        



test = Game(HumanPlayer("Eyanat"), ComputerPlayer("ComputerPlayer"))
test.play(True)
# print(test.printBoard(test.makeBoard(False)))

        

