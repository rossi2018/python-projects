import requests
from pprint import pprint

API_Key = '8897492a2648218d330226a2b56aab2f'

city = input('Enter a city: ')

base_url = 'http://api.openweatherapp.org/data/2.5/weather?appid='+API_Key+'&Q='+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
