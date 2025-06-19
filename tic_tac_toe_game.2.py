
my_list = []


# I collect input from the user using the Input function. This then outputs a string.
# I use the int function to change the data type the string outputs into a integer.
# This is something that range can use because Range can not accept a string.



num_items = int(input("Enter the number of items:\n "))


# Then I use a for loop. This is used to creat a repeating event. 
# The range function specifies the number of times this for loop is performed.
# After this number of times the loop will break and move forward.

for i in range(num_items):

# I ask for input a second time. This time I dont specify a int.
# This is because my list can accept any kind of information such as strings integers or floats.
# Next i use a f string. This allows me to add two pices of information together without having 
# to concatenate. i in this f string is the polace in the for loop. The system always starts at
# zero. There for I add a + 1. This allows the number to acurate with what pice of data is being
# inputed into the list later on.

    item = input(f"Enter item {i+1}:\n ")

# I bring the (my_list) assigned statment down and by using .append I am able to add 
# data to the end of my list. I use the item input from before to tell this what to 
# put into the list. 
    my_list.append(item)

# I print the list that has ben created from above. Due to using the .append (varriable?) the
# list is printed out in the order of what was put in.

print(my_list)


