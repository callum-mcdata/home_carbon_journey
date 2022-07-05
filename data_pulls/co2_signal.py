import requests
import json
import csv

## Variables
api_token = 'dsPymbbReNyruXQIb0kZ1C2dqZVgDpVy'
my_lat = '42.067169'
my_lon = '-87.712841'
zone_code= 'US-MIDA-PJM'

## The string for energy costs from ComeEd
carbon_emission_url = f'https://api.co2signal.com/v1/latest?lon={my_lon}&lat={my_lat}'

# This is making the call to get back the zones
response = requests.get(
        url = carbon_emission_url,
        headers={'auth-token': 'dsPymbbReNyruXQIb0kZ1C2dqZVgDpVy'},
        verify = False)

values = response.json()

# Write data from each batch to json file
with open(f"output_data/co2_data/data_file.json", "w") as write_file:
    json.dump(values, write_file,indent = 4, sort_keys=True)