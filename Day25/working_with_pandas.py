import pandas

# Pandas uses 2 main data types.
# The Series, which is analogous to a single column in a table
# and the DataFrame which is analogous to a table.
data = pandas.read_csv("weather_data.csv")
# the data type of print(type(data)) is DataFrame
# the data type of print(type(data["temp"])) is Series

# Pandas has a lot of methods to convert a Data Frame to other Python data types.
# for example, a dict
data_dict = data.to_dict()
print(data_dict)

# you can convert a Series to a list by doing...
series_list = data["temp"].to_list()
print(series_list)

# Challenge:
# Calculate the average temperature from the temp data
average_temp = round(sum(series_list) / len(series_list), 2)
print(f"the average temperature is: {average_temp}")
