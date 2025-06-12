import requests
from api_key import api_key
import json
print(api_key)
#r = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/London,UK/?key={api_key}")
#print(r.json())

with open('sample.json', 'r') as openfile:

    json_object = json.load(openfile)

for key,value in json_object["days"][0].items():
    print(key)
    print(value)
    print()


