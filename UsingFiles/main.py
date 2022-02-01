# read a file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# # overwrite a file
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")
#
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# # append a file
# with open("my_file.txt", mode="a") as file:
#     file.write("\nSome appended text.")
#
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# # If you try to open a file in write mode that doesn't exist, Python will create that file.
# with open("new_file.txt", mode="w") as file:
#     file.write("This file was created.")

# # Using an absolute path to access a file
# with open("/Users/wayneburris/Desktop/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Using a relative path to access a file:
with open("../../../my_file.txt") as file:
    contents = file.read()
    print(contents)
