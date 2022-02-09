# making a random number genrator that generates random number
def Num(min, max):
    # deifining a random number
    import random
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
