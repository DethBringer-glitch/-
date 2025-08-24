import requests
import json
import os



if os.path.exists('cats.json'):
    os.remove('cats.json')


for i in range(10):
    url = 'https://catfact.ninja/fact'
    response = requests.get(url)
    print(response.text)
    data = response.json()
    with open('cats.json', 'a') as file:
        json.dump(data, file, indent=4)