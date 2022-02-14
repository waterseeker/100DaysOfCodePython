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
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     # print(a_dictionary["something"])  # this will throw a KeyError
#     print(a_dictionary["key"])
# except FileNotFoundError:  # except blocks execute if there is an error. you should specify the type of error
#     file = open("a_file.txt", "w")
#     file.write("Something")
# # you can get the actual error message like this...
# except KeyError as error_message:
#     # print("That key does not exist.")
#     print(f"The key {error_message} does not exist.")
# else:  # an else block executes if the try block is successful
#     content = file.read()
#     print(content)
# finally:  # the finally block executes whether there were errors or not. not often used, but it can be useful
#     file.close()
#     print("File was closed.")


# you can raise your own errors with 'raise'
# you might want to do this as a form of input validation
# for example, if someone is entering their height and it's over 3 meters, you might want to raise an exception
height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
