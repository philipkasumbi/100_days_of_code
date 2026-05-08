# # write a program to check a number if its odd or even 
#  a number is even if when you divide itself by 2 the remainder is zero and
# a number is odd if when you divide itself by 2 the remainder is 1  

rand_num = int(input("Please enter a random number "))

if rand_num % 2 == 0:
    print("The number you entered is even")
else:
    print("The number you have entered is odd")
