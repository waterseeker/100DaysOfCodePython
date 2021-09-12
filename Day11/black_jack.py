#Wayne went to the ER today 9/12/21

from art import logo
import random
from collections import Counter
from os import system

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_stands = False
player_hand = []
player_busts = False
player_score = 0
dealer_stands = False
dealer_hand = []
dealer_busts = False
dealer_score = 0


def get_score(hand_array):
    """Takes in a hand array of cards and returns the sum.
        Changes the values of aces from 1 to 11 for best score.'"""
    # No matter the number of aces in a hand, only 1 could ever be worth 11
    # since 2 worth 11 would be an automatic bust (11 + 11 = 22)
    # finds the number of aces in the hand and calculates the score with one of
    # them being an 11 as long as that doesn't cause a bust, else they're all
    # worth 1 point each.
    number_of_aces = Counter(hand_array)[11]
    non_ace_total = sum(card for card in hand_array if card != 11)
    ace_value = 0
    if number_of_aces > 0:
        if non_ace_total + 11 + (number_of_aces - 1) <= 21:
            ace_value = 11 + (number_of_aces - 1)
            # replace all but 1 ace in hand with 1s
            for _ in range(number_of_aces - 1):
                for index, card in enumerate(hand_array):
                    if card == 11:
                        hand_array[index] = 1
        else:
            ace_value = number_of_aces
            # replace all aces in hand with 1s
            for index, card in enumerate(hand_array):
                if card == 11:
                    hand_array[index] = 1
    hand_total = non_ace_total + ace_value
    return hand_total


def is_blackjack(hand_array):
    """Returns True if there is blackjack in the hand_array."""
    if len(hand_array) == 2 and sum(hand_array) == 21:
        return True


def play_again():
    """Asks the player if they would like to play again.
    Clears the console and restarts game loop if so. """
    start_again = input("Do you want to play again? 'y' or 'n': ")
    if start_again == 'y':
        play_game = True
        return True
    else:
        return False


def clear_console():
    """Clears the console."""
    _ = system('clear')


def draw_card(hand_array):
    """takes in a hand array of cards.
    adds a random card from the cards array to the hand that is passed into
    the function"""
    hand_array.append(random.choice(cards))


def player_turn():
    """Asks the player if they want to draw a card.
    If so, adds a random card from the cards array to the player's hand.
    Repeats until either the player busts or stands."""
    global player_stands
    global player_score
    global player_hand
    global player_busts
    draw = input(f"You have {player_score}. Would you like to draw a card? \
                 'y' or 'n': ")
    if draw == 'y':
        draw_card(player_hand)
        print(f'Your cards: {player_hand}')
        player_score = get_score(player_hand)
        if player_score > 21:
            print(f"{player_score}. You bust! The dealer wins.")
            player_busts = True
            return
        elif player_score == 21:
            print("You have 21. It doesn't get better than that so you stand.")
            player_stands = True
            return
        else:
            player_turn()
    else:
        player_stands = True
        print(f"You stand with {player_score}.")


def dealer_turn():
    """Determines whether or not the dealer is going to draw.
    Draws a card and adds it to the dealer's hand until the dealer stands or
    busts."""
    global dealer_stands
    global dealer_score
    global dealer_hand
    global dealer_busts

    if dealer_score > 21:
        print("The dealer busts!")
        dealer_busts = True
        return
    elif dealer_score < 17:
        print("The dealer draws another card.")
        draw_card(dealer_hand)
        dealer_score = get_score(dealer_hand)
        print(f"Dealer's hand: {dealer_hand}")
        dealer_turn()
    elif dealer_score >= 17 and dealer_score < 21:
        print(f"The dealer stands with {dealer_score}.")
        dealer_stands = True
        return


def game_result():
    """Displays the results of the game in the case of no bust."""
    global player_score
    global dealer_score
    if player_score > dealer_score:
        print(f"Congratulations! You win with a score of {player_score}.")
    elif dealer_score > player_score:
        print(f"The dealer wins with a score of {dealer_score}.")
    else:
        print(f"It's a tie with you and the dealer both having \
              {player_score}.")


# prompt player to see if they want to play
start_game = input("Do you want to play a game of Blackjack? Type 'y' or \
                   'n': ")
if start_game == 'y':
    play_game = True
else:
    play_game = False

while play_game:
    # print logo
    player_hand = []
    dealer_hand = []
    player_score = 0
    dealer_score = 0
    player_busts = False
    dealer_busts = False
    clear_console()
    print(logo)

    # print initial hands, show both cards from player and only the first one
    #     from the dealer
    player_hand = [random.choice(cards), random.choice(cards)]
    player_score = get_score(player_hand)
    dealer_hand = [random.choice(cards), random.choice(cards)]
    dealer_score = get_score(dealer_hand)
    print(f'Your cards: {player_hand}')
    print(f"Dealer's first card: {dealer_hand[0]}")

    # checks for blackjack and prints results if so
    player_blackjack = is_blackjack(player_hand)
    dealer_blackjack = is_blackjack(dealer_hand)
    if player_blackjack and not dealer_blackjack:
        print('Blackjack! You win!')
        start_new_game = play_again()
        if start_new_game:
            continue
        else:
            play_game = False
            break
    elif dealer_blackjack and not player_blackjack:
        print('The dealer wins with Blackjack!')
        start_new_game = play_again()
        if start_new_game:
            continue
        else:
            play_game = False
            break
    elif player_blackjack and dealer_blackjack:
        print("It's a tie! You both have Blackjack. What are the odds?")
        start_new_game = play_again()
        if start_new_game:
            continue
        else:
            play_game = False
            break
    # player draws until they either stand or bust
    player_turn()
    #   if player bust, print results and prompt player to play again
    if player_busts:
        start_new_game = play_again()
        if start_new_game:
            continue
        else:
            play_game = False
            break
    # if the player didn't bust, dealer draws until they either stand or bust
    else:
        dealer_turn()
    #   if dealer busts, print results and prompt player to play again
    if dealer_busts:
        start_new_game = play_again()
        if start_new_game:
            continue
        else:
            play_game = False
            break
    if player_stands and dealer_stands:
        game_result()
        start_new_game = play_again()
        if start_new_game:
            continue
        else:
            play_game = False
            break
    play_game = False
