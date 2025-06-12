# start with a number

try:
    number = int(input("Tell me a number and I will tell you if it's even or odd:\n"))
except ValueError:
    print("Thats not a number. Try again.")

    


# Find out if its even or odd

if number % 2 == 0:
    print("Even")
else:
    print("odd")
