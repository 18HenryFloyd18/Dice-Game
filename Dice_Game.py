import random
import math
diceList = [1,2,3,4,5,6]
compWins = []
playerWins = []

# print("Welcome To Dice Battle!")
# wannaPlay = str(input("Type 'Enter' If You Would Like To Play:"))

# if(wannaPlay == "Enter" or "enter"):
#     print("Lets Begin! First To 3 Round Victory's Wins!")
# else:
#     print("Type 'Enter' To Begin Playing")

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




