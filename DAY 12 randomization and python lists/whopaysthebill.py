import random

seed_test = int(input("Create a seed number  "))
random.seed(seed_test)

# split string method 
nameasCSV = input("Give everybody's name, separated by a comma \n")
names = nameasCSV.split(",")

# choose a random person 
rand_person = random.choice(names)
print(f"{rand_person} is going to pay the bill")