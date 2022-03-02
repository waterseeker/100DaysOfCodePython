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
    "exclude": ,
    "appid": API_KEY
}
request = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
f"https://api.openweathermap.org/data/2.5/onecall?lat={MY_LATITUDE}&lon={MY_LONGITUDE}&exclude={part}&appid={API_KEY}"
