"""Blackjack game"""
import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

random.shuffle(cards)
computer = random.sample(cards,2)
player = random.sample(cards,2)


player_score = sum(player)
Dealer_score = sum(computer)

if player_score == 21:
    print ("You win")
elif Dealer_score == 21:
    print("You lose to the dealer")
else:
    second_draw = input("do you need any other card or stop?: ")
    if second_draw == "yes":
        second_card = random.choice(cards)
        player.append(second_card)
        if sum(player) > sum(computer):
            print(sum(player))
            print("You win")
        else:
            print("computer wins")


print(f"The dealer cards are {computer[0]} and {computer[1]}")
print(f"your cards are {player[0]} and {player[1]}")