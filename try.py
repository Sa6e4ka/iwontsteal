import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
ip = "185.24.76.184"

api_map = os.environ.get("STATIC_MAP_KEY")
api_loc= os.environ.get("LOCATOR")

'''
Функция для получения статической карты в формате .зng
'''
def get_map(cords):
    link = f"https://static-maps.yandex.ru/v1?lang=ang&z=5&pt={cords},vkbkm&apikey={api_map}"
    response = requests.get(link).content

    with open("map.png", "wb") as file:
        file.write(response)


'''
Функция для получения локации по ip
'''
def get_location(ip, api_loc):
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        "common": {
            "version": "1.0",
            "api_key": f"{api_loc}"
        },
        "gsm_cells": [
            {
                "countrycode": 250,
                "operatorid": 2,
                "cellid": 197403650,
                "lac": 9900,
                "signal_strength": -80,
                "age": 1000
            }
        ],
        "wifi_networks": [
            {
                "mac": "2CD02D814C80",
                "signal_strength": -68,
                "age": 500
            },
            {
                "mac": "E4AA5DE28CD0",
                "signal_strength": -60,
                "age": 500
            }
        ],
        "ip": {
            "address_v4": f"{ip}"
        }
    }


    data_str = json.dumps(data)
    
    response = requests.post('http://api.lbs.yandex.net/geolocation', headers=headers, data=f"json={data_str}").json()
    return f"{response["position"]["latitude"]},{response["position"]["longitude"]}"
    
get_map(cords=get_location(ip=ip, api_loc=api_loc))