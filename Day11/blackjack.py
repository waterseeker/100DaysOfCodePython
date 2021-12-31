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
player_score = 0
dealer_score = 0
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

    scores = []
    if 11 in hand:
        # all aces are ones, then add 10 for one to count as 11
        score_with_ace_as_11 = sum([card if card != 11 else 1
                                    for card in hand]) + 10
        scores.append(score_with_ace_as_11)
        # all aces are ones
        score_with_ace_as_1 = sum([card if card != 11 else 1
                                   for card in hand])
        scores.append(score_with_ace_as_1)
    else:
        score_with_no_aces = sum([card for card in hand])
        scores.append(score_with_no_aces)
    if 21 in scores:
        return 21
    else:
        filtered_scores = filter(lambda score: score < 21, scores)
        filtered_score_list = list(filtered_scores)
        filtered_score_list.sort()
        return scores[-1]


def show_hands():
    """Prints out the player's hand and the first card of the dealer's hand."""
    print(f"Your cards: {players_hand}, current score: \
{score_hand(players_hand)}")
    print(f"Computer's first card: {dealers_hand[0]}")


def show_final_hands():
    print(f"Your final hand {players_hand}, final score: \
{score_hand(players_hand)}")
    print(f"Computer's final hand {dealers_hand}, final score: \
{score_hand(dealers_hand)}")


def show_game_result(player_score, dealer_score):
    """Displays win or lose messages."""
    # player busts
    if player_score > 21 and dealer_score < 21:
        return print("You went over. You lose.")
    # dealer busts
    if dealer_score > 21 and player_score < 21:
        return print("Computer went over. You win.")
    # tie
    if dealer_score == player_score:
        return print("It's a tie.")
    # player wins
    if player_score > dealer_score:
        return print("You win.")
    # dealer wins
    if dealer_score > player_score:
        return print("You lose.")


def calculate_scores():
    """Calculates the scores of the player and the dealer."""
    global player_score
    global dealer_score
    player_score = score_hand(players_hand)
    dealer_score = score_hand(dealers_hand)


def check_for_blackjack():
    """Checks if the player or computer has blackjack.
    If either have blackjack, sets their stand flag to True."""
    global player_stands
    global dealer_stands
    if player_score == 21 and dealer_score == 21:
        player_stands = True
        dealer_stands = True
        print("You both have blackjack! It's a tie.")
        reset_game()
        play_game()
    elif player_score == 21:
        player_stands = True
        dealer_stands = True
        print("Blackjack! You win!")
        reset_game()
        play_game()
    elif dealer_score == 21:
        player_stands = True
        dealer_stands = True
        print("Dealer has Blackjack! You lose!")
        reset_game()
        play_game()


def play_game():
    global player_stands
    global dealer_stands
    while not player_stands:
        player_draws = input("Would you like to draw a card?\n")
        if player_draws == 'y':
            draw_card(players_hand)
            calculate_scores()
            show_hands()
            if player_score > 21:
                player_stands = True
            else:
                continue
        elif player_draws == 'n':
            player_stands = True
        else:
            print("I don't understand that. You have to type y or n.")
            continue
    while not dealer_stands:
        if dealer_score >= 17:
            dealer_stands = True
        else:
            draw_card(dealers_hand)
            calculate_scores()
            if dealer_score < 17:
                continue
            else:
                dealer_stands = True


def reset_game():
    """Resets all of the game flags to their starting values."""
    global players_hand
    global dealers_hand
    global player_score
    global dealer_score
    global player_busts
    global dealer_busts
    global player_stands
    global dealer_stands

    players_hand = []
    dealers_hand = []
    player_score = 0
    dealer_score = 0
    player_busts = False
    dealer_busts = False
    player_stands = False
    dealer_stands = False


playing_game = start_game()
while playing_game:
    print(logo)
    draw_card(dealers_hand)
    draw_card(dealers_hand)
    draw_card(players_hand)
    draw_card(players_hand)
    show_hands()
    check_for_blackjack()
    while not player_stands:
        play_game()
    show_final_hands()
    show_game_result(player_score, dealer_score)
    reset_game()
    play_again = start_game()
    if play_again:
        continue
    else:
        break
