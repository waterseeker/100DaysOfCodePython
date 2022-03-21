import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
RECEIVING_PHONE_NUMBER = os.getenv("RECEIVING_PHONE_NUMBER")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, ticket_list):
        self.ticket_list = ticket_list
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_message(self, ticket_list):
        for ticket in ticket_list:
            price = ticket['price']
            origination = ticket['origination']
            destination = ticket['destination']
            travel_date = ticket['date']
            message_body = f"Low price alert! Only ${price} to fly from {origination} to {destination}, from {travel_date}."
            self.client.messages.create(
                body=message_body,
                from_=TWILIO_PHONE_NUMBER,
                to=RECEIVING_PHONE_NUMBER
            )
