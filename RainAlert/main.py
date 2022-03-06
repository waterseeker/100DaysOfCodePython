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
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

response = requests.get(OPEN_WEATHER_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_forecasts = weather_data["hourly"]
average_temp_48_hour = sum([x["temp"] for x in hourly_forecasts]) / len(hourly_forecasts)
conditions = (day["weather"][0]["description"] for day in hourly_forecasts)
counter = Counter(conditions)
most_common_condition = counter.most_common(1)[0][0]
# check if weather code is less than 700 in the next 12 hours, if so, alert the user they need to bring an umbrella
next_12_hours = [hour["weather"][0]["id"] for hour in hourly_forecasts[:12]]
will_rain = False
for weather_id in next_12_hours:
    if int(weather_id) < 700:
        will_rain = True
if will_rain:
    print("You'll need to bring an umbrella")
print(f"Response status code: {response.status_code}")
print(f"48 hour average temp will be: {average_temp_48_hour}")
print(f"The most common weather condition for the next 48 hours will be: {most_common_condition}")
