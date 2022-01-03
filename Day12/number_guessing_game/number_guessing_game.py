# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low."
#   depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only
#   5 guesses in hard mode).

from art import logo
import random


def set_difficulty():
    """Asks the user to pick a difficulty, sets the difficulty variable. Calls
       itself if given an invalid input"""
    user_difficulty = input("Would you like to try easy or hard mode?\n")
    cleaned_user_difficulty = user_difficulty.lower().strip()
    if cleaned_user_difficulty == "easy":
        return cleaned_user_difficulty
    elif cleaned_user_difficulty == "hard":
        return cleaned_user_difficulty
    else:
        print("Sorry, you have to choose 'easy' or 'hard'.")
        return set_difficulty()


def set_guesses(game_difficulty):
    """Sets nubmer of guesses according to difficulty level."""
    if game_difficulty == 'easy':
        return 10
    else:
        return 5


def set_answer():
    """Sets answer to a random integer from 1 to 100."""
    return random.randint(1, 100)


def get_player_guess():
    """Gets a player guess."""
    while True:
        try:
            guess = int(input("Guess a number:\n"))
            if 0 < guess <= 100:
                return guess
            else:
                print("Sorry, that's not in the guessing range. Please pick a\
number from 1 to 100.")
                return get_player_guess()
        except(ValueError, TypeError):
            print("Sorry, that's not a whole number.")
            return get_player_guess()


# print logo
print(logo)
# ask what difficulty to play on
difficulty = set_difficulty()
# set number of guesses according to difficulty
guesses_left = set_guesses(difficulty)
# generate a random number from 1 to 100
answer = set_answer()
# player guesses
get_player_guess()
# tell player if they are above, below, or guesses the number
# adjust number of guesses
# if guesses == 0 end game and ask if they want to play again
#   otherwise run the guess loop again.
