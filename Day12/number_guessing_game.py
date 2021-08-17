import random

print('Welcome to the Number Guessing Game!')
print("I'm thinking of a whole number between 1 and 100.")
answer = random.randint(0,100)
playing_game = True
while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        player_guesses = 10
        guesses_remaining = player_guesses
        break
    elif difficulty == 'hard':
        player_guesses = 5
        guesses_remaining = player_guesses
        break
    else:
        print("What's that? Sorry you have to pick either 'easy' or 'hard'.")

# player guesses
while playing_game == True:
    if guesses_remaining == 0:
        print("You've run our of guesses. You lose.")
        playing_game = False
        break
    player_guess = input("Make a guess: ")
    if int(player_guess):
        player_guess = int(player_guess)
        if player_guess > answer:
            guesses_remaining -= 1
            print('Too high.')
            print('Guess again.')
            print(f"You have {guesses_remaining} attempts remaning to guess the number.")
            continue
        elif player_guess < answer:
            guesses_remaining -= 1
            print('Too low.')
            print('Guess again.')
            print(f"You have {guesses_remaining} attempts remaning to guess the number.")
            continue
        else:
            print(f"You got it! The answer was {answer}.")
            break
    else:
        print("Sorry, you have to guess a whole number.")