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

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    """Asks the user to pick a difficulty, sets the difficulty variable. Calls
       itself if given an invalid input"""
    user_difficulty = input("Would you like to try easy or hard mode?\n")
    cleaned_user_difficulty = user_difficulty.lower().strip()
    if cleaned_user_difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif cleaned_user_difficulty == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Sorry, you have to choose 'easy' or 'hard'.")
        return set_difficulty()


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


def play_again():
    """Restarts the game"""
    restart_game = input("Would you like to play again? y or n.\n")\
        .lower().strip()
    if restart_game == "y":
        play_game()
    elif restart_game == "n":
        return
    else:
        print("I don't understand that. Please enter 'y' or 'n'.")
        return(play_again())


def play_round(number_of_guesses, answer):
    """Runs the logic for a round of play. Calls itself if guesses_left is not
       0."""
    if number_of_guesses != 0:
        guess = get_player_guess()
        if guess == answer:
            print(f"That's it! The answer was {answer} You guessed correctly.")
            return play_again()
        elif guess > answer:
            print("Too high. Try again.")
            number_of_guesses -= 1
            return play_round(number_of_guesses, answer)
        else:
            print("Too low. Try again.")
            number_of_guesses -= 1
            return play_round(number_of_guesses, answer)
    else:
        print(f"You are out of guesses. The number was {answer}. You lose.")
        return play_again()


def play_game():
    """Runs the game loop."""
    # print logo
    print(logo)

    # ask what difficulty to play on
    # set number of guesses according to difficulty
    guesses_left = set_difficulty()

    # generate a random number from 1 to 100
    game_answer = set_answer()

    # play round
    play_round(guesses_left, game_answer)


play_game()
