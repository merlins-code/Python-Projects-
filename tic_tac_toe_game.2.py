board = []
size = 3
rungame = True

def printboard(board):
  for row in range(size):
    board.append([])
    for col in range(size):        
        board[row].append("")
        
  for i in range(len(board)):
    for j in range(len(board[i])):
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
            print(f"you picked\n{inrow}:{incol}")
          else:
            print("Thats outside of the board size")
        except ValueError:
            print("Thats not a number so try again.")
            
printboard(board)
playerinput(board)