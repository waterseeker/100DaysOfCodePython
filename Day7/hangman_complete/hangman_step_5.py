# Step 4

import random
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(word_list)
lives = 6
# TODO-3: - Import the logo from hangman_art.py and print it at the start of
# the game.
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = ['_' for x in chosen_word]

while True:
    guess = input("Guess a letter: ").lower()
    if guess not in chosen_word:
        # TODO-5: - If the letter is not in the chosen_word, print out the
        # letter and let them know it's not in the word.
        lives -= 1
        if lives == 0:
            print(display)
            print(hangman_art.stages[lives])
            print("You lose.")
            break
    # TODO-4: - If the user has entered a letter they've already guessed,
    # print the letter and let them know.
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
    # TODO-2: - Import the stages from hangman_art.py and make this error go
    # away.
    print(hangman_art.stages[lives])
    # Check if user has got all letters.
    if "_" not in display:
        print("You win!")
        break
