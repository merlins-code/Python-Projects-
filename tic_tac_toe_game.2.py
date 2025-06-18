
mylist =[]

# Ask for how manny objects are in the list

number = int(input("how manny Items do you have"))

#the for loop creates something that repeats
# This stors the for operation in I
# Then it sets the rang of objects that are in the aray
# This range comes from the input above

for i in range(number):
    
    #this allows the user to input the ogject at that space
    # then i+1 puts the number in the current i and then moves forward one spot

    item = input(f"Enter item{i+1}:\n")
    
    # this takes my item and adds it to the end of my list
    
    mylist.append(item)
    
    # this prints the current list once the loop is done
    
print(mylist)
      
  



    

    
    








