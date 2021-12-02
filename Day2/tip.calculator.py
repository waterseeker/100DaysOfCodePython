# If the bill was $150.00, split between 5 people, with 12% tip. 

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some
# Googling to solve this.💪

# Write your code below this line 👇

print("Welcome to the tip calculator.")
bill_cents = int(float(input("What was the total bill? $")) * 100)
tip_percent = int(input("What percentage tip would you like to give? "
                  "10, 12, or 15? "))
num_diners = int(input("How many people to split the bill? "))
total_with_tip_cents = int(bill_cents + (bill_cents * (tip_percent / 100)))
individual_cost_cents = total_with_tip_cents / num_diners
individual_cost_dollars = "{:.2f}".format(individual_cost_cents / 100)

print(f"Each person should pay: ${individual_cost_dollars}")
