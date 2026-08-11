total_bill = float(input("Welcome to the tip calculator! \nWhat was your total bill? $"))

tip_percentage =  int(input("How much would you like to give? 10, 12 or 15? %"))

split = int(input("How many people to split the bill? "))




print(f"This is how much each person should pay for the bill: ${total_bill * (tip_percentage / 100) / split}")

