# List comprehensions are a python feature that makes using for loops on lists shorter and easier to read
# For example...

numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

print(new_list)

# Same thing with a list comprehension
# the format is:
# new_list = [new_item for item in list]
numbers = [1, 2, 3]
comprehension = [n + 1 for n in numbers]
print(comprehension)

# You can add conditional statements to a comprehension as well
# the format is:
# new_list = [new_item for item in list if condition]

# get only names that have 4 letters or less
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
new_names = [name for name in names if len(name) <= 4]
print(new_names)

# Take all names from the list of names that have at least 5 letters and make them into a new list using all caps
cap_names = [name.upper() for name in names if len(name) > 4]
print(cap_names)

# Returning only even numbers from a list
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num for num in numbers if num % 2 == 0]

print(result)
