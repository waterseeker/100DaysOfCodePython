from art import logo, vs
from game_data import data
from random import choice

score = 0
data_length = len(data)
def getData(data):
    return choice(data)

first_person = getData(data)
second_person = getData(data)
print(first_person)
print(logo)
print(f'Compare A: {first_person}, a {first_person}, from {first_person}.')
print(vs)
print(f'Against B: {second_person}, a {second_person}, from {second_person}.')
user_choice = input("Who has more followers? Type 'A' or 'B': ")