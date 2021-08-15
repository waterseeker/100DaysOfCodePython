############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

from art import logo
import random
from collections import Counter
from os import system

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_busts = False
dealer_busts = False

def get_score(hand_array):
    """Takes in an array, checks for blackjack. 
    Returns either the hand total or 'blackjack'"""
    # checks to see if it's blackjack
    if len(hand_array) == 2 and sum(hand_array) == 21:
        return 'blackjack'
    # No matter the number of aces in a hand, only 1 could ever be worth 11
    # since 2 worth 11 would be an automatic bust (11 + 11 = 22)
    # finds the number of aces in the hand and calculates the score with one of
    # them being an 11 as long as that doesn't cause a bust, else they're all worth
    # 1 point each.
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

def draw_card(hand_array):
    """takes in a hand array of cards. 
    adds a random card from the cards array to the hand that is passed into the function"""
    hand_array.append(random.choice(cards))

def dealer_draw():
    """Determines whether or not the dealer is going to draw. 
    Draws a card and adds it to the dealer's hand until the dealer stands or busts."""
    global dealer_stands
    global dealer_score
    global dealer_hand
    global dealer_busts

    if dealer_score > 21:
        print("The dealer busts!")
        dealer_busts = True
        play_again()
    elif dealer_score < 17:
        print("The dealer draws another card.")
        draw_card(dealer_hand)
        dealer_score = get_score(dealer_hand)
        print(f"Dealer's hand: {dealer_hand}")
        dealer_draw()
    elif dealer_score >= 17 and dealer_score < 21:
        print(f"The dealer stands with {dealer_score}.")
        dealer_stands = True
        return

def player_draw():
    """Asks the player if they want to draw a card. 
    If so, adds a random card from the cards array to the player's hand.
    If the player busts, ends the game."""
    global player_stands
    global player_score
    global player_hand
    global player_busts
    draw = input(f"You have {player_score}. Would you like to draw a card? 'y' or 'n': ")
    if draw == 'y':
        draw_card(player_hand)
        print(f'Your cards: {player_hand}')
        player_score = get_score(player_hand)
        if player_score > 21:
            print(f"{player_score}. You bust! The dealer wins.")
            player_busts = True
            play_again()
            return
        elif player_score == 21:
            print("You have 21. It doesn't get better than that so you stand.")
            player_stands = True
        else:
            player_draw()
    else:
        player_stands = True
        print(f"You stand with {player_score}.")

def print_hands():
    """Displays the player's and dealer's hands."""
    global player_hand
    global dealer_hand
    print(f'Your cards: {player_hand}')
    print(f"Dealer's cards: {dealer_hand}")

def play_again():
    """Asks the player if they would like to play again. Clears the console and restarts game loop if so. """
    start_again = input("Do you want to play again? 'y' or 'n': ")
    if start_again == 'y':
        play_game = True
        reset_game()
        return True
    else:
        return False

def reset_game():
    """Clears the player's and dealer's hands, scores, and the console."""
    global player_hand
    global dealer_hand
    player_hand = []
    dealer_hand = []
    player_score = 0
    dealer_score = 0
    clear_console()

def game_result():
    """Displays the results of the game in the case of no bust."""
    global player_score
    global dealer_score
    if player_score > dealer_score:
        print(f"Congratulations! You win with a score of {player_score}.")
    elif dealer_score > player_score:
        print(f"The dealer wins with a score of {dealer_score}.")
    else:
        print(f"It's a tie with you and the dealer both having {player_score}.")

def play_blackjack():
    """The main game loop where the player and dealer get to draw until they either stand or bust."""
    global player_stands
    global dealer_stands
    if not player_stands and not player_busts:
        player_draw()
    if not dealer_stands and not player_busts:
        dealer_draw()
    if player_stands and dealer_stands:
        return

def clear_console():
    """Clears the console."""
    _ = system('clear')

start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start_game == 'y':
    play_game = True
else:
    play_game = False

while play_game:
    print(logo)
    player_stands = False
    dealer_stands = False
    player_busts = False
    dealer_busts = False
    player_hand = [random.choice(cards), random.choice(cards)]
    player_score = get_score(player_hand)
    dealer_hand = [random.choice(cards), random.choice(cards)]
    dealer_score = get_score(dealer_hand)
    if player_score == 'blackjack' and dealer_score != 'blackjack':
        print_hands()
        print('Blackjack! You win!')
        play_again()
        if play_again:
            continue
        else:
            play_game = False
            break
    elif player_score != 'blackjack' and dealer_score == 'blackjack':
        print_hands()
        print('The dealer wins with Blackjack!')
        play_again()
        if play_again:
            continue
        else:
            play_game = False
            break
    elif player_score == 'blackjack' and dealer_score == 'blackjack':
        print_hands()
        print("It's a tie! You both have Blackjack. What are the odds?")
        play_again()
        if play_again:
            continue
        else:
            play_game = False
            break
    else:
        print(f'Your cards: {player_hand}')
        print(f"Dealer's first card: {dealer_hand[0]}")
        play_blackjack()
        if not player_busts and not dealer_busts:
            game_result()
        if play_again:
            continue
        else:
            play_game = False
            break

    play_game = False