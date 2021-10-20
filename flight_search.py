from decouple import config
import requests


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

