# Goal:
# Use pandas to:
#   create a csv from the squirrel data names 'squirrel_count.csv' that has a small table that contains:
#       fur color (this is logged as "Primary Fur Color" in the census data
#       total for each fur color
# You should create the final csv file from a DataFrame
import pandas

# make a dict where the fur colors are the keys and the total squirrels with that color of fur are the values
squirrel_data = pandas.read_csv("squirrel_data.csv")

gray_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")