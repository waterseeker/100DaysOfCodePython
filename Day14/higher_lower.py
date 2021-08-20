from art import logo, vs
from game_data import data
from random import choice

score = 0
data_length = len(data)
def getData(data):
    return choice(data)
entry_A = getData(data)
entry_B = getData(data)
entry_A['choice'] = 'A'
entry_B['choice'] = 'B'
choices = [entry_A, entry_B]
play_game = True
print(logo)

while play_game:
    if entry_A['follower_count'] == entry_B['follower_count']:
        entry_B = getData(data)
        continue
    else:
        print(f'Compare A: {entry_A["name"]}, a {entry_A["description"]}, from {entry_A["country"]}.')
        print(vs)
        print(f'Against B: {entry_B["name"]}, a {entry_B["description"]}, from {entry_B["country"]}.')
        most_followers = max(x['follower_count'] for x in choices)
        answer = [x for x in choices if x['follower_count'] == most_followers][0]
        while True:
            user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
            if user_choice != 'A' and user_choice != 'B':
                print('Sorry, you have to choose A or B.')
                continue
            else:
                if user_choice == answer['choice']:
                    score += 1
                    print(f"You're right! Current score: {score}")
                    answer['choice'] = 'A'
                    entry_A = answer
                    entry_B = getData(data)
                    choices = [entry_A, entry_B]
                    break
                else:  
                    print(f"Sorry, that's wrong. Final score: {score}")
                    play_game = False
                    break