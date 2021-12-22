import os
from art import logo


def bidding():
    user_name = input("What is your name?\n")
    user_bid = int(input("What is your bid?\n"))
    bids[user_name] = user_bid
    while True:
        run_again = input("Is there another bidder?\n").lower()
        if run_again == "no":
            break
        elif run_again == "yes":
            os.system('clear')
            return bidding()
        else:
            print(f"Sorry, I don't understand {run_again}. You have to choose \
yes or no.")
            continue


print(logo)
bids = {}
bidding()
highest_bid = 0
highest_bidder = ""
for user in bids:
    if bids[user] > highest_bid:
        highest_bid = bids[user]
        highest_bidder = user
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
