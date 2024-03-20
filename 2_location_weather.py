#
# Uzdevums:
# Izmantojot piemēru no pirma uzdevuma, izveidojiet programmu kas atspoguļos laika apstakļus (temperaturu un nokrišņus) pa stundām 
# izmantojot sekojošu datu linku 
# https://api.open-meteo.com/v1/forecast?latitude=56.8&longitude=24.2&hourly=temperature_2m,precipitation&forecast_days=1

import urllib.request
import json

def get_city_information(city):
    link = f"https://api.open-meteo.com/v1/forecast?latitude=56.8&longitude=24.2&hourly=temperature_2m,precipitation&forecast_days=1"
    
    with urllib.request.urlopen(link) as response:
        data = response.read().decode('utf-8')

    return json.loads(data)

def display_city_information(city_info):
    if city_info:
        print("City Information:")
        for city_data in city_info['results']:
            print(f"Temperature: {city_data['temerature_2m']}")
            print(f"Precipitation: {city_data['precipitation']}")
            print("-----------------------")
    else:
        print("No city information available.")

city_name = input("Enter city name: ")
city_information = get_city_information(city_name)
display_city_information(city_information)
