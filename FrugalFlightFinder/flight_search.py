import requests
import os
from dotenv import load_dotenv

load_dotenv()
COMPARE_FLIGHT_PRICES_KEY = os.getenv("COMPARE_FLIGHT_PRICES_KEY")


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(self):
        self.headers = {
            'x-rapidapi-host': "compare-flight-prices.p.rapidapi.com",
            'x-rapidapi-key': COMPARE_FLIGHT_PRICES_KEY
        }
        self.flight_search_endpoint = "https://compare-flight-prices.p.rapidapi.com/GetPricesAPI/GetPrices.aspx"

    def search_flights(self, query_string):
        # querystring = {"SearchID": "<REQUIRED>"}
        querystring = query_string

        response = requests.request("GET", self.flight_search_endpoint, headers=self.headers, params=querystring)
        print(response.raise_for_status())
        print(response.text)
