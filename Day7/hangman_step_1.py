#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a 
# variable called chosen_word.
chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a 
# variable called guess. Make guess lowercase.
guess = input("Please guess a letter. ").lower()
while True:
    if not guess.isalpha():
        guess = input("Sorry, you can only guess a letter. Please guess a letter. ").lower()
        continue
    break

#TODO-3 - Check if the letter the user guessed (guess) is one of the 
# letters in the chosen_word.
split_word = list(chosen_word)
for character in split_word:
    if character == guess:
        print("Right")
    else:
        print("Wrong")