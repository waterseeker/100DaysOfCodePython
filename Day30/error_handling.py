# trying to open a file that doesn't exist will throw an error and crash your program.
# with open("a_file.txt") as file:
#     file.read()
# throws this error
# Traceback(most recent call last): File
#     'filepath goes here', line 2, in < module >
#         with open("a_file.txt") as file:
# FileNotFoundError: [Errno 2] No such file or directory: 'a_file.txt'

# some types of errors and examples
# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {'key': 'value'}
# value = a_dictionary["non_existent_key"]

# IndexError
# a_list = [1, 2, 3]
# a_non_existent_index = a_list[6]

# TypeError
# text = "abc"
# print(text + 4)
