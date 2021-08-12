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

def get_score(hand_array):
    # is it blackjack?
    if len(hand_array) == 2:
        if sum(hand_array) == 21:
            return 'blackjack'
    number_of_aces = Counter(hand_array)[11]
    non_ace_total = sum(card for card in hand_array if card != 11)
    ace_value = 0
    if number_of_aces > 0:
        if non_ace_total + 11 + (number_of_aces - 1) <= 21:
            ace_value = 11 + (number_of_aces - 1)
        else:
            ace_value = number_of_aces
    hand_total = non_ace_total + ace_value
    return hand_total

def draw_card(hand_array):
    hand_array.append(random.choice(cards))

def dealer_draw():
    global dealer_stands
    global dealer_score
    global dealer_hand
    if dealer_score >= 17:
        print("The dealer stands.")
        dealer_stands = True
        print(f"Dealer's hand: {dealer_hand}")
        return
    if dealer_score < 17:
        print("The dealer draws another card.")
        draw_card(dealer_hand)
        print(f"Dealer's hand: {dealer_hand}")
    if dealer_score > 21:
        print("The dealer busts!")
        play_again()

def player_draw():
    global player_stands
    global player_score
    global player_hand
    draw = input("Would you like to draw a card? 'y' or 'n': ")
    if draw == 'y':
        draw_card(player_hand)
        print(f'Your cards: {player_hand}')
        player_score = get_score(player_hand)
        if player_score > 21:
            print("You bust! The dealer wins.")
            play_again()
            return
        if player_score == 21:
            print("You have 21. It doesn't get better than that so you stand.")
            player_stands = True
    else:
        player_stands = True

def print_hands():
    global player_hand
    global dealer_hand
    print(f'Your cards: {player_hand}')
    print(f"Dealer's cards: {dealer_hand}")

def play_again():
    start_again = input("Do you want to play again? 'y' or 'n': ")
    if start_again == 'y':
        reset_hands()
        return True
    else:
        return False

def reset_hands():
    global player_hand
    global dealer_hand
    player_hand = []
    dealer_hand = []

def game_result():
    global player_score
    global dealer_score
    if player_score > dealer_score:
        print(f"Congratulations! You win with a score of {player_score}.")
        play_again()
    elif dealer_score > player_score:
        print(f"The dealer wins with a score of {dealer_score}.")
        play_again()

def turn_of_play():
    global player_stands
    global dealer_stands
    if not player_stands:
        player_draw()
    if not dealer_stands:
        dealer_draw()
    if player_stands and dealer_stands:
        return
    turn_of_play()

start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start_game == 'y':
    play_game = True
    print(logo)
else:
    play_game = False

while play_game:
    player_stands = False
    dealer_stands = False
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
        turn_of_play()
        game_result()


# how do we know all the rounds are over?
#   the dealer busts
#   the player busts
#   both the dealer and player stand

# then run logic to check final scores and declare the winner

# i think recursion will be the round of play except the first round where there can be a blackjack

    play_game = False


# does the player draw?
#   if so, do they bust?
#       if so, game over and dealer wins
#       if not, this is the end of the player's turn
#   if not the player stands
#       this is the end of the player's turn
# does the dealer draw?
#   if so, do they bust?
#   if not they stand
#       this is the end of the dealer's turn
# once both have stood, compare scores
# declare results
# prompt for play again
# if so return to first round logic where there can be a blackjack