# assumptions for this exercise
# 365 days in a year
# 52 weeks in a year
# 12 months in a year
# you will live 90 years
# ignore differences for leap years in this exercise

# 🚨 Don't change the code below 👇
age = int(input("What is your current age?"))
# 🚨 Don't change the code above 👆

years = 90 - age
days = years * 365
weeks = years * 52
months = years * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
