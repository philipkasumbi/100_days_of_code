# this program should print each number from 1 - 100 in turn 

# when the no is divisible by 3 instead of saying the number say FIZZ
# and when divisible by 5 should print BUZZ
# and if divisible by both 3 and 5 should print FizzBuzz

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)