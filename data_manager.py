from decouple import config
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    # def get_city_names(self):
    #     # Get from spreadsheet
    #     end_point_url = "https://api.sheety.co/33093744d338c796ac3b15096c2a0e35/flightDeals/prices"
    #
    #     headers = {
    #         "Content-Type": "application/json",
    #         "Authorization": config('BEARER_TOKEN')
    #     }
    #     response = requests.get(url=end_point_url, headers=headers)
    #     data = response.json()
    #
    #     lst = data.get('prices')
    #     cities = []
    #     for i in range(len(lst)):
    #         for key in lst[i]:
    #             if key == 'city':
    #                 cities.append(lst[i]["city"])
    #     return cities

    headers = {
                "Content-Type": "application/json",
                "Authorization": config('BEARER_TOKEN')
            }
    #post url
    end_point_post_url = "https://api.sheety.co/33093744d338c796ac3b15096c2a0e35/flightDeals/prices"

    airport_code = {
        "price": {
            "IATA Code": "BER"
        }
    }
    response = requests.post(url=end_point_post_url, json=airport_code, headers=headers)
    print(response.text)