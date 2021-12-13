# Write your code below this row 👇

first_number = 1
last_number = 101
answer = sum(x for x in range(first_number, last_number) if x % 2 == 0)
print(f"The sum of all even numbers between {first_number} and {last_number} is {answer}")