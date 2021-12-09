import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
number_of_diners = len(names)
random_diner = names[random.randint(1, number_of_diners)]
print(f"{random_diner.title()} is going to buy the meal today!")
