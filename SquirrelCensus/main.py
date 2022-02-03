# Goal:
# Use pandas to:
#   create a csv from the squirrel data names 'squirrel_count.csv' that has a small table that contains:
#       fur color (this is logged as "Primary Fur Color" in the census data
#       total for each fur color
# You should create the final csv file from a DataFrame
import pandas

# make a dict where the fur colors are the keys and the total squirrels with that color of fur are the values
squirrel_data = pandas.read_csv("squirrel_data.csv")

# drop rows with NaN
only_fur_colors = squirrel_data["Primary Fur Color"].dropna()

# get only unique values and their counts
counts = only_fur_colors.value_counts()

# turn counts into a dataframe
counts_data_frame = pandas.DataFrame(counts)

# turn dataframe into a csv
counts_csv = counts_data_frame.to_csv("squirrel_count.csv")
