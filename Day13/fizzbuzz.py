# ## Debug FizzBuzz

# # Instructions

# - Read this the code
# - Spot the problems 🐞.
# - Modify the code to fix the program.
# - No shortcuts  - don't copy-paste to replace the code entirely with a
#       working solution.

# The code needs to print the solution to the FizzBuzz game.

# > `Your program should print each number from 1 to 100 in turn.`

# > `When the number is divisible by 3 then instead of printing the number
#        it should print "Fizz".`

# > `When the number is divisible by 5, then instead of printing the number
#        it should print "Buzz".`

# >       `And if the number is divisible by both 3 and 5 e.g. 15 then instead
#              of the number it should print "FizzBuzz"`

# # Hint

# There is more than one fix required.

# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])

# # Describe the bug.
# #1. For 3, the program is returning 'FizzBuzzz' and it should be returning
#         'Fizz'
#   This is because the OR statement should be an AND statement.
#   Also, the program is printing out the numbers like this '[2]'.
#   This is because of the print statement being passed [number] instead of
#       just number.
# # Reproduce the bug.
# x = 3
# if x % 3 == 0 or x % 5 == 0:
#     print("FizzBuzz")
# # Fix the bug.
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     if number % 3 == 0:
#         print("Fizz")
#     if number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
# # Describe the bug.
# #2. For 21, the program is returning 'Fizz' and printing 21.
#   This is because the if statements after the first one should be elifs.
# # Reproduce the bug.
# for number in range(21,22):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     if number % 3 == 0:
#         print("Fizz")
#     if number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
# # Fix the bug.
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
