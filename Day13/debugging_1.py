# ###########DEBUGGING#####################

# # Describe Problem


def my_function():
    for i in range(1, 20):
        # i will never == 20 because the second parameter of the range function
        # is exclusive. This range call will only return 1-19.
        if i == 20:
            print("You got it")


# to fix this, just add 1 to the second parameter of range()
def fixed_my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it.")


fixed_my_function()

# Reproduce the Bug
# This code is erroring out sometimes.
# That is because the index for a list is 0-based. So whenever dice_num is 6,
# there is no element at index 6 in the list.
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])
# To reproduce this bug, you could hard-code the value of dice_num to 6
# and see that it is erroring out every time you run this.

# This errors out every time
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = 6
# print(dice_imgs[dice_num])

# # To fix this, you can subtract 1 from the dice_num
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) - 1
# print(dice_imgs[dice_num])
# # or you could change the randint call to be from 0 to 5
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")
# The bug is that nothing happens if you input 1994
# That's because there is never a check if the user input is = 1994
# You can fix that by changing one of the conditions to include 1994
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year >= 1994:
#     print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# Using the print statement, you see that total_words is always = 0. That's
# because of the == operator on the words_per_page line. It's not an
# assignment so the value of words_per_page is always 0, which makes the
# total_words also always be 0. 
# You can fix this by changing the == to =
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger


# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#     b_list.append(new_item)
#     print(b_list)


# mutate([1, 2, 3, 5, 8, 13])
# This isn't working right because the .append() is not happening on every 
# iteration of the for loop. It's been put outside the scope of the for loop, 
# so it's only running one time, after the for loop has finished. 
# You can fix this by indenting the .append() call into the scope of the for
# loop.


def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
