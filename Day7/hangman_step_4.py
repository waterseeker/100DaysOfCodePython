# Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# TODO-1: - Create a variable called 'lives' to keep track of the number of
# lives left.
# Set 'lives' to equal 6.

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = ['_' for x in chosen_word]

while True:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    index = 0
    for letter in chosen_word:
        if letter == guess:
            display[index] = guess
            index += 1
    # TODO-2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print
    # "You lose."
        else:
            index += 1

    # Join all the elements in the list and turn it into a String.
    print(f"{''.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        print("You win!")
        break

    # TODO-3: - print the ASCII art from 'stages' that corresponds to the
    # current number of 'lives' the user has remaining.
