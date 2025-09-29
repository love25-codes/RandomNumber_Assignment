import random

x = 1
while True:
    my_number = random.randint(0, 100)  # generate random number between 0-100
    
    try:
        user_number = int(input("Guess any number between 0 - 100: "))
    except ValueError:
        print("Please enter a valid number!")
        continue  
    
    if user_number == my_number:
        print("Number GUESSED correct")
    elif user_number > my_number:
        print("Number too large")
    else:
        print("Number too small")

    print("My number is", my_number)

    try:
        y = int(input("Press 1 to continue and 0 to exit: "))
    except ValueError:
        print("Invalid input. Exiting...")
        break

    if y != 1:
        print("BYE")
        break  

    print()
    x += 1
