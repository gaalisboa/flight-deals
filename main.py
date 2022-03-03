import os
from dotenv import load_dotenv
load_dotenv()

from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from flight_data import FlightData


SHEETY_ENDPOINT = os.getenv('SHEETY_ENDPOINT')

search_tool = FlightSearch()
print(search_tool.get_destination_code("London"))