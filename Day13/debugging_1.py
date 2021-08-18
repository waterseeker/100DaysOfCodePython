############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()
# The desired result is to get the print statement to run. 
# It's not running because the range function's second parameter is non-inclusive.
# So, i never == 20. The loop stops at 19.
# # Solve Problem
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()
# ------------------------------------------------------------------------------

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])
# # Describe Problem
#   If you run this many times, occasionally you'll get an error 
#       IndexError: list index out of range.
#   This is because of 0 based indexing. randint(1, 6) will return numbers from 1 to 6
#       with both numbers being inclusive. I.E. (1, 2, 3, 4, 5, 6).
#   The dice_imgs list holds 6 entries, but the indexes start at 0.
#   So the indexes are (0, 1, 2, 3, 4, 5). There is no 6 index.
# # Reproduce the Bug
#   You can reproduce this buy by trying to print index 6 from dice_imgs.
#   print(dice_imgs[6])
#   So when randint returns a 6, it is throwing the list index out of range error.
# # # Solve Problem
#   One way to solve this is to change randint(1, 6) to randint(0, 5)
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])
# ------------------------------------------------------------------------------

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
# # Describe Problem
#   When the user enters 1994, for example, there is nothing printed out to the console.
#   The desired behavior is to have the program print "You are a Gen Z."
#   This is because there is no condition where the input is == 1994, only 
#       if it's greater than or less than 1994.
# # Reproduce the Bug
# x = 2
# if x > 1 and x < 2:
#     print('Test')
# # # Solve Problem
# You can solve this by including 1994 in the Gen Z condition.
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")
# ------------------------------------------------------------------------------

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")
# # Describe Problem
#   There is an 'expected an indented block' error in this code.
#   This is because the print statement should be nested inside the if block.
# # Reproduce the Bug
# x = 1
# if x == 1:
# print('something')
# # # Solve Problem
#   You can solve the 'expected an indented block' error in the code by 
#       indenting the print statement.
# age = input("How old are you?")
# if age > 18:
#     print("You can drive at age {age}.")
#   However, when you run this code you get another error.
#       TypeError: '>' not supported between instances of 'str' and 'int'
#   This is because the input is not being case to an int.
#   You can solve this by casting the input to an int.
# age = int(input("How old are you?"))
# if age > 18:
#     print("You can drive at age {age}.")
#   There is then another problem with the code. That is the expected output
#       of the print statement should include the age variable. 
#   However, the print statement is not using an f string syntax so the variable
#       name is getting printed out "{age}" instead of the input.
#   You can fix this by changing the print statement to us an f string.
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")
# ------------------------------------------------------------------------------


# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# # Describe Problem
#   No matter what you input here, the result is 0.
#   This is because the value of word_per_page is always 0
# # Reproduce the Bug
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# print(word_per_page)
# # Solve Problem
#   You can fix this but changing == to = on the line that is supposed to be
#       assigning the user's input to word_per_page
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
# ------------------------------------------------------------------------------

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])