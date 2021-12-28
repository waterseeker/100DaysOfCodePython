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


def show_player_hand():
    """Prints out the player's hand."""
    print(f"Your cards: {players_hand}, current score: {sum(players_hand)}")


def show_dealer_hand():
    """Prints out the dealer's hand. Keeps the second card hidden unless it's
       the end of the game."""
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
