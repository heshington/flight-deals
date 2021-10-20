from data_manager import DataManager

class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self, price, deperature_airport_code, departure_city):
        self.deperature_airport_code = deperature_airport_code,
        self.deperature_airport_code = departure_city


    data_manager = DataManager()
    flight_data = data_manager.get_data()
    print(flight_data)
