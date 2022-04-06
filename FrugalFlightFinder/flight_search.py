import requests
import os
from dotenv import load_dotenv
import datetime
from dateutil.relativedelta import relativedelta

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
        # TODO make this consume a list of dicts like
        #   example_return_from_sheety_json = {
        #     'prices': [{'city': 'Paris', 'iataCode': 'LTQ', 'targetPrice': 54, 'country': 'FR', 'id': 2},
        #                {'city': 'Berlin', 'iataCode': 'SXF', 'targetPrice': 42, 'country': 'DE', 'id': 3},
        #                {'city': 'Tokyo', 'iataCode': 'NRT', 'targetPrice': 485, 'country': 'JP', 'id': 4},
        #                {'city': 'Sydney', 'iataCode': 'BWU', 'targetPrice': 551, 'country': 'AU', 'id': 5},
        #                {'city': 'Istanbul', 'iataCode': 'ISL', 'targetPrice': 95, 'country': 'TR', 'id': 6},
        #                {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'targetPrice': 414, 'country': 'MY', 'id': 7},
        #                {'city': 'New York', 'iataCode': 'JFK', 'targetPrice': 240, 'country': 'US', 'id': 8},
        #                {'city': 'San Francisco', 'iataCode': 'SFO', 'targetPrice': 260, 'country': 'US', 'id': 9},
        #                {'city': 'Cape Town', 'iataCode': 'CPT', 'targetPrice': 378, 'country': 'ZA', 'id': 10}]}

        # TODO make dates dynamic according to current date, should look 6 months out from current date in the format:
        #   "2021-01-01"
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        tomorrow_as_string = str(tomorrow)
        four_days_after_today = today + datetime.timedelta(days=4)
        four_days_after_today_as_string = str(four_days_after_today)
        six_months_time_delta = relativedelta(months=6)
        six_months_from_today = today + six_months_time_delta

        for city in cities:
            # api paramaters at https://rapidapi.com/obryan-software-obryan-software-default/api/compare-flight-prices/
            # date1 is departure date and required
            # date2 is return date and looks like it's required too
            # cabin is an enum and required
            #   1 = economy
            #   2 = business
            #   3 = first
            #   4 = premium economy
            querystring = {f"lapinfant": "0", "child": "0", "city2": {city["iataCode"]}, "date1": {tomorrow_as_string},
                           "youth": "0", "flightType": "2", "adults": "1", "cabin": "1",
                           "infant": "0", "city1": {HOME_CITY_IATA_CODE}, "seniors": "0",
                           "date2": {four_days_after_today_as_string},
                           "islive": "true"}

            response = requests.request("GET", self.start_flight_search_endpoint, headers=self.headers,
                                        params=querystring)

            print(response.text)

    def search_flights(self, query_string):
        # querystring = {"SearchID": "<REQUIRED>"}
        querystring = query_string

        response = requests.request("GET", self.flight_search_endpoint, headers=self.headers, params=querystring)
        print(response.raise_for_status())
        print(response.text)


# test_cities = [{'city': 'Paris', 'iataCode': 'LTQ', 'targetPrice': 54, 'country': 'FR', 'id': 2}]
test_flight_search = FlightSearch()

# should return a search id to be used by another api call
# test_flight_search.start_flight_search(test_cities)

TEST_SEARCH_ID = os.getenv("TEST_SEARCH_ID")
flight_search_query_string = {
    "SearchID": TEST_SEARCH_ID
}
# TODO debug why api is returning empty list
test_flight_search.search_flights(flight_search_query_string)
#   returned:
#   "None
#   []"
