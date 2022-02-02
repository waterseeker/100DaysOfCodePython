# # Challenge: Open up the weather_data.csv file with open and save each line in a list called data
# with open("weather_data.csv") as file:
#     data = file.readlines()
#     stripped_data = [line.strip() for line in data]
#     print(stripped_data)

# # Python has a built-in library called csv that makes it easier to handle csv files
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row)

# # Challenge: using the csv.reader() create a new list called temperatures that contains all of the temps in
# # weather_data.csv as ints not strings
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     rows = [row for row in data]
#     temperatures = []
#     for row in rows[1:]:
#         temperatures.append(int(row[1]))
#     print(temperatures)

# but this is pretty cumbersome to just access a few lines of data. Using Pandas makes it even easier.
import pandas

data = pandas.read_csv("weather_data.csv")
# to do what we did using csv.reader above
print(data["temp"])
