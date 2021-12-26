# Example output:

# What's the first number?: 3
# +
# -
# *
# /
# Pick an operation: *
# 3.0 * 5.0 = 15.0
# Type 'y' to continue calculating with 15.0, or type 'n' to start a new
# calculation:
import re


def get_number(user_input):
    """Takes a user string input, sees if it's castable to a number or float.
       Prints and error message if not and calls itself. Otherwise returns the
       number or float.
    """
    # Int is:
    #  - Only numbers that do NOT start with 0 (protect padded number strings)
    #  - Exactly 0
    re_int = re.compile(r"(^[1-9]+\d*$|^0$)")
    # Float is:
    #  - Only numbers but with exactly 1 dot.
    #  - The dot must always be followed number numbers
    re_float = re.compile(r"(^\d+\.\d+$|^\.\d+$)")
    if re_int.match(user_input):
        first_number = int(user_input)
        return first_number
    elif re_float.match(user_input):
        first_number = float(user_input)
        return first_number
    else:
        print("Sorry, that's not a number. Try again.")
        user_input = input("What's the first number?\n")
        return get_number(user_input)


def get_operator(user_input):
    """Takes in a string and checks that it is either +, -, *, or /. Returns
       True if it is and False if it's not.
    """
    input_length = len(user_input)
    if input_length == 1:
        # Operator is:
        #  +, -, *, or /
        operator_found = re.search("[-+*\/]", user_input)
        if operator_found:
            print("Match")
        else:
            print("No Match")
    else:
        print("Sorry, that's not a valid operator. Please choose +, -, *, or \
/")
        user_input = input("Pick an operation.\n")
        get_operator(user_input)


user_input = input("Pick an operation.\n")
get_operator(user_input)

# if len(x) == 1 and get_operator(x):
#     print("Yep")
# else:
#     print("nah")

# user_input = input("What's the first number?\n")
# first_number = get_number(user_input)
# get the operator (make this a function)
# check operator is valid
#   if not, error message
#   if so, continue
# get second number
# check second number is valid
#   if not, error message
#   if so, continue
# print out equation with the answer
# get input to continue with answer or not
#   if not, exit program
#   if so, return to selecting operation and continue from there
