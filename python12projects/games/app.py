# core games
from functools import partial
from gameCore.janken import janken
from gameCore.guessTheNumber import guessNum
from gameCore.compGuessYourNumber import compGuess
from gameCore.hangman import game
# utilities
from gameCore.utils import utils
def gameMenu():
    minMaxInts =  utils.randoCore()
    max = minMaxInts[0]
    min = minMaxInts[1]
    intro = [
     'Guess the number(0)',
     'Computer Gueses your number(1)',
     "RockPaperScissors(2)",
     "Hangman(3)"
    ]
    print(intro)
    usrInpu = int(input("Enter a number: "))
    games = [
        partial(guessNum.Num,min, max),
        partial(compGuess.Guess,min, max),
        partial(janken.RPS,5),
        partial(game.hangmanGame,utils.words),
    ]
    games[usrInpu]()

gameMenu()
