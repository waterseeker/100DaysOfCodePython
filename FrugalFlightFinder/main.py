from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

# TODO add a country column to google sheet to help with search by city name

ticket_list = []

data_manager = DataManager()

# read sheety data
data_manager.get_all_lines()

# add missing iata codes in sheety data
data_manager.put_missing_iata_codes()

# update data manager with new sheety info after any missing iata codes are added
data_manager.get_all_lines()

flight_data = FlightData()
flight_search = FlightSearch()

if len(ticket_list) > 0:
    notification_manager = NotificationManager(ticket_list)
