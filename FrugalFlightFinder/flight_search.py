import requests
import os
from dotenv import load_dotenv

load_dotenv()
COMPARE_FLIGHT_PRICES_KEY = os.getenv("COMPARE_FLIGHT_PRICES_KEY")
HOME_CITY_IATA_CODE = os.getenv("HOME_CITY_IATA_CODE")

class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(self):
        self.headers = {
            'x-rapidapi-host': "compare-flight-prices.p.rapidapi.com",
            'x-rapidapi-key': COMPARE_FLIGHT_PRICES_KEY
        }
        self.start_flight_search_endpoint = "https://compare-flight-prices.p.rapidapi.com/GetPricesAPI/StartFlightSearch.aspx"
        self.flight_search_endpoint = "https://compare-flight-prices.p.rapidapi.com/GetPricesAPI/GetPrices.aspx"

    def start_flight_search(self, cities):
        for city in cities:
            querystring = {f"lapinfant": "0", "child": "0", "city2": {city["iata_code"]}, "date1": "2021-01-01",
                           "youth": "0", "flightType": "2", "adults": "1", "cabin": "3",
                           "infant": "0", "city1": {HOME_CITY_IATA_CODE}, "seniors": "0", "date2": "2021-01-02"}

            response = requests.request("GET", self.start_flight_search_endpoint, headers=self.headers,
                                        params=querystring)

            print(response.text)

    def search_flights(self, query_string):
        # querystring = {"SearchID": "<REQUIRED>"}
        querystring = query_string

        response = requests.request("GET", self.flight_search_endpoint, headers=self.headers, params=querystring)
        print(response.raise_for_status())
        print(response.text)
