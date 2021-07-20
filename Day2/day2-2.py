# Instructions

# Write a program that calculates the Body Mass Index (BMI) 
# from a user's weight and height.

# The BMI is a measure of some's weight taking into account their height. 
# e.g. If a tall person and a short person both weigh the same amount, 
# the short person is usually more overweight.

# The BMI is calculated by dividing a person's weight (in kg) 
# by the square of their height (in m):

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# This exercise is assuming the user is passing appropriate data for inputs
# BMI should be converted to a whole number
height_cast_to_float = float(height)
weight_cast_to_int = int(weight)
user_bmi = int(weight_cast_to_int / height_cast_to_float ** 2)
print("Your bmi is : " + str(user_bmi))