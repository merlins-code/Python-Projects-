
list = []

# ask user for data to enter

while True:
  data = input("What would you like to save")
  list.append(data)
  
# Do you have more data?

  go = input("Do you have more to enter? y/n: ")
  if go.lower() == "n":
      break
# Reprint list

print(list)
  
      
  



    

    
    








