import json
import os
from dotenv import load_dotenv
load_dotenv()

import requests

SHEETY_ENDPOINT = os.getenv('SHEETY_ENDPOINT')

class DataManager:
    def __init__(self) -> None:
        pass

    def get_data(self):
        data = requests.get(url=SHEETY_ENDPOINT).json()
        return data['prices']