from words import words
import random
# making a random number genrator that generates random number
def randoCore():
    rando1 = random.randint(1, 100)
    rando2 = random.randint(1, 100)
    # checks for which var is the geater and returns value accordingly
    if(rando1>rando2):
        return [rando1, rando2]
    # else:
    #     return [rando2, rando1]

def guessNum(min, max):
    # deifining a random number
    num = random.randint(min, max)
    print(f'Guess a number between {min} and {max}')
    # setting base num
    guess = 0
    while guess != num:
        # while guess not equal num return a val acc to guess 
        guess = int(input(f'Guess the number: '))
        if guess > num:
            print('Too high')
        else:
            print('Too low')
    print(f'Congrats on guess the number {num}')

def compGuessNum(min, max):
    print(f'Select a number between {min} and {max} for the computer to guess')
    num = int(input('Number: '))  # asking user for a number
    # setting guess range for the comp
    low = min
    high = max
    guess = 0
    while guess != num:
        guess = random.randint(low, high)
        print(guess, low, high)
        if guess > num:
            high = high - 1
        elif guess < num:
            low = low - 1
    print(f'number guessed correctly {guess}')

def jankun(winPoint):
    # intro msg for the user
    intro = 'Rock(1) || Paper(2) || Scissor(3)'
    # possible outputs
    combinations = ['Rock', 'Paper', 'Scissor']
    # list of array index which indicated win conditions
    winCondition = {
        'PlayerWin': [ [0,1],  [1,2],  [0,2], ],
        'ComputerWin': [ [1,0], [2,1], [2,0],],
        'Draw': [ [1,1], [0,0], [2,2],]
    }
    # point tracker
    points = {
        "player": 0,
        "computer": 0,
        "winPoint": winPoint
    }
        

    # continues the game until loop condition is filled
    while points["player"] < points["winPoint"] and points["computer"] < points["winPoint"]:
        print(intro)
        compSelect = random.randint(0,2)
        usrInput = int(input("Please select a move: "))
        usrSelection = combinations[usrInput - 1]
        compSelection = combinations[compSelect]
        outCome = [compSelect, usrInput -1]
        print("-------------------------------------------------------------------------")
        print("Computer: ", compSelection,"\nPlayer: ", usrSelection,)
        for key,val in winCondition.items():
            if key == 'ComputerWin':
                for i in val:
                    if i == outCome:
                        points['computer'] +=1
                        print('[[ComputerWins]]')
                        print('Points:', points)
                        print("-------------------------------------------------------------------------")
            elif key == 'PlayerWin':
                for i in val:
                    if i == outCome:
                        points['player'] +=1
                        print('[[PlayerWins]]')
                        print('Points:',points)
                        print("-------------------------------------------------------------------------")
            elif key == "Draw":
                for i in val:
                    if i == outCome:
                        print('DRAW')
                        print("-------------------------------------------------------------------------")


def hangman():
    from words import words
    import string
    # this filters words with - and a white space
    def filterWords():
        word = random.choice(words)
        while "-" in word and " " in word:
            word = random.choice(words)
        return word.lower()
    def game():
        gWord = list(filterWords())
        xWord = gWord.copy()
        alphabets = list(string.ascii_lowercase)
        usrRepeat = []
        print("type: IDK to give up")
        while len(gWord) != 0 :
            displayedWord = ['-' if item not in usrRepeat else item for item in xWord ]
            print("-------------------------------------------------------------------------")
            print("Guess Word:\n",' '.join(displayedWord), "\nGuessed Words:\n", " ".join(usrRepeat))
            print("-------------------------------------------------------------------------")
            usrInput = str(input("Enter a letter: ")).lower()
            if usrInput in alphabets:
                if usrInput in gWord:
                    usrRepeat.append(usrInput)
                    gWord.remove(usrInput)
                    print(gWord)
                else:
                    print("\nPlease try again\n")
            elif usrInput == "idk":
                print("the word was: ", ''.join(gWord))
                break
            else:
                print("Invalid character")
                break
        print("#########################################################################")
        print("Congrats you guess the words: ", ''.join(xWord))
        print("#########################################################################")
    game()
        

    minMaxInts = randoCore()

def gameMenu():
    games = [ 
            'Guess the number(1)', 
            'Computer Gueses your number(2)',
            "RockPaperScissors(3)",
            "Hangman(4)"
            ]
    print(games)
    gameSelect = int(input('Please select a game: '))
    if gameSelect == 1:
        guessNum(minMaxInts[1], minMaxInts[0])
        again = input('Game Over, will play another game? Yes(Y/y) No(N/n): ').lower()
        if again == 'y':
            gameMenu()
        else:
            print('Thanks for playing')
    elif gameSelect == 2:
        compGuessNum(minMaxInts[1], minMaxInts[0])
        again = input('Game Over, will play another game? Yes(Y/y) No(N/n): ').lower()
        if again == 'y':
            gameMenu()
        else:
            print('Thanks for playing')
    elif gameSelect == 3:
        jankun(int(input("Please set a win point: ")))
        again = input('Game Over \nwill play another game? Yes(Y/y) No(N/n): ').lower()
        if again == 'y':
            gameMenu()
        else:
            print('Thanks for playing')
    elif gameSelect == 4:
        hangman()
        again = input('Game Over \nwill play another game? Yes(Y/y) No(N/n): ').lower()
        if again == 'y':
            gameMenu()
        else:
            print('Thanks for playing')

gameMenu()
