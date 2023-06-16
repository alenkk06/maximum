        
import requests
import json

url = 'https://swapi.dev/api/'

response = requests.get(url).json()

starships_api = response.get('starships')

def check_starships(url):
    max_atmosphering_speed = []
    for i in range(1,6):
        response = requests.get(f'{url}/{i}').json()
        max_atmosphering_speed.append({response.get('name'):response.get('max_atmosphering_speed')})
        print(max_atmosphering_speed)

check_starships(starships_api)
