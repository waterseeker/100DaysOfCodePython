# The basic syntax is:
# new_dict = {new_key:new_value for item in list}
import random

names = ["Gabriella", "Heath", "Indaria", "Julie"]
random_scores = {item: random.randint(0, 100) for item in names}
print(random_scores)

# You can also create a new dictionary from an existing dictionary
# new_dict = {new_key:new_value for (key, value) in dict.items()}
old_dict = {
    "player_1": "Arianna",
    "player_2": "Boudreaux",
    "player_3": "Chang",
    "player_4": "David",
    "player_5": "Elizabeth",
}

new_dict = {value.upper(): key.lower() for (key, value) in old_dict.items()}
print(new_dict)

# You can use conditionals with this too
conditional_dict = {value.upper(): key.lower() for (key, value) in old_dict.items() if len(value) > 7}
print(conditional_dict)

# Using a dictionary comprehension for finding the lengths of words in a sentence.
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word: len(word) for word in sentence.split()}
print(result)
