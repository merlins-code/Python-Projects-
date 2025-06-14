board = ["-","-","-",
         "-","-","-",
         "-","-","-"]


# Create the Board

print(board[0] + " | " + board[1] + " | " + board[2])
print("---------")
print(board[3] + " | " + board[4] + " | " + board[5])
print("---------")
print(board[6] + " | " + board[7] + " | " + board[8])

# Get player X inpute
while True:
    try:
        inp = int(input("Player X select a number from 1 - 9. press 0 end the game.:\n"))
        if inp >= 1 and inp <= 9 and board[inp - 1]:
            break
        elif inp <= -1 and inp >= 10:
            print("No space for that number.")
    except ValueError:
        print("Thats not a number, try again")
        
print("great job!")
    
    
    

        




# Find out if they wone or if they tied

#Get Player O inpute

# Find out if they wone or if they tied