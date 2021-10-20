from decouple import config
import requests
from datetime import datetime, timedelta

class FlightSearch:



    def get_airport_code(self, city):
        flight_url_endpoint = "https://tequila-api.kiwi.com/locations/query"
        headers = {
            "apikey": config('FLIGHT_API_KEY')
        }

        parameters = {
            "term": city,
            "location_types": "airport"
        }

        response = requests.get(flight_url_endpoint, params=parameters, headers=headers)
        data = response.json()

        return(data.get('locations')[0].get('id'))

    def get_flight_prices(self, destination):
        headers = {
            "apikey": config('FLIGHT_API_KEY')
        }
        end_point_search_url = "https://tequila-api.kiwi.com/v2/search/"
        todays_date = datetime.now()
        six_months_from_now = todays_date + timedelta(days=90)
        todays_date_formatted = todays_date.strftime("%d/%m/%Y")
        six_months_from_now_formatted = six_months_from_now.strftime("%d/%m/%Y")

        parameters = {

            "fly_from": "LCY",
            "fly_to": destination,
            "date_from": todays_date_formatted,
            "date_to": six_months_from_now_formatted,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": 0,
            "flight_type": "round",
            "curr": "GBP"
        }
        response = requests.get(end_point_search_url, params=parameters, headers=headers)
        data = response.json()

        return data


