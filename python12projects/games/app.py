# core games
from functools import partial
from gameCore.janken import janken
from gameCore.guessTheNumber import guessNum
from gameCore.compGuessYourNumber import compGuess
from gameCore.hangman import game
from gameCore.tictactoe import ticky

# utilities
from gameCore.utils import utils #for guess number games
from gameCore.utils.tickyPlayer import HumanPlayer,ComputerPlayer # for tictactoe
def gameMenu():
    minMaxInts =  utils.randoCore()
    max = minMaxInts[0]
    min = minMaxInts[1]
    intro = [
     "-----------------------------------",
     "Guess the number(0)",
     "-----------------------------------",
     "Computer Gueses your number(1)",
     "-----------------------------------",
     "RockPaperScissors(2)",
     "-----------------------------------",
     "Hangman(3)",
     "-----------------------------------",
     "TicTacToe(4)",
     "-----------------------------------",
    ]
    for y in intro:
        print(y)
    usrInpu = int(input("Enter a number: "))
    games = [
        partial(guessNum.Num,min, max),  # guess random number
        partial(compGuess.Guess,min, max),  # computer guess YOUR random number
        partial(janken.RPS,5),  # RockPaperScissors
        partial(game.hangmanGame,utils.words),  # hangman with unlimited lives
        partial(ticky.startGame,HumanPlayer("Human"),ComputerPlayer("Computer"))
    ]
    games[usrInpu]()

gameMenu()
