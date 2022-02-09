import random
def RPS(winPoint):
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
