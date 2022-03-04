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

response = requests.get(OPEN_WEATHER_ENDPOINT, params=parameters)
response.raise_for_status()
response_json = response.json()
hourly_forecasts = response_json["hourly"]
average_temp_48_hour = sum([x["temp"] for x in hourly_forecasts]) / len(hourly_forecasts)
conditions = (day["weather"][0]["description"] for day in hourly_forecasts)
counter = Counter(conditions)
most_common_condition = counter.most_common(1)[0][0]

print(f"Response status code: {response.status_code}")
print(f"48 hour average temp will be: {average_temp_48_hour}")
print(f"The most common weather condition for the next 48 hours will be: {most_common_condition}")
