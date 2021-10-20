#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch

data_manager = DataManager()
#sheet_data = data_manager.get_data()
search_flight = FlightSearch()



#print(sheet_data[0])
destination_cities = ['Paris', 'Berlin', 'Tokyo', 'Sydney', 'Istanbul', 'Kuala Lumpur', 'New York', 'San Francisco', 'Cape Town']
destination_codes = ["CDG", "BER", "HND", "SYD" "SAW" "KUL" "EWR" "SFO" "CPT"]
# i = 0
# while i < len(sheet_data):
#     if sheet_data[i]['iataCode'] == "":
#         sheet_data[i]['iataCode'] = search_flight.get_airport_code(sheet_data[i]['city'])
#         destination_cities.append(sheet_data[i]['city'])
#     i += 1

# data_manager.destination_data = sheet_data
data_manager.update_row()

print(destination_cities)
for city in destination_codes:
    flight = search_flight.get_flight_prices(city)
    print(flight)










