# Instructions
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
#
# You are going to create a list called result which contains the numbers that are common in both files.
#
# e.g. if file1.txt contained:
#
# 1
# 1
# 2
# 2
# 3
# 3
# and file2.txt contained:
#
# 2
# 2
# 3
# 3
# 4
# 4
# result = [2, 3]
# result = [2, 3]
# IMPORTANT: The result should be a list that contains Integers, not Strings. Try to use List Comprehension instead of a Loop.
#
# Example Output
# [3, 6, 5, 33, 12, 7, 42, 13]
# [3, 6, 5, 33, 12, 7, 42, 13]

with open("file1.txt") as file1:
    file1_list = [int(num) for num in file1.readlines()]
with open("file2.txt") as file2:
    file2_list = [int(num) for num in file2.readlines()]

result = [num for num in file1_list if num in file2_list]
print(result)
