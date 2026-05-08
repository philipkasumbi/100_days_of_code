# weeks in a year = 52
# days in a year 365

# if i were to live up to 90 years 
# what time is left

Total_weeks = 90 * 52
Total_days = 90 * 365

user_name = input("Please enter you name\n")
user_age = int(input("Enter your current age\n"))

remaining_years = 90 - user_age

remaining_weeks = remaining_years * 52
remaining_days = remaining_years * 365
remaining_months = remaining_years * 12

print(f"Hi there {user_name} you have {remaining_days} days, {remaining_weeks} weeks and {remaining_months} months left")