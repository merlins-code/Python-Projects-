board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
playerx = "X"
gamerunning = True
winner = False

# Create the Board

def printboard(board):
  print(board[0] + " | " + board[1] + " | " + board[2])
  print("---------")
  print(board[3] + " | " + board[4] + " | " + board[5])
  print("---------")
  print(board[6] + " | " + board[7] + " | " + board[8])

# Get player X inpute

def playerinput(board):

  try:
    inp = int(input("Player X select a number from 1 - 9.\n"))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp-1] = playerx
    else:
      print("No space for that.")
  except ValueError:
    print("Thats not a number, try again")
  

# Find out if they wone or if they tied

def checkacross(board):
    global winner
    if board[0] == board[1] == board[2] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] != "-":
        winner = board[6]
        return True
        
def checkdown(board):
    global winner
    if board(0) == board(3) == board(6) != "-":
        winner = board(0)
        return True
    elif board(1) == board(4) == board(7) != "-":
        winner = board(0)
        return True
    elif board(2) == board(5) == board(8) != "-":
        winner = board(0)
        return True
        
def checkdiaganal(board):
    global winner
    if board(0) == board(4) == board(8) != "-":
        winner = board(0)
        return True
    elif board(2) == board(4) == board(6) != "-":
        winner = board(0)
        return True
        
def tie(board):
    if "-" not in (board):
        global gamerunning
        printboard(board)
        print("Its a Tie!")
        gamerunning = False

#Get Player O inpute

# Find out if they wone or if they tied




# Run the game

while True:
    printboard(board)
    playerinput(board)
    if checkacross(board) is True:
        print("X wins!")
        break
    elif checkdown(board) is True:
        print("X Wins!")
        break
    elif checkdiaganal(board) is True:
        print("X Wins!=")

    
    





























