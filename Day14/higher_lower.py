from art import logo, vs
import random
from game_data import data

# entry data structure
# {
#     'name': 'Instagram',
#     'follower_count': 346,
#     'description': 'Social media platform',
#     'country': 'United States'
# }


def get_random_entry():
    """Returns a random entry from data"""
    return random.choice(data)


def get_next_matchup(entry_1=get_random_entry()):
    """Takes in an optional entry (the answer from the previous round should
    go here if it's not the first round. Returns a pair of entries for
    comparison during the game round."""
    entry_a = entry_1
    entry_b = get_random_entry()
    cleaned_matchup = remove_duplicates_and_ties(entry_a, entry_b)
    return cleaned_matchup


def label_entries(list_of_entries):
    """Takes in a list and assigns a new 'label' property to the entries.
    This is so the player input can be matched to the entries during the game.
    This method assumes there are only 2 entries in the passed in list and
    returns the modified list."""
    list_of_entries[0]['label'] = 'A'
    list_of_entries[1]['label'] = 'B'
    return list_of_entries


def remove_duplicates_and_ties(first_entry, second_entry):
    """Takes in 2 entries. If the second entry is the same as the first one,
    or if the second entry has the same number of followers as the first one,
    it generated a new second entry until there is no tie. Returns the 2
    entries as a list."""
    while first_entry['follower_count'] == second_entry['follower_count']:
        second_entry = get_random_entry()
    return [first_entry, second_entry]


def get_highest_number_of_followers(entry_list):
    """Takes in a list, returns an int that is the highest number of followers
    between the 2 entries."""
    highest_followers = 0
    for entry in entry_list:
        if int(entry['follower_count']) > highest_followers:
            highest_followers = int(entry['follower_count'])
    return highest_followers


def get_answer(entry_list, highest_followers):
    """Takes in a list and an int and returns the list entry where the
    follower_count is equal to the int."""
    answer = ([entry for entry in entry_list
              if int(entry['follower_count']) == highest_followers]
              [0])
    return answer


def get_user_answer():
    """Takes in user input. Cleans it and makes sure it's valid, then returns
    it. If the input isn't valid, the method calls itself until the user
    inputs a valid value."""
    user_answer = (input("Who has more followers? Type 'A' or 'B':\n")
                   .upper()
                   .strip())
    if user_answer != 'A' and user_answer != 'B':
        print("Choose 'A' or 'B'.")
        return get_user_answer()
    else:
        return user_answer


def ask_user_to_play_again():
    """Gets user input for whether or not they want to play again. Cleans and
    validates the input. If the input isn't valid, the method calls itself
    until the input is valid. Returns the cleaned and valid input."""
    play_again = (input("Would you like to play again? 'Y' or 'N'.\n")
                  .upper()
                  .strip())
    if play_again == 'Y' or play_again == 'N':
        return play_again
    else:
        print("Please select 'Y' or 'N'.")
        return ask_user_to_play_again()


def play_another_round(entry_a):
    """Takes in an entry (the answer from the previous round. Runs game round
    logic in loops until the user wants to quit."""
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
            return


# print higher lower logo art on game start
print(logo)

playing_game = True
while playing_game:
    # get set of entries
    try:
        answer
        entries = get_next_matchup(answer)
    except NameError:
        entries = get_next_matchup()
    # make sure no ties or duplicates
    entry_a = entries[0]
    entry_b = entries[1]
    cleaned_entries = remove_duplicates_and_ties(entry_a, entry_b)
    # label entries for comparison against 'a' and 'b' input from player later
    labeled_entries = label_entries(cleaned_entries)
    # get highest number of followers
    highest_followers = get_highest_number_of_followers(labeled_entries)
    # get answer
    answer = get_answer(labeled_entries, highest_followers)
    # print line for first entry
    print(f"Compare A: {labeled_entries[0]['name']}, a \
{labeled_entries[0]['description']}, from {labeled_entries[0]['country']}.")
    # print vs art
    print(vs)
    # print line for second entry
    print(f"Against B: {labeled_entries[1]['name']}, \
a {labeled_entries[1]['description']}, \
from {labeled_entries[1]['country']}.")
    # get player answer
    # make sure it's a or b, recursion if not
    user_answer = get_user_answer()
    # check player input against answer
    # if correct, recursion with the answer getting passed into the new set
    # of comparisons.
    # make sure the answer getting passed doesn't get replaced by checking for
    # duplicates and ties
    if user_answer == answer['label']:
        print("Correct!")
        continue
    # if wrong, display end game message
    else:
        print("Incorrect! GAME OVER")
        # ask if player wants to play again
        play_again = ask_user_to_play_again()
        if play_again == 'Y':
            # if so, recursion with all new entries
            answer = get_random_entry()
            continue
        # if not, end game
        else:
            playing_game = False
