import os
from dotenv import load_dotenv
import requests
from collections import Counter

load_dotenv()
API_KEY = os.getenv('API_KEY')
MY_LATITUDE = os.getenv('MY_LATITUDE')
MY_LONGITUDE = os.getenv('MY_LONGITUDE')
OPEN_WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": API_KEY
}

request = requests.get(OPEN_WEATHER_ENDPOINT, params=parameters)
request.raise_for_status()
request_json = request.json()
hourly_forecasts = request_json["hourly"]
average_temp_48_hour = sum([x["temp"] for x in hourly_forecasts]) / len(hourly_forecasts)
conditions = (day["weather"][0]["description"] for day in hourly_forecasts)
counter = Counter(conditions)
most_common_condition = counter.most_common(1)[0][0]

print(f"48 hour average temp : {average_temp_48_hour}")
print(f"The most common weather condition for the past 48 hours was: {most_common_condition}")
