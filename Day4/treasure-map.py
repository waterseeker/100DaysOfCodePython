# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
# first digit of position is the vertical coordinate
# second digit of position is the horizontal coordinate
# example input = 31
# example output
# ['⬜️', '⬜️', 'X']

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']
row = int(position[-1]) - 1
column = int(position[0]) - 1
map[row][column] = "X"

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
