# Step 1
import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a
# variable called chosen_word.
random_word = random.choice(word_list)
# TODO-2 - Ask the user to guess a letter and assign their answer to a
# variable called guess. Make guess lowercase.
guess = input("Please choose a letter:\n").lower()
# TODO-3 - Check if the letter the user guessed (guess) is one of the
# letters in the chosen_word.
if guess in random_word:
    print(f"That letter is in {random_word}.")
else:
    print(f"That letter is not in {random_word}.")
