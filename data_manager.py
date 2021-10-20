from decouple import config
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

        # Get from spreadsheet
    def get_data(self):
        end_point_url = "https://api.sheety.co/3a57a1832d829121cd2f4b974397be4e/flightDeals/prices"

        response = requests.get(url=end_point_url)
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data


    def update_row(self):
        end_point_url = f"https://api.sheety.co/3a57a1832d829121cd2f4b974397be4e/flightDeals/prices/"

        print(end_point_url)
        print(self.destination_data)
        headers = {
            "Content-Type": "application/json",
            # "Authorization": config('BEARER_TOKEN')
        }
        for city in self.destination_data:
            print(city['iataCode'])
            new_data = {
                "price": {
                    "iataCode": city['iataCode']
                }
            }
            response = requests.put(url=f"{end_point_url}/{city['id']}", json=new_data, headers=headers)
            print(response.text)

