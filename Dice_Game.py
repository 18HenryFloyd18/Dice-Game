import random #Import The Random Function
import math #Import The Math Function

diceList = [1,2,3,4,5,6] # Create A List 
comp_Wins = 0 #Create A List For The Wins To Be Stored In For The Player And The Computer
player_Wins = 0

print("Welcome To Dice Game!") #Welcome The Player
print("Game Rules: You And The Computer Roll A Dice, Whoever Has The Highest Dice Number Wins The Round. First To Three Wins Takes The Victory!") # Explain The Rules

trynaGame = str(input("If You Would Like To Play Enter 'Game'")) #Ask If They Would Like To Play The Game
if(trynaGame == "Game" or "game"): # If The Input Is Fine, Begin The Game. If It Is Not Then Tell Them How To Play
    print("The Computer Will Roll First")
else:
    print("If You Would Like To Play Enter 'Game'")
while True: # While Either Of The Players Do Not Have 3 Wins Iterate The Loop
    while(player_Wins < 3 and comp_Wins < 3):
      randomComp = random.choice(diceList) # Get A Random Number For The Dice
      print("The Number That The Computer Rolled Was",randomComp) # Tell The User What The Number Is For The Computer

      wannaPlay = str(input("Type 'Roll' To Roll The Dice:")) # Ask The User To Roll Their Dice
      if(wannaPlay != "Roll" or "roll"): # If The Answer Is Not This Then Tell Them How To Play It
        print("If You Want To Play Please Enter 'Roll'")
      randomPlayer = random.choice(diceList) # Get A Random Number For The User
      print("The Number That You Rolled Was",randomPlayer) #Print Their Number

      if(randomComp > randomPlayer): #If The 
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
    
    




