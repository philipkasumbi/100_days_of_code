from replit import clear

print("welcome to the secret auction program")

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
my_dict ={}

def callForBidder():
    user = input("Whats your name?: ")
    bid = int(input("Whats your bid?: "))
    Other_bidders = input("Are there any other bidders? yes or no?: ") 
    result = {user:bid}
    my_dict.update(result)
    if Other_bidders == "yes":
        clear()
        callForBidder()
    
 

take = input("Do you want to play this game? Type 'Y' for Yes and 'N' for No:  ")

if take=="Y":
    callForBidder()
    max_bid =max(my_dict,key=my_dict.get)
    print(f"congratulation {max_bid} you won the bid")

else:
    exit
