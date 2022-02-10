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

    """""
    @staticmethod
    def XprintBoardNums(j):
        numberBoard = [str(i) for i in range(j*3,(j+1)*3)]
        print(numberBoard)
    """""

x = TicTacToe()

        


