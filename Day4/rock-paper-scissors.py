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

# Write your code below this line 👇
possible_choices = ["rock", "paper", "scissors"]
choice_pictures = [rock, paper, scissors]
possible_numerical_inputs = [0, 1, 2]
print("Welcome to Rock, Paper, Scissors!")
choice_is_valid = True
while True:
    try:
        player_choice = int(input("What do you choose? Type 0 for Rock, 1 for \
Paper or 2 for Scissors.\n"))
    except ValueError:
        print("Sorry, that's not a valid move.")
        continue
    if player_choice not in possible_numerical_inputs:
        choice_is_valid = False
    else:
        choice_is_valid = True
    while choice_is_valid is False:
        player_choice = input(f"Sorry, that's is not a valid move. \
Please type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
        continue
    computer_choice = random.choice(possible_numerical_inputs)
    if player_choice == computer_choice:
        print(f"It's a tie. You both chose {possible_choices[player_choice]}.")
        continue
    elif player_choice == 0 and computer_choice == 1:
        print(f"{rock} vs. {paper}\n You lose!")
    elif player_choice == 1 and computer_choice == 2:
        print(f"{paper} vs. {scissors}\n You lose!")
    elif player_choice == 2 and computer_choice == 0:
        print(f"{scissors} vs. {rock}\n You lose!")
    else:
        print(f"{choice_pictures[player_choice]} vs. \
{choice_pictures[computer_choice]}\nYou win!")
