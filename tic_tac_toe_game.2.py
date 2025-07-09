

size = 3
rungame = True
player = "X"
board = [["" for i in range(size)] for i in range(size)]

def printboard(board):  
  for i in range(len(board)):
    for j in range(len(board[i])):
      print(board[i][j], end="")
      if j < size - 1:
        print(" | ", end="")
    print()
    if i < size - 1:
        print("-" * (size * 3 - 3))
      
def playerinput(board):
        try:
          inrow = int(input("what row do you pick?\n"))
          incol = int(input("What collumn do you pick?\n"))
          if incol <= size and inrow <= size:
            if board[inrow - 1][incol - 1] == "":
                board[inrow - 1][incol - 1] = player
          else:
            print("Thats outside of the board size")
        except ValueError:
            print("Thats not a number so try again.")
        
            

while rungame:
  printboard(board)
  playerinput(board)
  
