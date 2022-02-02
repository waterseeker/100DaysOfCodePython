# # Challenge: Open up the weather_data.csv file with open and save each line in a list called data
# with open("weather_data.csv") as file:
#     data = file.readlines()
#     stripped_data = [line.strip() for line in data]
#     print(stripped_data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(row)

# Challenge: using the csv.reader() create a new list called temperatures that contains all of the temps in
# weather_data.csv as ints not strings
