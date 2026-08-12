print("Welcome to python pizza mafarker")

size = input("What size do you want your pizza? S, M or L? ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "s":
    bill =  15
    if pepperoni == "y":
        bill += 2
elif size == "m":
    bill = 20
    if pepperoni == "y":
        bill += 3 
else: 
    bill = 25
    if pepperoni == "y":
        bill += 3 

if extra_cheese == "y":
    bill += 1

print(f"Your total is: ${bill}.")