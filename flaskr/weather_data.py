import requests
from api_key import api_key
import json


def weather_data():

    r = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/London,UK/?key={api_key}")

    json_object = r.json()
    weather = {

    }

    for days in json_object["days"]:
        weather[days["datetime"]] = [days["temp"],days["conditions"]]
    return weather

#    for key, value in days.items():
#        print(key)
#        print(value)

