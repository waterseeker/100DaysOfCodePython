import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv('API_KEY')
MY_LATITUDE = os.getenv('MY_LATITUDE')
MY_LONGITUDE = os.getenv('MY_LONGITUDE')
parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": API_KEY
}

request = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
request.raise_for_status()
request_json = request.json()
hourly_forecasts = request_json["hourly"]
