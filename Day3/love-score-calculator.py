# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
combined_names = name1 + name2
lowercase_names = combined_names.lower()
t_occurs = lowercase_names.count("t")
r_occurs = lowercase_names.count("r")
u_occurs = lowercase_names.count("u")
e_occurs = lowercase_names.count("e")
first_digit = t_occurs + r_occurs + u_occurs + e_occurs
l_occurs = lowercase_names.count("l")
o_occurs = lowercase_names.count("o")
v_occurs = lowercase_names.count("v")
second_digit = l_occurs + o_occurs + v_occurs + e_occurs
love_score = first_digit * 10 + second_digit

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
