import string
import random
def hangmanGame(words):
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
