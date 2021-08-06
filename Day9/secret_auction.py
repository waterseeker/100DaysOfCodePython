# Print the logo
# The program asks for a user name and a bid on an item.
# The program asks if there is another bidder after each person is done.
# Store names and bids in a dictionary.
# Print out the winning bidder and bid after everyone has bid.
from art import logo
from os import system

# function to clear the console when there is a new bidder
def clear():
    _ = system('clear')

def secret_auction():
    print(logo)
    print('Welcome to the secret auction program.')
    bids = {}
    while True:
        user_name = input('What is your name?: ')
        bid = input("What's your bid?: $")
        bids[user_name] = bid
        next_user = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        if next_user == 'no':
            bid_values = bids.values()
            highest_bid = max(bid_values)
            index_of_highest_bid = list(bids.values()).index(highest_bid)
            highest_bidder = list(bids.keys())[index_of_highest_bid]
            print(f'The winner is {highest_bidder} with a bid of ${highest_bid}.')
            break
        elif next_user == 'yes':
            clear()
            continue    

secret_auction()        