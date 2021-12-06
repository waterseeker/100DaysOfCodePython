# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
t_occurs = name1.count("t") + name2.count("t")
r_occurs = name1.count("r") + name2.count("r")
u_occurs = name1.count("u") + name2.count("u")
e_occurs = name1.count("e") + name2.count("e")
first_digit = t_occurs + r_occurs + u_occurs + e_occurs
l_occurs = name1.count("l") + name2.count("l")
o_occurs = name1.count("o") + name2.count("o")
v_occurs = name1.count("v") + name2.count("v")
second_digit = l_occurs + o_occurs + v_occurs + e_occurs
love_score = first_digit * 10 + second_digit

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
