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
def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()


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
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])



# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])