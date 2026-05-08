print("Welcome to the Tip Calculator")
total_bill = float(input ("What was the total bill in dollars?\n "))
percentage_tip = int(input("What Percentage tip would you like to give? 10, 12 or 15?\n "))
split_number =float(input("How many people to split the bill?\n "))

tip_amount = total_bill * (percentage_tip / 100)
new_total_bill = total_bill + tip_amount

bill_share = new_total_bill / split_number

rounded_bill_share = round(bill_share,2)


print(f"Each Person should pay: ${rounded_bill_share}")