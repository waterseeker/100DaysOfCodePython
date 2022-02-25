import requests
from datetime import datetime
import os
from dotenv import load_dotenv
import smtplib
import time

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude
load_dotenv()
my_email = os.getenv("MY_EMAIL")
my_email_2 = os.getenv("MY_EMAIL_2")
password = os.getenv("EMAIL_PASSWORD")
receiving_email = os.getenv("RECEIVING_EMAIL")
smtp_address = os.getenv("SMTP_ADDRESS")
smtp_address_2 = os.getenv("SMTP_ADDRESS_2")
app_password = os.getenv("APP_PASSWORD")
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def iss_is_overhead(my_lat, my_long):
    """Returns True if current ISS position is within 5 degrees of long and lat parameters"""
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    if my_lat - 5 <= iss_latitude <= my_lat + 5 and my_long - 5 <= iss_longitude <= my_long + 5:
        return True
    return False


def is_dark(sunrise_sunset_api_params):
    """Returns True if it is currently between sunset and sunrise hours at passed in lat and long"""
    dark_response = requests.get("https://api.sunrise-sunset.org/json", params=sunrise_sunset_api_params)
    dark_response.raise_for_status()
    dark_data = dark_response.json()
    sunrise_hour = int(dark_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(dark_data["results"]["sunset"].split("T")[1].split(":")[0])

    current_hour = datetime.now().hour
    if current_hour >= sunset_hour or current_hour <= sunrise_hour:
        return True
    return False


while True:
    time.sleep(60)
    if iss_is_overhead(MY_LAT, MY_LONG) and is_dark(parameters):
        with smtplib.SMTP(smtp_address) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                msg=f"ISS OVERHEAD!!!\n\nLook up! The ISS is above you and should be visible!")
