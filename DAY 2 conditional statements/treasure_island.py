print("Welcome to the treasure island \n" \
"Your mission is to find the Treasure")

direction = input("Would you like to go left or right? type L for Left and R for right \n")

if direction == "L":
    choice = input("Would you like to wait or swim? W or S  ")

    if choice == "W":
        door =input("Which door would you like to get in? RED,BLUE or YELLOW    ")
        if door == "YELLOW":
            print("Hurray You won😂😊😎")
        else:
            print("sorry you came this far just to lose 🫥😂")


    else:
        print("oops Game over!!")

else:
    print("Game over!!, you lost too early 🤡🤭")    