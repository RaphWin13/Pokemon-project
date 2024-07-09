import csv
import json

with open("data/pokemon_data_copy.csv", newline='') as csvFile:
    reader = csv.DictReader(csvFile)
    data = [row for row in reader]

with open('data/pokemon.json', 'w') as jsonfile:
    json.dump(data, jsonfile)   