from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

ticket_list = []

data_manager = DataManager()
flight_data = FlightData()
flight_search = FlightSearch()
if len(ticket_list) > 0:
    notification_manager = NotificationManager(ticket_list)
