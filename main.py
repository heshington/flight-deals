#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_data()
search_flight = FlightSearch()
# code = search_flight.get_airport_code("Wellington")


print(sheet_data[0])

i = 0
while i < len(sheet_data):
    if sheet_data[i]['iataCode'] == "":
        sheet_data[i]['iataCode'] = search_flight.get_airport_code(sheet_data[i]['city'])
    print(f"sheet_data: \n {sheet_data}")
    i += 1

data_manager.destination_data = sheet_data
data_manager.update_row()










