while True:
    try:
        number = int(input("Tell me a number or type 0 to exit:\n"))
        if number == 0:
            break
        elif number % 2 == 0:
            print("Even")
        else:
            print("odd")
    except ValueError:
        print("Thats not a number. Try again")


print("Thanks for playing!")