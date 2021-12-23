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

# get first number input
first_number = float(input("What's the first number?\n"))
# check that it's a number (make this a function)
try:
    if float(i).is_integer():
        print("integer")
    else:
        print("float")
except ValueError:
    print("not integer or float")
#   if not, error message
#   if so, continue
# get the operator
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
