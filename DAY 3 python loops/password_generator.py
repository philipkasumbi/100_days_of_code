import string
import random

alphabet_list = list(string.ascii_letters)
digits = list(string.digits)
symbols = list(string.punctuation)

print("Welcome to my pass generator")
pass_letters = int(input("How many letters would you like your password?\n"))
pass_symbols = int(input("How many symbols whould you like? \n"))
pass_numbers = int(input("How many number would you like you password? \n"))


rand_letters = random.sample(alphabet_list,pass_letters)
rand_symbols = random.sample(symbols,pass_symbols)
rand_digits = random.sample(digits,pass_numbers)

all_chars = rand_letters+rand_symbols+rand_digits

random.shuffle(all_chars)

password = ''.join(all_chars)



print(password)



