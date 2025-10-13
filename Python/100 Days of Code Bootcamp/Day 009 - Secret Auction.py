import os

# clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def logo():
    print(r"""
          
                         ___________
                                  /
                          )_______(
                          |       |_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )       (
                         /_________\
                       .-------------.
                      /_______________\                   
""")
    print("\n\n")
    
# Create variables and dictionary

bids = {}
new_name = ""
new_bid = 0
auction_on = True
winner = ""
higest_bid = 0

# START program
while auction_on:
    clear()
    logo()
    new_name = input("What is your name?: ")
    new_bid = int(input("What is your bid?: $"))
    bids[new_name] = new_bid

    decision = input("Do you want to add another bidder? Type 'yes' or 'no': ").lower()
    
    while decision not in ["yes","no"]:
            decision = input("I did not understand that. Do you want to add another bidder? Type 'yes' or 'no': ").lower()

    if decision == "no":
        auction_on = False
    elif decision == "yes":
        auction_on = True

# Determine the highest bidder


for key, value in bids.items():
     bid_amount = bids[key]    
     if bid_amount > higest_bid:
        higest_bid = bid_amount
        winner = key


# Print highest bid
clear()
logo()
print(f"The winner is {winner} with a bid of ${higest_bid}.")
input("Press enter to continue...")