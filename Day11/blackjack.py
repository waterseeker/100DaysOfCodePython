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


def score_hand(hand):
    """Takes in a hand array and returns the best score possible with the
       given cards."""

    # all aces are ones, then add 10 for one to count as 11
    if 11 in hand:
        score_with_ace_as_11 = sum([card if card != 11 else 1
                                    for card in hand]) + 10
    else:
        score_with_ace_as_11 = 0
    # all aces are ones
    score_with_ace_as_1 = sum([card if card != 11 else 1 for card in hand])
    scores = [score_with_ace_as_11, score_with_ace_as_1]
    if score_with_ace_as_11 > 21 and score_with_ace_as_1 > 21:
        return min(scores)
    else:
        return max(scores)


def show_hands():
    """Prints out the player's hand and the first card of the dealer's hand."""
    print(f"Your cards: {players_hand}, current score: \
{score_hand(players_hand)}")
    print(f"Computer's first card: {dealers_hand[0]}")


play_game = start_game()
while play_game:
    print(logo)
    draw_card(dealers_hand)
    draw_card(dealers_hand)
    draw_card(players_hand)
    draw_card(players_hand)
    show_hands()
    if score_hand(dealers_hand) == 21 and score_hand(players_hand) != 21:
        print("Dealer has blackjack!\n You lose :(")
    # setting play_game to False to break the loop
    play_game = False
