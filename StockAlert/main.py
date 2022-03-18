import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client
from datetime import datetime, timedelta

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
RECEIVING_PHONE_NUMBER = os.getenv('RECEIVING_PHONE_NUMBER')
STOCK_SYMBOL = os.getenv('STOCK_SYMBOL')
COMPANY_NAME = os.getenv('COMPANY_NAME')
ALPHAVANTAGE_API_KEY = os.getenv('ALPHAVANTAGE_API_KEY')
ALPHAVANTAGE_BASE_URL = "https://www.alphavantage.co/query"
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# # ## STEP 1: Use https://www.alphavantage.co
# # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_SYMBOL,
    "apikey": ALPHAVANTAGE_API_KEY,
}
alphavantage_response = requests.get(ALPHAVANTAGE_BASE_URL, params=parameters)
alphavantage_response.raise_for_status()
stock_data = alphavantage_response.json()

day_prices = {day: day_info for day, day_info in stock_data["Time Series (Daily)"].items()}

today = datetime.now()
yesterday = str(today - timedelta(days=1)).split()[0]
day_before_yesterday = str(today - timedelta(days=2)).split()[0]

yesterdays_close_price = float(day_prices[yesterday]["4. close"])
day_before_yesterdays_close_price = float(day_prices[day_before_yesterday]["4. close"])
difference_in_prices = (yesterdays_close_price - day_before_yesterdays_close_price)
percentage_difference = (difference_in_prices / day_before_yesterdays_close_price) * 100
rounded_percentage_difference = round(percentage_difference, 2)

if percentage_difference > 5 or percentage_difference < -5:
    # ## STEP 2: Use https://newsapi.org
    # Get the first 3 news pieces for the COMPANY_NAME.
    NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
    news_parameters = {
        "q": COMPANY_NAME,
        "searchin": "title",
        "from": day_before_yesterday,
        "language": "en",
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY,
    }
    news_api_response = requests.get(NEWS_API_ENDPOINT, params=news_parameters)
    news_api_response.raise_for_status()
    first_3_articles = news_api_response.json()["articles"][:3]

    # ## STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.
    for article in first_3_articles:
        if percentage_difference > 0:
            change_direction_image = "🔺"
        else:
            change_direction_image = "🔻"
        headline = article["title"]
        brief = article["description"]
        message_body = f"{STOCK_SYMBOL}: {change_direction_image}{rounded_percentage_difference}%\nHeadline: {headline}\nBrief: {brief}"
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to=RECEIVING_PHONE_NUMBER
        )
