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
        input_number = int(user_input)
        return input_number
    elif re_float.match(user_input):
        input_number = float(user_input)
        return input_number
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
            return user_input
    else:
        print("Sorry, that's not a valid operator. Please choose +, -, *, or \
/")
        user_input = input("Pick an operation.\n")
        get_operator(user_input)


def process_equation(first_number, operator, second_number):
    """Returns a solution."""
    if operator == "+":
        solution = (first_number + second_number)
    elif operator == "-":
        solution = (first_number - second_number)
    if operator == "*":
        solution = (first_number * second_number)
    if operator == "/":
        solution = (first_number / second_number)
    return solution


def run_again(first_number):
    """Takes in a number, gets operator and second number, runs equation and
       prints out the solution.
    """
    while True:
        user_input = input(f"Type 'y' to continue calculating with \
{first_number}, or type 'n' to start a new calculation.\n")
        if user_input == "y":
            operator_input = input("Pick an operation.\n")
            operator = get_operator(operator_input)
            second_number_input = input("What's the second number?\n")
            second_number = get_number(second_number_input)
            solution = process_equation(first_number, operator, second_number)
            print(f"{str(first_number)} {operator} {str(second_number)} = \
    {str(solution)}")
            return run_again(solution)
        elif user_input == "n":
            first_number_input = input("What's the first number?\n")
            first_number = get_number(first_number_input)
            return run_again(first_number)
        else:
            print("Sorry, I don't know what that means. Please choose y or n.")
            continue


while True:
    first_number_input = input("What's the first number?\n")
    first_number = get_number(first_number_input)
    operator_input = input("Pick an operation.\n")
    operator = get_operator(operator_input)
    second_number_input = input("What's the second number?\n")
    second_number = get_number(second_number_input)
    solution = process_equation(first_number, operator, second_number)
    print(f"{str(first_number)} {operator} {str(second_number)} = \
{str(solution)}")
    run_again(solution)
