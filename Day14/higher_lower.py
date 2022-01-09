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


def get_random_entry():
    """Returns a random entry from data"""
    return random.choice(data)


def get_next_matchup(entry_1):
    entry_a = entry_1
    entry_b = get_random_entry()
    entry_b = get_rid_of_duplicates_and_ties(entry_a, entry_b)
    return [entry_a, entry_b]


def label_entries(list_of_entries):
    # Assign 'A' and 'B' labels to the entries
    list_of_entries[0]['label'] = 'A'
    list_of_entries[1]['label'] = 'B'
    return list_of_entries


def get_rid_of_duplicates_and_ties(first_entry, second_entry):
    while first_entry['follower_count'] == second_entry['follower_count']:
        second_entry = get_random_entry()
    return second_entry


def get_highest_number_of_followers(entry_list):
    highest_followers = 0
    for entry in entry_list:
        if int(entry['follower_count']) > highest_followers:
            highest_followers = int(entry['follower_count'])
    return highest_followers


def get_answer(entry_list, highest_followers):
    answer = ([entry for entry in entry_list
              if int(entry['follower_count']) == highest_followers]
              [0])
    return answer


def get_user_answer():
    user_answer = (input("Who has more followers? Type 'A' or 'B':\n")
                   .upper()
                   .strip())
    if user_answer != 'A' and user_answer != 'B':
        print("Choose 'A' or 'B'.")
        return get_user_answer()
    else:
        return user_answer


def ask_user_to_play_again():
    play_again = (input("Would you like to play again? 'Y' or 'N'.\n")
                  .upper()
                  .strip())
    if play_again == 'Y' or play_again == 'N':
        return play_again
    else:
        print("Please select 'Y' or 'N'.")
        return ask_user_to_play_again()


def play_another_round(entry_a):
    entries = get_next_matchup(entry_a)
    label_entries(entries)
    highest_number_of_followers = (
        get_highest_number_of_followers(entries))
    answer = get_answer(entries, highest_number_of_followers)

    # Print first entry info.
    print(f"Compare A: {entries[0]['name']}, a {entries[0]['description']}, \
from {entries[0]['country']}.")

    # vs Art
    print(vs)

    # Print second entry info.
    print(f"Against B: {entries[1]['name']}, a {entries[1]['description']}, \
from {entries[1]['country']}.")
    user_answer = get_user_answer()
    if user_answer == answer['label']:
        print("Correct!")
        return play_another_round(answer)
    else:
        print("You guessed wrong. GAME OVER")
        play_again = ask_user_to_play_again()
        if play_again == 'Y':
            return play_another_round(get_random_entry())
        else:
            pass


# print higher lower logo art on game start
print(logo)

# get entries
entry_a = get_random_entry()
entry_b = get_random_entry()

# make sure there isn't a tie, and that the choices aren't the same item.
get_rid_of_duplicates_and_ties(entry_a, entry_b)

# add 'A' and 'B' labels to entries for comparison to user input later.
entries = [entry_a, entry_b]
label_entries(entries)

# determine which entry has the highest follower count
highest_number_of_followers = get_highest_number_of_followers(entries)

answer = get_answer(entries, highest_number_of_followers)

# Print entry_a info
print(f"Compare A: {entry_a['name']}, a {entry_a['description']}, \
from {entry_a['country']}.")

# vs Art
print(vs)

# Print entry_b info.
print(f"Against B: {entry_b['name']}, a {entry_b['description']}, \
from {entry_b['country']}.")

playing_game = True
while playing_game:
    user_answer = get_user_answer()
    if user_answer == answer['label']:
        print("Correct!")
        play_another_round(answer)
    else:
        print("You guessed wrong. GAME OVER")
        play_again = ask_user_to_play_again()
        if play_again == 'Y':
            play_another_round(get_random_entry())
        else:
            playing_game = False
            break
