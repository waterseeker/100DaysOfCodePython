# Challenge: Open up the weather_data.csv file with open and save each line in a list called data
with open("weather_data.csv") as file:
    data = file.readlines()
    stripped_data = [line.strip() for line in data]
    print(stripped_data)
