import os
from dotenv import load_dotenv
import requests
from collections import Counter
from twilio.rest import Client

load_dotenv()
TWILIO_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
RECEIVING_PHONE_NUMBER = os.getenv('RECEIVING_PHONE_NUMBER')
STOCK = os.getenv('STOCK')
COMPANY_NAME = os.getenv('COMPANY_NAME')
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
# ## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# ## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# ## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
change_percentage = 0
change_direction_image = "🔻"
if change_percentage > 0:
    change_direction_image = "🔺"
message_body = f"{STOCK}: {change_direction_image}{change_percentage}"
message = client.messages.create(
    body=message_body,
    from_=TWILIO_PHONE_NUMBER,
    to=RECEIVING_PHONE_NUMBER
)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to
file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height
of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to
file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height
of the coronavirus market crash.
"""
