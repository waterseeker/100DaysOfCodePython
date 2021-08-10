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

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# may need flags for player has blackjack and computer has blackjack

def get_score(hand_array):
    # is it blackjack?
    if len(hand_array) == 2:
        if sum(hand_array) == 21:
            return 'blackjack'
    number_of_aces = Counter(hand_array)[11]
    non_ace_total = sum(card for card in hand_array if card != 11)
    if number_of_aces > 0:
        if non_ace_total + 11 + (number_of_aces - 1) <= 21:
            ace_value = 11 + (number_of_aces - 1)
        else:
            ace_value = number_of_aces
    hand_total = non_ace_total + ace_value
    return hand_total

def draw_card(hand_array):
    hand_array += random.choice(cards)

start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start_game == 'y':
    play_game = True
    print(logo)
else:
    play_game = False

while play_game:
    player_hand = [random.choice(cards), random.choice(cards)]
    player_score = get_score(player_hand)
    dealer_hand = [random.choice(cards), random.choice(cards)]
    dealer_score = get_score(dealer_hand)
    if player_score == 'blackjack' and dealer_score != 'blackjack':
        print(f'Your cards: {player_hand}')
        print(f"Dealer's cards: {dealer_hand}")
        print('Blackjack! You win!')
        start_again = input("Do you want to play again? 'y' or 'n': ")
        if start_again:
            continue
        else:
            break
    elif player_score != 'blackjack' and dealer_score == 'blackjack':
        print(f'Your cards: {player_hand}')
        print(f"Dealer's cards: {dealer_hand}")
        print('The dealer wins with Blackjack!')
        start_again = input("Do you want to play again? 'y' or 'n': ")
        if start_again:
            continue
        else:
            break
    elif player_score == 'blackjack' and dealer_score == 'blackjack':
        print(f'Your cards: {player_hand}')
        print(f"Dealer's cards: {dealer_hand}")
        print("It's a tie! You both have Blackjack. What are the odds?")
        start_again = input("Do you want to play again? 'y' or 'n': ")
        if start_again:
            continue
        else:
            break
    else:
        print(f'Your cards: {player_hand}')
        print(f"Dealer's first card: {dealer_hand[0]}")
        draw = input("Would you like to draw a card? 'y' or 'n': ")
        if draw == 'y':
            draw_card(player_hand)
            print(f'Your cards: {player_hand}')
            player_score = get_score(player_hand)
            if player_score > 21:
                print("You bust!")
                start_again = input("Do you want to play again? 'y' or 'n': ")
                if start_again:
                    continue
                else:
                    break
            if player_score == 21:
                print("You have 21. It doesn't get better than that so you stand.")
            if dealer_score >= 17:
                print("The dealer stands.")
                print(f"Dealer's first card: {dealer_hand[0]}")
            if dealer_score < 17:
                print("The dealer draws another card.")
                draw_card(dealer_hand)
                print(f'Computer"s first card: {dealer_hand[0]}')
        else:



    play_game = False