# Step 4

import random
import hangman_art
import hangman_words

# Update the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(hangman_words.word_list)
lives = 6
# Import the logo from hangman_art.py and print it at the start of the game.
logo = hangman_art.logo
print(logo)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = ['_' for x in chosen_word]

# Track guesses letters
guesses = []
while True:
    guess = input("Guess a letter: ").lower()
    # If the user has entered a letter they've already guessed, print the
    # letter and let them know.
    if guess in guesses:
        print(f"You've already guessed {guess}. Try again.")
        continue
    elif guess not in guesses:
        guesses.append(guess)
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and
        # let them know it's not in the word.
        print(f"Sorry, {guess} is not in the word. You lose a life.")
        lives -= 1
        print(f"You have {lives} lives remaning.")
        if lives == 0:
            print(display)
            print(hangman_art.stages[lives])
            print("You lose.")
            break

    # Check guessed letter
    index = 0
    for letter in chosen_word:
        if letter == guess:
            display[index] = guess
            index += 1
        else:
            index += 1

    # Join all the elements in the list and turn it into a String.
    print(f"{''.join(display)}")

    # Import the stages from hangman_art.py.
    print(hangman_art.stages[lives])

    # Check if user has got all letters.
    if "_" not in display:
        print("You win!")
        break
