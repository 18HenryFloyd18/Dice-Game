import random
import math
diceList = [1,2,3,4,5,6]
comp_Wins = 0
player_Wins = 0
while:
    randomComp = random.choice(diceList)
    print("The Number That The Computer Rolled Was",randomComp)

    randomPlayer = random.choice(diceList)
    print("The Number That You Rolled Was",randomPlayer)

    if(randomComp > randomPlayer):
       print("The Computer Won This Round!")
    elif(randomComp == randomPlayer):
       print("You And The Computer Got The Same Numbers, Let's Redo The Round")
    else:
       print("You Won This Round!")
    
    if(randomComp > randomPlayer):
        compWins.append(1)
        print("Computer Score:",comp_Wins)
        print("Player's Score:",player_Wins)
    elif(randomComp == randomPlayer):
        print("Computer's Score:",comp_Wins)
        print("Player's Score:",player_Wins)
    else:
        playerWins.append(1)
        print("Computer's Score:",comp_Wins)
        print("Player's Score:",player_Wins)

    




