# Blind Auction Program

from replit import clear
from art import logo

print(logo)
print("Welcome to the silent auction!")

# Input person's bid and insert into a dictionary:
bid_dictionary = {}

def make_bid():
    name = input("What is your name? \n")
    bid = input("What is your bid? \n")
    bid_dictionary[name] = bid

make_bid()

# Ask if there is another person and loop until everyone has bid:

another_person = True
while another_person == True:
    bid_on = input("Is there someone else bidding? (Type 'yes' or 'no'):\n")
    if bid_on == "yes":
        another_person = True
        clear()
        make_bid()
    elif bid_on == "no":
        another_person = False
    else:
        print("Invalid entry: type 'yes' or 'no'.\n")

# Compare bids and print out winner's bid:

highest_bid = 0
winner = ""

for bidder in bid_dictionary:
    bid_amount = int(bid_dictionary[bidder])
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder

print(f"{winner} won the auction with a bid of ${highest_bid}")