import pandas

# You can loop through a pandas dataframe

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Examples of looping through a dictionary:
for (key, value) in student_dict.items():
    print(value)

for (key, value) in student_dict.items():
    print(key)

# Looping through a dataframe is the same. You can think of a pandas dataframe as a dictionary
df = pandas.DataFrame(student_dict)
for (key, value) in df.items():
    # the keys are the titles of the columns
    print(f"df key is: {key}")
    # the values are the data in the columns
    print(f"df value is: {value}")

# pandas has a built-in loop called iterrows that is more useful
# this loops through each of the rows instead of each of the columns
for (index, row) in df.iterrows():
    print(f"iterrows index is: {index}")
    print(f"iterrows row is: {row}")
    # You can use dot notation to access values of a particular column in the df
    print(f"the score is: {row.score}")

# You can combine these with conditionals too
for (index, row) in df.iterrows():
    if row.student != "Angela":
        print(f"using a conditional: {row.score}")
