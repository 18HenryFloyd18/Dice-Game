import random
import math
diceList = [1,2,3,4,5,6]
comp_Wins = 0
player_Wins = 0
print("Welcome To Dice Game!")
print("Game Rules: You And The Computer Roll A Dice, Whoever Has The Highest Dice Number Wins The Round. First To Three Wins Takes The Victory!")
trynaGame = str(input("If You Would Like To Play Enter 'Game'"))
if(trynaGame == "Game" or "game"):
    print("The Computer Will Roll First")
else:
    print("If You Would Like To Play Enter 'Game'")
while True:
    while(player_Wins < 3 and comp_Wins < 3):
      randomComp = random.choice(diceList)
      print("The Number That The Computer Rolled Was",randomComp)

      wannaPlay = str(input("Type 'Roll' To Roll The Dice:"))
      if(wannaPlay != "Roll" or "roll"):
        print("If You Want To Play Please Enter 'Roll'")
      randomPlayer = random.choice(diceList)
      print("The Number That You Rolled Was",randomPlayer)

      if(randomComp > randomPlayer):
        print("The Computer Won This Round!")
      elif(randomComp == randomPlayer):
        print("You And The Computer Got The Same Numbers, Let's Redo The Round")
      else:
        print("You Won This Round!")
    
      if(randomComp > randomPlayer):
        comp_Wins = comp_Wins + 1
        print("Computer Score:",comp_Wins)
        print("Player's Score:",player_Wins)
      elif(randomComp == randomPlayer):
        print("Computer's Score:",comp_Wins)
        print("Player's Score:",player_Wins)
      else:
        player_Wins = player_Wins + 1
        print("Computer's Score:",comp_Wins)
        print("Player's Score:",player_Wins)
    if(player_Wins > comp_Wins):
      print("You Won Congrats!")
    else:
      print("The Computer Won This Game, Better Luck Next Game")
    break
    
    




