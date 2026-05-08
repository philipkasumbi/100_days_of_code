# normal year = 365 days 
# leap year = 366 days 
#  for a leap year, on every year that is evenly divisible by 4 
# except every year that is divisible by 100
# unless the year the year is also divisible by 400

print("Welcome to this program\n" \
"it checks whether an year is a leap one\n" \
"these are the conditons for it to be a leap year\n" \
"first step:The year should be evenly divisible by 4(if not its automatically not a leap year)\n" \
"second step: it checks whether the year is divisible by 100 or not(if it is not, then its directly a leap one but if it is we check the next step)\n" \
"Third step: The year should be divisible by 400 for it to be a leap year\n")
rand_year = int(input("Enter a random year to check whether is a leap year or not?"))


if rand_year % 4 == 0:
    print("its a leap year but wait a min....")
    if rand_year % 100 ==0:
        print("Its still a leap year but wait...")
        if rand_year % 400 == 0:
            print("Finally its a leap year")
        else:
            print("It failed the last test so its not a leap year")    
    else:
        print("Its leap year maan..!")
else:
    print("It is not a leap year")