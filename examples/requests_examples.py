import json  # noqa
import os

import requests

API_KEY = os.getenv('API_KEY')


headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic abc123'
}

ep_data = {
    "shipment": {
        "carrier_account": {"id": "ca_..."},
        "from_address": {
            "name": "Sara Rivera",
            "street1": "16 Mulford Avenue",
            "street2": "",
            "city": "East Hanover",
            "state": "NJ",
            "zip": "07936",
            "country": "US",
            "phone": "9738867458"
        },
        "to_address": {
            "name": "John Smith",
            "company": "",
            "street1": "228 Park Ave S",
            "street2": "",
            "city": "New York",
            "state": "NY",
            "zip": "10003",
            "country": "US",
            "phone": "7531592522",
            "email": "example@example.com"
        },
        "buyer_address": {
            "name": "John Smith",
            "company": "",
            "street1": "228 Park Ave S",
            "street2": "",
            "city": "New York",
            "state": "NY",
            "zip": "10003",
            "country": "US",
            "phone": "7531592522",
            "email": "example@example.com"
        },
        "parcel": {
            "length": 2.0,
            "width": 2.0,
            "height": 2.0,
            "weight": 20
        }
    }
}

# Create Shipment
response = requests.post(
    'http://localhost:5000/shipments',
    json=json.dumps(ep_data),
    headers=headers
)
print(response.text)

# # Buy Shipment
# response = requests.post(
#     'http://localhost:5000/shipments/shp_r8i7am95qm8jvnv0mwfj5u7vb8j0qwf2/buy'
# )
# print(response.text)

# # Retrieve Shipment
# response = requests.get(
#     'http://localhost:5000/shipments/shp_r8i7am95qm8jvnv0mwfj5u7vb8j0qwf2'
# )
# print(response.text)

# # Refund Shipment
# response = requests.post(
#     'http://localhost:5000/shipments/shp_r8i7am95qm8jvnv0mwfj5u7vb8j0qwf2/refund'
# )
# print(response.text)

# # Retrieve Tracker
# response = requests.get(
#     'http://localhost:5000/trackers/shp_r8i7am95qm8jvnv0mwfj5u7vb8j0qwf2'
# )
# print(response.text)
