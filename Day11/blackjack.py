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
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
players_hand = []
dealers_hand = []
player_busts = False
dealer_busts = False
player_stands = False
dealer_stands = False


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


def draw_card(hand):
    """Adds 1 card to the hand."""
    hand.append(random.choice(cards))

# You've most likely got a method that evaluates a blackjack hand value.
# Always value aces at one point. If a hand contains an ace, compute a hard
# value (all aces are ones, +10) and a soft value (all aces ones).

# If the hard value is not a bust, return the hard value. If the hard value is
# a bust, return the soft value.


def evaluate_hand(hand):
    """Takes in a hand array and returns the sum, 'blackjack' if it's blackjack
       and 'bust' if it's a bust."""
    # all aces are ones, +10
    value_with_ace_as_11 = sum(hand)
    # all aces are ones
    value_with_ace_as_1 = sum(hand)
    return value_with_11


def show_hands():
    """Prints out the player's hand and the first card of the dealer's hand."""
    print(f"Your cards: {players_hand}, current score: \
{evaluate_hand(players_hand)}")
    print(f"Computer's first card: {dealers_hand[0]}")


play_game = start_game()
while play_game:
    print(logo)
    draw_card(dealers_hand)
    draw_card(dealers_hand)
    draw_card(players_hand)
    draw_card(players_hand)
    show_player_hand()
    show_dealer_hand()
    # setting play_game to False to break the loop
    play_game = False
