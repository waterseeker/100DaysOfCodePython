# You can use comprehensions with strings too.
# You can use them with any python Sequence (list, tuple, range, string)
name = "Martin"
new_list = [letter for letter in name]
print(new_list)

# You can manipulate the new variable with methods as well
name = "Lucien"
new_list = [letter.lower() for letter in name]
print(new_list)
