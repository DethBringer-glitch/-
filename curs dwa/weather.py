import json

with open('Weather.json') as file:
    data = json.load(file)

for city in data[:10]:
    print(f"{city['name']}:\nТип погоды: {city['weather'][0]['description']}")
    print(f"Температура: {city['main']['temp']}")