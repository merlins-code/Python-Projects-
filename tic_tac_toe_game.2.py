size = 4
player = "X"
rungame = True

board = [["" for _ in range(size)] for _ in range(size)]

def printboard(board):
    for i in range(size):
        row_display = ""
        for j in range(size):
            cell = board[i][j] if board[i][j] != "" else " "
            row_display += f" {cell} "
            if j < size - 1:
                row_display += "|"
        print(row_display)
        if i < size - 1:
            print("-" * (size * 3 + (size - 1)))

def playerinput(board):   
    try:
        inrow = int(input(f"what row do you pick? (1-{size})\n"))
        incol = int(input(f"What column do you pick? (1-{size})\n"))
        if 1 <= inrow <= size and 1 <= incol <= size:
            if board[inrow - 1][incol - 1] == "":
                board[inrow - 1][incol - 1] = player
            else:
                print("That spot is already taken.")
        else:
            print("That's outside of the board size")
    except ValueError:
        print("That's not a number so try again.")


while rungame:
    printboard(board)
    playerinput(board)
