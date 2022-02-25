import math
import time
from player import HumanPlayer,RandomComputerPlayer

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
        numberBoard = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for x in numberBoard:
            print(" | "+" | ".join(x)+" | ")

    def emptySpaces(self):
        # retruns boolen
        return "_" in self.board

    def emptySpacesNum(self):
        return self.board.count("_")

    def availableMoves(self):
        # return "_" in self.board
        return [i for i,spot in enumerate(self.board) if spot == "_"]

    def makeMove(self,square,letter):
        if self.board[square] == "_":
            self.board[square] = letter
            if self.winCondition(square,letter):
                self.currentWinner = letter
            return True
        return False

    def winCondition(self,square,letter):
        horizontalWin = [self.board[(square//3)*3+x] for x in range(3)]
        verticleWin = [self.board[square%3+x*3] for x in range(3)]
        if all(square == letter for square in horizontalWin):
            return True
        if all(square == letter for square in verticleWin):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False
            



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
            letter = 'O' if letter == "X" else "X"
        time.sleep(.8)

    if printGame:
        print("its a tie")



if __name__ == '__main__':
    x_player = RandomComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, printGame=True)
        

