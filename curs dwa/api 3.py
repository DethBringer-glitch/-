import json, requests, os

if os.path.exists('Weather.json'): os.remove('Weather.json')

api = '49db58d1f28a68f7f84dea6c7c6ab942'
cities = ['Омск', 'Великий Новгород', 'Мытищи', 'Новосибирск', 'Екатеринбург', 'Санкт-Петербург', 'Красноярск', 'Волгоград', 'Саратов', 'Мурманск']
data = [requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={c}&lang=ru&units=metric&appid={api}').json() for c in cities]

with open('Weather.json', 'w') as f: json.dump(data, f, indent=4)
print(data[-1])