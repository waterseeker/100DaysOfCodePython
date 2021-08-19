## Debug Leap Year

# Instructions

# - Read this the code in main.py
# - Spot the problems 🐞. 
# - Modify the code to fix the program. 
# - No shortcuts - don't copy-paste to replace the code entirely with a working solution. 

# Fix the code so that it works.

# year = input("Which year do you want to check?")

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")

# # Describe the bug.
#   When running the program with the input 1999, it throws an error:
#       TypeError: not all arguments converted during string formatting
#   This is because the user input is not cast to an int.
# # Reproduce the bug.
# x = '1'
# if x % 1 == 0:
#     print('test')
# # Fix the bug.
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")