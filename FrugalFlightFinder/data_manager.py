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
        missing_iata_codes = [{entry['city'], entry['id']} for entry in self.sheety_json['prices'] if
                              entry['iataCode'] == '']


# TODO create a method to consume cities missing IATA codes list and write IATA codes to their lines
# TODO create a method to change the lowest price for a city
# TODO create a method to add a line
# TODO create a method to edit a line
# TODO create a method to delete a line
# TODO create a method that will return a list of dictionaries containing all the info in the sheet

example_response = {'prices': [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2},
                               {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3},
                               {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4},
                               {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5},
                               {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6},
                               {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7},
                               {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8},
                               {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9},
                               {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]}

print(missing_iata_codes)
