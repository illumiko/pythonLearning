import math
import time

class TicTacToe():
    def __init__(self) -> None:
        self.board = self.makeBoard()
        self.currentWinner = None

    @staticmethod
    def makeBoard():
        return ["_" for _ in range(9)]

    def printBoard(self):
        """""
        print(self.board[0:3]) # i*3:(i+1)*3 |i = 0|
        print(self.board[3:6]) # i*3:(i+1)*3 |i = 1|
        print(self.board[6:9]) # i*3:(i+1)*3 |i = 2|
        """""
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print(" | "+" | ".join(row) +" | ")
    @staticmethod    
    def printBoardNums():
        numberBoard = [[str(i) for i in range(j*3, j(1+1)*3)] for j in range(3)]
        for x in numberBoard:
            print(" | "+" | ".join(x)+" | ")

    def emptySpaces(self):
        return "_" in self.board

    def emptySpacesNum(self):
        return self.board.count("_")

    def availableMoves(self):
        return "_" in self.board

    """""
    @staticmethod
    def XprintBoardNums(j):
        numberBoard = [str(i) for i in range(j*3,(j+1)*3)]
        print(numberBoard)
    """""

def play(game,aPlayer,bPlayer, printGame=True):
    if printGame:
        game.printBoardNums()
    letter = 'X'

    while game.emptySpaces():
        if letter == "O":
            square = bPlayer.get_move(game)
        else:
            square = aPlayer.get_move(game)

        if game.makeMove(square, letter):
            if printGame:
                print(letter + 'makes a move to sqaure', square)
                game.printBoard()
                print('')

            if game.currentWinner:
                if printGame:
                    print(letter + 'wins!')
                return letter # ends the loop and exits
            letter = 0 if letter == "X" else "X"
        time.sleep(.8)

    if printGame:
        print("its a tie")




x = TicTacToe()
x.printBoardNums()

        


