# Some examples of how to use lists in Python

# Storing some strings
state1 = "Delaware"
state2 = "Pennsylvania"

list_of_states = [state1, state2]

# If you print the list, you'll see brackets
print(f"Printing the list variable: {list_of_states}")

# You can iterate through the list with a for loop to not print the brackets.
# This prints each entry on a new line.
for entry in list_of_states:
    print(f"Printing from a for loop: {entry}")

# Same sort of thing with a list comprehension
[print(f"Printing from a list comprehension: {x}") for x in list_of_states]

# Print by index in the list
print(f"Printing by index 0: {list_of_states[0]}")

# You can get the last item in a list of any length by using index of -1
print(f"Printing last item in the list using -1 index {list_of_states[-1]}")

# Change items by using assignment with an index
list_of_states[0] = "Changed State"
print(f"New first item is: {list_of_states[0]}")

# Append a single item to the list using append function
list_of_states.append("New State")
print(f"Added {list_of_states[2]} to the list of states.")

# Add a list to a list using the extend function
another_list = ["extended state1, extended state2"]
list_of_states.extend(another_list)
print(f"Used the extend method to add the entries in another list to the first list. {list_of_states}")