
# Create a variable to store the size of the board. 
# I can use this to change the board later on.

size = 3

# Create a variable that tells the code the game is running.
# I made it a boolean so I can use False to turn it off later on.

rungame = True

# Create a variable to store the player's marking.

player = "X"

# Create a variable to store the board.
# In this variable, the board does a few things. I start with brackets to indicate that the board will be a list.
# Then I use a second set of brackets to create a list of lists. In the second set of brackets, I first create
# an empty string, then use a for loop to create (three in this case) different lists inside the main list (rows).
# I use another loop to create (three in this case) empty strings in each inner list (columns).
# The empty string at the beginning is what is placed in each index spot.

board = [["" for i in range(size)] for i in range(size)]

# Here I create a function to format and print the existing board.

def printboard(board):  
  
# I start out with a for loop. This is where I use len to iterate through the rows and columns of the board. 
# This len is used so no matter what size the board is the board will always work.
# The outer loop create a loop that will iterate through each row of the board.

  for i in range(len(board)):
    
# This inner loop iterats through each column in the current row. Again using len for the flexibiliy of 
#  changing the size of the board.

    for j in range(len(board[i])):
      
# Print each individual cell of the current board. This is done for each row due to the above for loop.
# end="" is used to prevent the print function from automatically adding a new line. This allows each
# item to be printed on the same line.

      print(board[i][j], end="")
      
# if the current column is less then size - 1 then do the following

      if j < size - 1:
        
# Print a pipe and then don't go to the next line. This is so when the inner loop runs again, it prints again
# on the same line. Then once it goes over size - 1, it stops printing as advised above.

        print(" | ", end="")
        
# Print a new line once the inner for loop is complete. This is because it is indented in alignment with the
# inner loop. So it is only used after the loop is complete.

    print()
    
# If the row is less then size -1 then

    if i < size - 1:
      
# Print a -. But I use multiplication to determine how many - I want. I tell the computer to do size * 3 - 3 first.
# Then make that many -'s. This is because based on the size of the board, this number will have to change as
# well. If I only have 3 lines and then change my board to a 12x12, it will look funny. 

        print("-" * (size * 3 - 3))
        
# Creat a Function to stor the player input

def playerinput(board):
  
# I am encapsulating this function in a try statement. This allows the code to catch errors and prevent it from crashing.
# In this case, it catches the ValueError exception.

        try:
          
# Created a variable called inrow. Take player input to determine which row they would like to place the X on.
# I also used an f-string. This is because my input includes both strings and variables. If I did not use an f-string,
# the computer would treat the variable as a string and just print out the words. For aesthetics, I also tell the computer
# to take input on a new line.

          inrow = int(input(f"what row do you pick?(1-{size})\n"))
          
# I do the same as up above but for a incol variable. This will take player input for what column they would like.

          incol = int(input(f"What collumn do you pick?(1-{size})\n"))
          
# I created an if statement. This if statement checks if both the incol input and the inrow input are less than or
# equal to size. If they are, the code moves on to the next line within the if statement.

          if incol <= size and inrow <= size:
            
# Since the if statement above is correct, I am now checking if there is anything in the spot the player is trying to use.
# I do this by checking if the spot on the board, indicated by the input from inrow and incol, is empty. If it is, then proceed.
            if board[inrow - 1][incol - 1] == "":
              
# Finally, since the above two if statements are true, I place the player (X) in that spot.
# I set the spot on the board indicated by row inrow - 1 and column incol - 1 (because the board starts at 0) to player (X).

                board[inrow - 1][incol - 1] = player
                
# If either of the if statements above is not true, then the code will jump to this line, skipping all the code before it starting at the if statments.

          else:
            
# Display in the console "That's outside of the board size." This prompts the user to try again since the game is in a while loop.

            print("Thats outside of the board size")
            
# This is where the try block from above is caught. The system tries the code, and if something goes wrong, instead of crashing,
# it goes here and catches the error. Depending on the error type, it handles it appropriately.
   
        except ValueError:
          
# Display in the console "That's not a number, so try again."

            print("Thats not a number so try again.")
        
# This while loop tells the computer to keep performing this action until it becomes false. 
# As of right now, rungame is set to True, so the loop never ends.          

while rungame:
  
# Execute the printboard(board) function from above.

  printboard(board)
  
# Also execute the playerinput(board) function from above after the printboard function.

  playerinput(board)
  
