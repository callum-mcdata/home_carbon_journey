import requests
import json
import csv

## Variables
api_token = 'dsPymbbReNyruXQIb0kZ1C2dqZVgDpVy'
my_lat = '42.067169'
my_lon = '-87.712841'
start_date = '202201020000'
end_date = '202201030000'

## The string for energy costs from ComeEd
energy_cost_url = f'https://hourlypricing.comed.com/api?type=5minutefeed&datestart={start_date}&dateend={end_date}'

# This is making the call to get back the zones
response = requests.get(
        url = energy_cost_url,
        verify = False)

values = response.json()

# Write data from each batch to json file
with open(f"output_data/comed_pricing/data_file__{start_date}_{end_date}.json", "w") as write_file:
    json.dump(values, write_file,indent = 4, sort_keys=True)