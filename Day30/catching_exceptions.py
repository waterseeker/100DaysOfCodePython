# FileNotFound

# try:
#     file = open("a_file.txt")
# except: # you shouldn't use an except block without a specific error type
#     file = open("a_file.txt", 'w')
#     file.write("Something")

# try:
#     file = open("a_file.txt")
# except FileNotFoundError:
#     file = open("a_file.txt", 'w')
#     file.write("Something")

# you can have multiple except blocks, catching different errors
try:
    file = open("a_file.txt")
    a_dictionary = {'key': 'value'}
    print(a_dictionary["something"])  # this will throw a KeyError
except FileNotFoundError:
    file = open("a_file.txt", 'w')
    file.write("Something")
# you can get the actual error message like this...
except KeyError as error_message:
    # print("That key does not exist.")
    print(f"The key {error_message} does not exist.")
