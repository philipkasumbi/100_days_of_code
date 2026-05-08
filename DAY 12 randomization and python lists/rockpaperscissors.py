
# Rock Paper Scissors ASCII Art
import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")


paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
Scissors =("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

users_choice = input("choose either rock,paper or scissors \n")

if users_choice == "rock":
    print(f"You chose Rock {rock}")
elif users_choice == "paper":
    print(f"You chose Paper {paper}")
elif users_choice == "scissors":
    print(f"You chose Scissors {Scissors}")
else:
    print("Choose between rock,paper and scissors")



computer_choice = random.choice(["rock","paper","scissors"])

if computer_choice == "rock":
    print(f"Computer chose Rock{rock}")
elif computer_choice == "paper":
    print(f"Computer chose Paper{paper}")
else:
    print(f"Computer chose Scissors{Scissors}\n \n \n")

# game rules - rock beats scissors
#            - scissors beats paper
#            - paper beats rock 

if users_choice == "rock" and computer_choice == "scissors":
    print("you beat the computer")
elif users_choice == "scissors" and computer_choice == "paper":
    print("you beat the computer")
elif users_choice == "paper" and computer_choice == "rock":
    print("you beat the computer")
elif users_choice == computer_choice:
    print("oops its a TIE")
else:
    print("sorry you lose to computer")
