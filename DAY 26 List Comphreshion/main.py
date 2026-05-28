# TODO 1: Create a dict in this format {"A":"Alfa","B":"Bravo"}
import pandas
from pyseto import key

words_data = pandas.read_csv("nato_phonetic_alphabet.csv")
pandas.DataFrame(words_data)

new_dict = {row.Letter:row.Code_Word for (index,row) in words_data.iterrows()}

# TODO 2: Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()

new_list = [new_dict[letter] for letter in user_input]

print(new_list)