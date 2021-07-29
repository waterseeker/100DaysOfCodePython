#Step 5

import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
user_guesses = []
end_of_game = False
lives = 6

print(logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in user_guesses:
        print(f"You've already guessed {guess}.")
        continue
    user_guesses += guess  

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"Sorry, {guess} is not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
        else:
            if lives == 1:
                print("This is your last chance. You only have 1 life left.")
            else:
                print(f"You have {lives} lives left.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])