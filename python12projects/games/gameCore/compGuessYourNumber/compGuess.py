# making a random number genrator that generates random number
def Guess(min, max):
    import random
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
