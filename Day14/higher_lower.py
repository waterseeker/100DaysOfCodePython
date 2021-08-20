from art import logo, vs
from game_data import data
from random import choice

score = 0
data_length = len(data)
def getData(data):
    return choice(data)

entry_A = getData(data)
entry_B = getData(data)
print(entry_A)
print(logo)
print(f'Compare A: {entry_A}, a {entry_A}, from {entry_A}.')
print(vs)
print(f'Against B: {entry_B}, a {entry_B}, from {entry_B}.')
user_choice = input("Who has more followers? Type 'A' or 'B': ")

# if the player guesses correctly,
score += 1
print(f"You're right! Current score: {score}")
#   the correct answer becomes entry A for the next round
#   get a new entry from data that becomes entry B for the next round

# game ends when the player get an incorrect answer
print(f"Sorry, that's wrong. Final score: {score}")