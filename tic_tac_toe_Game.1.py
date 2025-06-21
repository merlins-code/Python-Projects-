
# These are my starting varibles I use to refrence data later on in the code.

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
player = "X"
gamerunning = True
winner = False

# I First Create the board. I creat this with multiple print statments.
# I use one print statemtn per line. This allows me to draw the board.
# All of the spaces are useing the variable board with an assosiated number to represent
# the placment with in the list that board represents. Then I use a pipe and
#  concatination for the vertical lines.
# This is all held within a def that I can call later to run that section of code.

def printboard(board):
  print(board[0] + " | " + board[1] + " | " + board[2])
  print("---------")
  print(board[3] + " | " + board[4] + " | " + board[5])
  print("---------")
  print(board[6] + " | " + board[7] + " | " + board[8])

# Next I collect input from the user. inp is the variable I save the Input function in.
# This input spits out a string so I convert that string into a Integer. This is usful
# so I can do math. Then I use a if statment to give the code sopmething to do if a 
# sertain input is given. I say if the variable int is larger or equal to 1
# but smaller or equal to 9 then a certain spot on the list equels plarer. Player represents 
# X so a X is placed at that spot. While making sure its larger then 1 and smaller then 9 I 
# also want to make sure that you cant change a space once it has been played on.
# This is done with the math. Computers start at 0 and we start at 1 so I subtract 1 from the 
# inp to get a accurate spot number. As well == -, this makes sure no one has played
# in this spot yet because it still has a - in it. 

def playerinput(board):

  try:
    inp = int(input("Select a Spot from 1 - 9.\n"))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp-1] = player
    
 # Else is used because only 9 spots exist on the board. If someone gives another number
 # then 1-9 it can not be places. I have the code spit out a statment letting them know.
 # Finally I use the Except function to Catch any strings that are put in.
 # Due to me needing a integer, I dont want the game to crash if I recieve something 
 # that can not math. so I print out a statment for this telling the user.   
    
    
    else:
      print("No space for that.")
  except ValueError:
    print("Thats not a number, try again")
  

# Find out if they wone or if they tied. The Check across, down, and diaganoal are all
# the same. I first use def to define the function name asociated to the variable board.
# Then I use global to change what the variable winner represents. As of rite now it is
# false so I want it to be True to odetemin the winner. I use If and elif statments
# to determin the ways to win in each catagorie. I make sure that each list item slot 
# in the winning row is the same and not a -. I do this by using the == to say they have 
# to be exactly the same and the != to say not equat to  -. Then I let it tell the user who the 
# winner is be printing the simbol from the beginning slot of that row. Finally if this if or
# elif statment is true I return True. This changes the winner variables boolion from False to
# True.

def checkacross(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
        
def checkdown(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
        
def checkdiaganal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

# The tie function is to determin that no set of 3 X's or O's are on the board. I do this 
# by taking out -. If I take that out then that means that all the spaces have a x or o
# so the board is full. so I use if to say if - is not in the variable board then
# do the rest. So I stop the game at this point by changing the gamerunning global
# variable to False. This stops the while loop at the end from running and closes the game.
# Then I show the board again and let the user know that this has happened.       
        
def tie(board):
    if "-" not in (board):
        global gamerunning
        printboard(board)
        print("Its a Tie!")
        gamerunning = False


# This function checks if anyone won the game. I use the iff statment to check all
# three gme winning types at the same time using or. Then if any of them come back as 
# true I print the winners letter X or O. I do this by using a f string to 
# cocatinate the string and the variable. The winner at this point is a variable holding
# a spot that was placed in the winner def. That is where it determins what 
# to print. Next i tap into the global variable gamerunning anfd turn it to false
# to shut down the while loop and the game stops.

def checkwin():
    if checkdown(board) or checkacross(board) or checkdiaganal(board):
        print(f"the winner is {winner}")
        global gamerunning
        gamerunning = False
    

# Switching players was easier then I thought. I taped into the global variable player
# and said if player is X then lets make that O and anything else ( if its O ) then
# turn it back to X.



def Switchplayer():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"


# Here I took each funtion I created and ran them in order o opperation.
# I stated by displaying the board. Then asking the player what they would like
# to do. Then check for the win to see if the game needs to be turned off or not.
# Then tie for the same reason. Then if those do not turn off the game then switch
# Players and keep going untill one returns false to the gamerunning variable to 
# stop the while loop..

while gamerunning:
    printboard(board)
    playerinput(board)
    checkwin()
    tie(board)
    Switchplayer()
    
