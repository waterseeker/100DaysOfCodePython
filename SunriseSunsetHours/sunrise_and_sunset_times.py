import requests
from datetime import datetime

MY_LAT = 60.169857
MY_LONG = 24.938379

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunrise_hour = sunrise.split("T")[1].split(":")[0]

sunset = data["results"]["sunset"]
sunset_hour = sunset.split("T")[1].split(":")[0]

current_hour = datetime.now().hour

print(sunset_hour)
