# create a function called greet
# write three print statements inside the function 
# call the function and run the code 


# simple function
def greet():
    print("hello there")
    print("hello there")
    print("hello there")

greet()


# function that allows for inputs

def greet_with_name(name):
    print(f"hello {name}, how are you doing today")

greet_with_name("philip")

# function with more than one input 

def greet_with(name,location):
    print(f"hello {name}, how are you doing today?")
    print(f"How's the weather around {location}?")

greet_with("kasumbi","Kitui")



