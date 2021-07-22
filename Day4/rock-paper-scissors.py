# Make a rock, paper, scissors game where the user inputs 0, 1, or 2 for their choice.
# The game should display the asci art for the players choice and the computers choice.
# There should be a message telling the player whether they win, lose, or tie.
# In the case of a tie, ask the player to choose again until there is a winner.
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
symbols = [rock, paper, scissors]
print("Welcome to Rock, Paper, Scissors!")
while True:
    player_input = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
    possible_choices = ["0", "1", "2"]
    if player_input not in possible_choices:
        print("Sorry, that's not a valid choice. Please enter 0, 1, or 2.")
        continue
    else:
        print("You chose:")
        player_choice = int(player_input)
        print(symbols[player_choice])
        print("The computer chose:")
        computer_choice = random.randint(0,2)
        print(symbols[computer_choice])
        if player_choice == computer_choice:
            print("It's a tie. Try again.")
            continue
        # 0 = rock, 1 = paper, 2 = scissors
        elif player_choice == 0: 
            if computer_choice == 1:
                print("You lose.")
            else:
                print("You win.")
        elif player_choice == 1:
            if computer_choice == 2:
                print("You lose.")
            else:
                print("You win.")
        elif player_choice == 2:
            if computer_choice == 1:
                print("You lose.")
            else:
                print("You win.")
        break