# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = round(weight / height**2)
message = f"Your BMI is {bmi}, "
if bmi < 18.5:
    message += "you are underweight."
elif bmi < 25:
    message += "you have a normal weight."
elif bmi < 30:
    message += "you are slightly overweight."
elif bmi < 35:
    message += "you are obese."
else:
    message += "you are clinically obese."
print(message)
