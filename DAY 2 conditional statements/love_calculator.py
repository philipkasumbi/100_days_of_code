# take 2 peoples names
# check the number of times the letters in the word TRUE occurs
# check the number of times the the letters in the word LOVE occurs
# combine the numbers to make a two digit number

print("Welcome to the print calculator")
user1 = input("Please enter your name? ")
user2 = input("Please enter your name? ")

name = user1 +" " + user2

lowerstring_name = name.lower()

t = lowerstring_name.count("t")
r = lowerstring_name.count("r")
u = lowerstring_name.count("u")
e = lowerstring_name.count("e")

true = t+r+u+e

l = lowerstring_name.count("l")
o = lowerstring_name.count("o")
v = lowerstring_name.count("v")
e = lowerstring_name.count("e")

love = l+o+v+e


print(f"The probability of falling in love is {true}{love}%")

