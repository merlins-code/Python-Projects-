board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
player = "X"
gamerunning = True
winner = False

# Create the Board

def printboard(board):
  print(board[0] + " | " + board[1] + " | " + board[2])
  print("---------")
  print(board[3] + " | " + board[4] + " | " + board[5])
  print("---------")
  print(board[6] + " | " + board[7] + " | " + board[8])

# Get player inpute

def playerinput(board):

  try:
    inp = int(input("Select a Spot from 1 - 9.\n"))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp-1] = player
    else:
      print("No space for that.")
  except ValueError:
    print("Thats not a number, try again")
  

# Find out if they wone or if they tied

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
        
        
def tie(board):
    if "-" not in (board):
        global gamerunning
        printboard(board)
        print("Its a Tie!")
        gamerunning = False


def checkwin():
    if checkdown(board) or checkacross(board) or checkdiaganal(board):
        print(f"the winner is {winner}")
        global gamerunning
        gamerunning = False
    

#Switch Player


def Switchplayer():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"


# Run the Game

while gamerunning:
    printboard(board)
    playerinput(board)
    checkwin()
    tie(board)
    Switchplayer()
    
