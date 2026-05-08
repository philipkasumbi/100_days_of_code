# small pizza = $15
# medium pizza = $20
# large pizza = $25

# pepperoni for small pizza = +$2
# pepperoni for medium and large pizza = +$3
    
# extra cheese for any size pizza = +$1    

print("Welcome to pizza automatic order\n")

customers_name = input("Please enter your name? ")

print(f"Hello {customers_name} feel free to order some pizza with us ")

small_pizza = 15
medium_pizza = 20
large_pizza = 25
bill = 0

small_pepperoni_bill = 2
medium_pepperoni_bill = 3
large_pepperoni_bill = 3

cheese_bill = 1
pizza_size = input("What size of pizza would you like? S,M or L?  ")

if pizza_size == "S":
    bill = 15
    print(f"The small size costs ${small_pizza}")
    pepperoni = input("Would you like some pepperoni? Y or N  ")
    if pepperoni == "Y":
        bill += small_pepperoni_bill
        cheese = input("What about some cheese? Y or N  ")
        if cheese == "Y":
            bill += cheese_bill
            print(f"Your Final bill is {bill}")
        else:    
            print(f"Final bill is {bill}")
    else:
        print(f"Your bill is {bill}")  

elif pizza_size == "M":
    bill = 20
    print(f"The medium size costs ${medium_pizza}")
    pepperoni = input("Would you like some pepperoni? Y or N  ")
    if pepperoni == "Y":
        bill += medium_pepperoni_bill
        cheese = input("What about some cheese? Y or N  ")
        if cheese == "Y":
            bill += cheese_bill
            print(f"Your Final bill is {bill}")
        else:    
            print(f"Final bill is {bill}")

    else:
        print(f"Your bill is {bill}")  

elif pizza_size == "L":
    bill = 25
    print(f"The large size costs ${large_pizza}")
    pepperoni = input("Would you like some pepperoni? Y or N  ")
    if pepperoni == "Y":
        bill += large_pepperoni_bill
        cheese = input("What about some cheese? Y or N  ")
        if cheese == "Y":
            bill += cheese_bill
            print(f"Your Final bill is {bill}")
        else:    
            print(f"Final bill is {bill}")

    else:
        print(f"Your bill is ${bill}")    

else:
    print("You never ordered anything")

    


