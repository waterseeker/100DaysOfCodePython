#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
# This is assuming the user just inputs a number, no %
tip_percentage = input("What percentage tip would you like to give?")
number_of_diners = input("How many people to split the bill? ")

total_as_float = float(total_bill)
tip_percentage_as_float = float(tip_percentage)
number_of_diners_as_int = int(number_of_diners)
tip_as_decimal = tip_percentage_as_float / 100
tip = total_as_float * tip_as_decimal
total_bill_with_tip = total_as_float + tip
total_per_diner = round(total_bill_with_tip / number_of_diners_as_int, 2)
formatted_total_per_diner = "{:.2f}".format(total_per_diner)
print(f"Each person should pay: ${formatted_total_per_diner}")
    