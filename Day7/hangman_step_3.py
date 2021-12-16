# Step 2
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = ['_' for x in chosen_word]

# TODO-1: - Use a while loop to let the user guess again. The loop should
# only stop once the user has guessed all the letters in the chosen_word and
# 'display' has no more blanks ("_"). Then you can tell the user they've won.

while True:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    index = 0
    for letter in chosen_word:
        if letter == guess:
            display[index] = guess
            index += 1
        else:
            index += 1

    print(display)

    if "_" not in display:
        print("You win!")
        break
