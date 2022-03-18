# TODO create a client with .env variables
# TODO create format for message
# TODO create send message method

import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
RECEIVING_PHONE_NUMBER = os.getenv("RECEIVING_PHONE_NUMBER")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    pass
