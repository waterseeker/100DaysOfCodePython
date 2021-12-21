import os
from art import logo


def clear():
    lambda: os.system("clear")


def next_bidder(is_bidding):
    run_again = input("Is there another bidder?\n").lower()
    while is_bidding:
        if run_again == "yes":
            clear()
            return
        elif run_again == "no":
            is_bidding = False
            return
        else:
            print(f"Sorry, I don't understand {run_again}. You have to choose \
    yes or no.")
            next_bidder(is_bidding)


print(logo)
bids = {}
bidding = True
while bidding:
    user_name = input("What is your name?\n")
    user_bid = int(input("What is your bid?\n"))
    bids[user_name] = user_bid
    next_bidder(bidding)
highest_bid = 0
highest_bidder = ""
for user in bids:
    if bids[user] > highest_bid:
        highest_bid = bids[user]
        highest_bidder = user
print(highest_bid, highest_bidder)
