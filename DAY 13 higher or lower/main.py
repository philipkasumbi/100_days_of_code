from data import countries
from art import vs
import random

game_to_continue = True
score = 0

# pick country A and B
countryA = random.choice(countries)
countryB = random.choice(countries)


while game_to_continue:
    print(f"country A : {countryA['name']}")
    print(vs)
    print(f"country B : {countryB['name']}")

    user_choice= input("Which of the two countries has the largest population? A or B?: ").upper()

    # get correct answer
    if countryA['population'] > countryB['population']:
        correct_answer = 'A'
    else:
        correct_answer = 'B'

   
    if user_choice == correct_answer:
        score += 1
        print(f"Correct✅, your score is: {score}")
        countryA = countryB
        countryB = random.choice(countries)
    else:
        print(f"❌ Wrong!! you  final score is: {score}")
        game_to_continue = False

