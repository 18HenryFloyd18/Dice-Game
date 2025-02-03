import random
import math
diceList = [1,2,3,4,5,6]
print("Welcome To Dice Battle!")
wannaPlay = str(input("If You Would Like To Play Type The Word Enter:"))

if(wannaPlay == "Enter"):
    print("Welcome To The Game!")
else:
    print("To Play Please Type Enter")
random.choice(diceList)
print(diceList)

