# ############## Blackjack Project #####################
# ############## Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
from art import logo


def start_game():
    """Returns True if player enters y, False if n, and calls itself if the
       input is neither."""
    play_game = input("Do you want to play a game of blackjack?\n")
    if play_game == 'y':
        return True
    elif play_game == 'n':
        return False
    else:
        print("Sorry, I don't know what that means. Please choose 'y' or 'n'.")
        start_game()


play_game = start_game()
while play_game:
    print(logo)
    # setting play_game to False to break the loop
    play_game = False
