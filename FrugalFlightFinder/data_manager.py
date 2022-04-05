import os
import requests
from dotenv import load_dotenv
import csv

load_dotenv()
SHEETY_PUT_ENDPOINT = os.getenv("SHEETY_PUT_ENDPOINT")
SHEETY_AUTH_TOKEN = os.getenv("SHEETY_AUTH_TOKEN")
sheety_headers = {
    "Authorization": f"Bearer {SHEETY_AUTH_TOKEN}"
}


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
        with open('cleaned_airport_data.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
        csv_data = data
        cleaned_csv_data = [{"city": entry[3].strip(), "country": entry[2].strip(), "iata_code": entry[4].strip()} for
                            entry in
                            csv_data]
        missing_iata_codes = [{"city": destination['city'], "country": destination['country'], "id": destination["id"],
                               "targetPrice": destination["targetPrice"]}
                              for destination in
                              self.sheety_json['prices'] if
                              destination['iataCode'] == '']
        for destination in missing_iata_codes:
            airport_iata_code = [airport for airport in cleaned_csv_data if
                                 destination["city"] in airport["city"] and airport["country"] == destination[
                                     "country"]][0]["iata_code"]
            line_id = destination["id"]
            sheety_body = {
                "price": {
                    "city": destination["city"],
                    "iataCode": airport_iata_code,
                    "targetPrice": destination["targetPrice"],
                    "country": destination["country"],
                    "id": line_id
                }
            }
            sheety_put_endpoint = f"{SHEETY_PUT_ENDPOINT}/{line_id}"
            sheety_response = requests.put(url=sheety_put_endpoint, json=sheety_body, headers=sheety_headers)
            sheety_response.raise_for_status()
            print(sheety_response.status_code)


example_return_from_sheety_json = {
    'prices': [{'city': 'Paris', 'iataCode': 'LTQ', 'targetPrice': 54, 'country': 'FR', 'id': 2},
               {'city': 'Berlin', 'iataCode': 'SXF', 'targetPrice': 42, 'country': 'DE', 'id': 3},
               {'city': 'Tokyo', 'iataCode': 'NRT', 'targetPrice': 485, 'country': 'JP', 'id': 4},
               {'city': 'Sydney', 'iataCode': 'BWU', 'targetPrice': 551, 'country': 'AU', 'id': 5},
               {'city': 'Istanbul', 'iataCode': 'ISL', 'targetPrice': 95, 'country': 'TR', 'id': 6},
               {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'targetPrice': 414, 'country': 'MY', 'id': 7},
               {'city': 'New York', 'iataCode': 'JFK', 'targetPrice': 240, 'country': 'US', 'id': 8},
               {'city': 'San Francisco', 'iataCode': 'SFO', 'targetPrice': 260, 'country': 'US', 'id': 9},
               {'city': 'Cape Town', 'iataCode': 'CPT', 'targetPrice': 378, 'country': 'ZA', 'id': 10}]}
