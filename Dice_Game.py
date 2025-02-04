import random
import math
diceList = [1,2,3,4,5,6]
# print("Welcome To Dice Battle!")
# wannaPlay = str(input("If You Would Like To Play Type The Word Enter:"))

# if(wannaPlay == "Enter"):
#     print("Welcome To The Game!")
# else:
#     print("To Play Please Type Enter")

randomComp = random.choice(diceList)
print("The Number That The Computer Rolled Was",randomComp)

randomPlayer = random.choice(diceList)
print("The Number That You Rolled Was",randomPlayer)

if(randomComp > randomPlayer):
    print("The Computer Won This Round!")
else:
    print("You Won This Round!")



