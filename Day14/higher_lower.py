from art import logo, vs
import random
from game_data import data

# data structure
# {
#     'name': 'Instagram',
#     'follower_count': 346,
#     'description': 'Social media platform',
#     'country': 'United States'
# }
letters_to_index = {
                    "a": 0,
                    "b": 1,
                    }
# Get entries from the data
entry_a = random.choice(data)
entry_b = random.choice(data)
entries = [entry_a, entry_b]
answer = max(entry['follower_count'] for entry in entries)
print(answer)
# make sure there isn't a tie, and that the choices aren't the same item.
while entry_b == entry_a or \
      entry_b['follower_count'] == entry_a['follower_count']:
    entry_b = random.choice(data)
# higher lower logo art on game start
print(logo)
# "Compare A: Christiana Ronaldo, a Footballer, from Portugal"
print(f"Compare A: {entry_a['name']}, a {entry_a['description']}, \
from {entry_a['country']}.")
# vs Art
print(vs)
# "Against B: Vin Diesel, a Actor, from United States.
print(f"Against B: {entry_b['name']}, a {entry_b['description']}, \
from {entry_b['country']}.")
# Who has more followers? Type'A' or 'B':
while True:
    user_answer = input("Who has more followers? Type 'A' or 'B':\n")\
                  .lower()\
                  .strip()
    if user_answer != 'A' and user_answer != 'B':
        print("Choose 'A' or 'B'.")
        continue
    else:
        break
# If correct,
if letters_to_index[user_answer] == answer:
    # the previous answer becomes A, a new entry from the data is B
    # game loop runs again
else:
    print("Game Over")
    # game ends
