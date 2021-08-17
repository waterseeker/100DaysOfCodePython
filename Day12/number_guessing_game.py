import random

print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(0,100)

while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        player_guesses = 10
        break
    elif difficulty == 'hard':
        player_guesses = 5
        break
    else:
        print("What's that? Sorry you have to pick either 'easy' or 'hard'.")
# player gets a number of guesses based on difficulty 
#  easy = 10     hard = 5
# player guesses
# gets message telling them whether their guess is too high, too low, or correct.
# if they didn't guess it, they get a message
# print("Guess again.")
# print(f"You have {number_of_guesses} attempts remaning to guess the number.")
player_guess = input("Make a guess: ")

# if the player runs out of guesses:
# print("You've run our of guesses. You lose.")

# if the player guesses the number:
# print(f"You got it! The answer was {answer}")