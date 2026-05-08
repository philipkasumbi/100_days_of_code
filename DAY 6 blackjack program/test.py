import random
import sys

logo = """
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/           
"""

win = """
 __   __           __        ___       _ 
 \ \ / /__  _   _  \ \      / (_)_ __ | |
  \ V / _ \| | | |  \ \ /\ / /| | '_ \| |
   | | (_) | |_| |   \ V  V / | | | | |_|
   |_|\___/ \__,_|    \_/\_/  |_|_| |_(_)
"""

lose = """
 __   __            _                   _ 
 \ \ / /__  _   _  | |    ___  ___  ___| |
  \ V / _ \| | | | | |   / _ \/ __|/ _ \ |
   | | (_) | |_| | | |__| (_) \__ \  __/_|
   |_|\___/ \__,_| |_____\___/|___/\___(_)
"""

draw = """
  ____  ____      ___        ___ _ 
 |  _ \|  _ \    / \ \      / / | |
 | | | | |_) |  / _ \ \ /\ / /| | |
 | |_| |  _ <  / ___ \ V  V / |_|_|
 |____/|_| \_\/_/   \_\_/\_/  (_|_)
"""

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

players_total = []
computer_total = []

player = random.sample(cards,2)
computer = random.sample(cards,2)

print(f"Your cards are {player}")
print(f"Computers cards are {computer[0]} and an 'Hidden card'")

players_total.append(sum(player))
computer_total.append(sum(computer))

if sum(player) == 21:
    print("You win")
    print(win)
    sys.exit()
elif sum(computer) == 21:
    print("You Lose to the computer")
    print(lose)
    sys.exit()
  

def anotherComputerCard():
    another_card = random.choice(cards)
    if another_card == 11 and sum(computer_total) > 10:
        another_card = 1
        computer_total.append(another_card)
    else:
        computer_total.append(another_card)

def anotherPlayerCard():
    another_card = random.choice(cards)
    if another_card == 11 and sum(players_total) > 10:
        another_card = 1
        players_total.append(another_card)
    else:
        players_total.append(another_card)

while sum(players_total) < 21:
    next_card = input("do you take another card or stop? yes or no:  ").lower()
    if next_card == "yes":
          anotherPlayerCard()
    else:
        break
while sum(computer_total) < 17:
    anotherComputerCard()



if sum(players_total) == 21:
    print("You win")
    print(win)
elif sum(computer_total) == 21:
    print("You Lose to the computer")
    print(lose)
elif sum(players_total) >21:
    print("It's a BUST\n"
    "You lost the game")
elif sum(computer_total) >21:
    print("It's a BUST for the computer\n"
    "You win the game")
    print(win)
elif sum(players_total) > sum(computer_total) and sum(players_total) <=21 :
    print("You won the game!!")
    print(win)
elif sum(computer_total) > sum(players_total) and sum(computer_total) <=21 :
    print("Computer wins")
    print(lose)
elif sum(computer_total) == sum(players_total):
    print("It's a draw!!")
    print(draw)

print(f"Your total is {sum(players_total)}")
print(f"computer's total is {sum(computer_total)}")

print(players_total)
print(computer_total)
