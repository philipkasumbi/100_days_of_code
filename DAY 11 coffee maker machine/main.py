resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 300,
    "money": 0
}

menu = [
    {
        "name": "espresso",
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "price": 1.5
    },

    {
        "name": "latte",
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "price": 2.5
    },

    {
        "name": "cappuccino",
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "price": 3.0
    }
]
Penny = 0.01
Nickel = 0.05
Dime = 0.10
Quarter = 0.25


    # TODO Print resources of all coffee machine resources
def report():
    print(f" Water: {resources['water']}ml")
    print(f" Milk: {resources['milk']}ml")
    print(f" Coffee: {resources['coffee']}ml")
    print(f" Money: ${resources['money']}")

def ask_coins():

    print("Please enter coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total = (Quarter * quarters) + (Dime * dimes) + (Nickel * nickels) + (Penny * pennies)
    return total


def resourcefulness(drink):
    if drink == "espresso":
        resources["water"] = resources["water"] - menu[0]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - menu[0]["ingredients"]["coffee"]
        resources["money"] = resources["money"] + menu[0]["price"]


    elif drink == "latte":
        resources["water"] = resources["water"] - menu[1]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - menu[1]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - menu[1]["ingredients"]["coffee"]
        resources["money"] = resources["money"] + menu[1]["price"]

    elif drink == "cappuccino":
        resources["water"] = resources["water"] - menu[2]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - menu[2]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - menu[2]["ingredients"]["coffee"]
        resources["money"] = resources["money"] + menu[2]["price"]


machine_on = True

while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "report":
        report()

    elif user_choice == "espresso":
        if resources["water"] >= menu[0]["ingredients"]["water"] and resources["coffee"] >= menu[0]["ingredients"]["coffee"]:
            total =ask_coins()

            balance = total - menu[0]['price']
            rounded_balance = round(balance, 2)


            if rounded_balance >= 0:
                if rounded_balance > 0:
                    print(f"Here is your ${rounded_balance} in change.")

                print("Here is your espresso ☕ Enjoy")
                resourcefulness(user_choice)

            else:
                print("Sorry that's not enough money. Money refunded.")

        else:
            print("something is not enough")


    elif user_choice == "latte":
        if resources["water"] >= menu[1]["ingredients"]["water"] and resources["coffee"] >= menu[1]["ingredients"]["coffee"] and resources["milk"] >= menu[1]["ingredients"]["milk"]:
            total =ask_coins()

            balance = total - menu[1]['price']
            rounded_balance = round(balance, 2)

            if rounded_balance >= 0:
                if rounded_balance > 0:
                    print(f"Here is your ${rounded_balance} in change.")

                print("Here is your latte ☕ Enjoy")
                resourcefulness(user_choice)



            else:
                print("Sorry that's not enough money. Money refunded.")

        else:
            print("something is not enough")
    elif user_choice == "cappuccino":
        if resources["water"] >= menu[2]["ingredients"]["water"] and resources["coffee"] >= menu[2]["ingredients"]["coffee"] and resources["milk"] >= menu[2]["ingredients"]["milk"]:
            total =ask_coins()

            balance = total - menu[2]['price']
            rounded_balance = round(balance, 2)

            if rounded_balance >= 0:
                if rounded_balance > 0:
                    print(f"Here is your ${rounded_balance} in change.")

                print("Here is your cappuccino ☕ Enjoy")
                resourcefulness(user_choice)
            else:
                print("Sorry that's not enough money. Money refunded.")

        else:
            print("something is not enough")

    elif user_choice == "off":
        print("Shutting down..............")
        machine_on = False

    else:
        print("Invalid choice")

