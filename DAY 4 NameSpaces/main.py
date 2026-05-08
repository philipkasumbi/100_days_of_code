import random

print("WELCOME TO THE NUMBER GUESSING GAME!!")
print("I'm thinking of a number between 0 and 100 \n" \
"and your job is to guess what number it is...")

computer_number = random.randint(0,100)

users_choice = input("What level do you want to play? easy or hard?: ").lower()

easy_level_attempts = 10
hard_level_attempts = 5

def easyLevel():
    global easy_level_attempts
    while easy_level_attempts:
        print(f"You have {easy_level_attempts} attempts left.....")
        user = int(input("Guess the number: "))
        if user > computer_number:
            print("Your Guess is too high")
        elif user < computer_number:
            print("Your Guess is too low")
        else:
            print(f"You Got it in {easy_level_attempts} attempts!!! The answer was {computer_number}")
            return 0
        
        easy_level_attempts -= 1

    print("You've used all your attempts,, sorry")    

def hardLevel():
    global hard_level_attempts
    while hard_level_attempts:
        print(f"You have {hard_level_attempts} attempts left.....")
        user = int(input("Guess the number: "))
        if user > computer_number:
            print("Your Guess is too high")
        elif user < computer_number:
            print("Your Guess is too low")
        else:
            print(f"You Got it in {hard_level_attempts} attempts !!! The answer was {computer_number}")
            return 0
           
        hard_level_attempts -= 1
    print("You've used all your attempts,, sorry")    

if users_choice == "easy":
    easyLevel()
elif users_choice == "hard":
    hardLevel()
else:
    print("Wrong input, enter either easy or hard")

