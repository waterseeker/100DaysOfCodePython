import os
import requests
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_auth_token = os.getenv("SHEETY_AUTH_TOKEN")
        self.sheety_get_endpoint = os.getenv("SHEETY_GET_ENDPOINT")
        self.sheety_headers = {
            "Authorization": f"Bearer {self.sheety_auth_token}",
        }
        self.sheety_json = {}

    def get_all_lines(self):
        sheety_response = requests.get(self.sheety_get_endpoint, headers=self.sheety_headers)
        sheety_response.raise_for_status()
        self.sheety_json = sheety_response.json()

    def put_missing_iata_codes(self):
        # missing_iata_codes = [{entry['city'], entry['country']} for entry in self.sheety_json['prices'] if
        #                       entry['iataCode'] == '']
        missing_iata_codes = [{entry['city'], entry['country']} for entry in example_response['prices'] if
                              entry['iataCode'] == '']
        print(missing_iata_codes)


# TODO create a method to consume cities missing IATA codes list and write IATA codes to their lines
# TODO create a method to change the lowest price for a city
# TODO create a method to add a line
# TODO create a method to edit a line
# TODO create a method to delete a line
# TODO create a method that will return a list of dictionaries containing all the info in the sheet

example_response = {'prices': [{'city': 'Paris', 'iataCode': '', 'targetPrice': 54, 'country': 'FR', 'id': 2},
                               {'city': 'Berlin', 'iataCode': '', 'targetPrice': 42, 'country': 'DE', 'id': 3},
                               {'city': 'Tokyo', 'iataCode': '', 'targetPrice': 485, 'country': 'JP', 'id': 4},
                               {'city': 'Sydney', 'iataCode': '', 'targetPrice': 551, 'country': 'AU', 'id': 5},
                               {'city': 'Istanbul', 'iataCode': '', 'targetPrice': 95, 'country': 'TR', 'id': 6},
                               {'city': 'Kuala Lumpur', 'iataCode': '', 'targetPrice': 414, 'country': 'MY', 'id': 7},
                               {'city': 'New York', 'iataCode': '', 'targetPrice': 240, 'country': 'US', 'id': 8},
                               {'city': 'San Francisco', 'iataCode': '', 'targetPrice': 260, 'country': 'US', 'id': 9},
                               {'city': 'Cape Town', 'iataCode': '', 'targetPrice': 378, 'country': 'ZA', 'id': 10}]}

e = DataManager()
e.put_missing_iata_codes()
example_missing_codes = [{'Paris', 'FR'}, {'Berlin', 'DE'}, {'Tokyo', 'JP'}, {'AU', 'Sydney'}, {'Istanbul', 'TR'},
                         {'Kuala Lumpur', 'MY'}, {'New York', 'US'}, {'San Francisco', 'US'}, {'Cape Town', 'ZA'}]
