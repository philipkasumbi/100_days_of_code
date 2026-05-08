
print()
def add(number1,number2):
    return number1 + number2

def subtract(number1,number2):
    return number1 - number2

def multiply(number1,number2):
    return number1 * number2

def divide(number1,number2):
    return number1 / number2


num1= int(input("Enter a first number: "))
num2= int(input("Enter another number: "))

operand = input("Choose an operand ' +(add), /(divide), *(multiply), -(subtract) ':  ")

def operands(operand):
    if operand == "+":
        result = (add(num1,num2))
        return result

    elif operand == "-":
        result = (subtract(num1,num2))
        return result

    elif operand == "*":
        result = (multiply(num1,num2))
        return result

    else:
        result = (divide(num1,num2))
        return result
result = operands(operand)
print(result)

user_continue = input("do you want to continue with the last result? yes or no:   ")
if user_continue == "yes":
    ask_number = int(input("Enter another number:  "))
    operand = input("Choose an operand ' +(add), /(divide), *(multiply), -(subtract) ':  ")
    if operand == "+":
        final = result + ask_number
        print(final)
    elif operand == "-":
        final = result + ask_number
        print(final)
    elif operand == "*":
        final = result + ask_number
        print(final)
    elif operand == "/":
        final = result + ask_number
        print(final)
    else:
        print("Enter a valid operator")
else:
    print(f"your result is {result}, feel free to start over again")

    
