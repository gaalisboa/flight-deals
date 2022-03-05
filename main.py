import os
from dotenv import load_dotenv
load_dotenv()

from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from flight_data import FlightData


flight_search = FlightSearch()
data_manager = DataManager()

sheety_data = data_manager.get_data()

for row in sheety_data:
    row['iataCode'] = flight_search.get_destination_code(row['city'])

print(sheety_data)