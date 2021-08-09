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

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# hand = random.choices(cards, k=2)
hand = [11, 10]

def get_score(hand_array):
    print(hand_array)
    if 11 not in hand_array:
        score = sum(hand_array)
    score = sum(hand_array)
    if score == 21:
        print(f'Your score is : {score}')
get_score(hand)
# start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
# if start_game == 'y':
#     play_game = True
#     print(logo)

# while play_game:
#     player_hand = [random.choice(cards), random.choice(cards)]
#     player_score = get_score(player_hand)
#     dealer_hand = [random.choice(cards), random.choice(cards)]
    

    
#     print(f'Your cards: {player_hand}')
#     print(f'Computer"s first card: {dealer_hand[0]}')

#     play_game = False