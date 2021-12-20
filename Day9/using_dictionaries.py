programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as\
expected.",
    "Function": "A piece of code that you can easily call over and over \
again.",
}

# Retrieve an item from the dictionary
# using key
print(programming_dictionary["Bug"])

# Add an entry
programming_dictionary["Loop"] = "The action of doing something over and \
over again."
print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Loop"] = "Edited value."
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

for key, value in programming_dictionary.items():
    print(key, value)

# Create an empty dictionary
empty_dictionary = {}

# You can also use that to wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)
