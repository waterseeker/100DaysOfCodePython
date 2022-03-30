from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

# TODO add a country column to google sheet to help with search by city name

ticket_list = []

data_manager = DataManager()
data_manager.get_all_lines()
data_manager.put_missing_iata_codes()
flight_data = FlightData()
flight_search = FlightSearch()
if len(ticket_list) > 0:
    notification_manager = NotificationManager(ticket_list)
