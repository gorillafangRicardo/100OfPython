logo = r''' ______
|_,.,--\
   ||
   ||
   ##
   ##'''

bidder = {}

def add_bidder():
    person = input("Whats your name?: ")
    bid = int(input("Whats your bid?: "))

    bidder[person] = bid
    multiple_bidders = input("You want to add more bidders? Y/N?: ").lower()

    if multiple_bidders == 'y':
        print("\n" * 100)
        add_bidder()
    else:
        highest_bidder = max(bidder, key=bidder.get)
        print("chaumafaker")
        print(f"The winner is: {highest_bidder}!")
        
        
        
        
add_bidder()


# highest_value = max(my_dict.values())