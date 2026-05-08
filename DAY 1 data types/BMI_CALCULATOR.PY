# BMI = WEIGHT/HEIGHT SQUARED 
name = input("Please Enter your name\n")
weight = float(input("Enter your weight in kilograms\n"))
height = float(input("Enter your height in meters\n"))
height_squared = height * height

BMI = weight/height_squared

print(f"hello {name} your body mass index is {BMI}")

if BMI < 18.5:
    print("You are underweight")
if 18.5 < BMI < 24.9:
    print("You have an healthy weight")
if 25.0 < BMI < 29.9:
    print("You are Overweight")
else:
    print("You are obese!!")
