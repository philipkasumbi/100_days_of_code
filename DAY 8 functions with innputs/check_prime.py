print("welcome to a prime number ")
number = int(input("Enter a random number to check if its a prime number or not ....?\n"))

def isPrime(number):
    if number<= 1:
        print(f"{number} is not a prime number") 
    
    for i in range (2,number):
        if number % i == 0:
            return False

    return True    

print(isPrime(number))