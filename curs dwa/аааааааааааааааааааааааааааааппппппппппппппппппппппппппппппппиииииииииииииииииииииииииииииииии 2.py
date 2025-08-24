import json

json_data = '{"name": "Макс", "age": 10, "city": "Mytishi"}'
python_object = json.loads(json_data)
print(python_object["name"])
with open('dg.json', 'w') as file:
    json.dump(json_data, file, indent=4)
with open('dg.json', 'r') as file:
    loaddata = json.load(file)

print(loaddata)