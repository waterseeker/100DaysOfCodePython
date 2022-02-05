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
