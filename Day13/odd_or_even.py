# Debug Odd or Even

# Instructions

# - Read this the code in main.py
# - Spot the problems 🐞.
# - Modify the code to fix the program.

# Fix the code so that it works and passes the tests when you submit.

# number = int(input("Which number do you want to check?"))

# if number % 2 = 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

# # Describe the problem.
#   This code is showing an error in the syntax checker. 'unexpected token'
#   This is because the if statement is using assignment instead of equality.
# # Reproduce the bug.
# if 1 = 1:
#     print('stuff')
# # Fix the bug.
number = int(input("Which number do you want to check?"))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
