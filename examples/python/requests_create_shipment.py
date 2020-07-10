import requests
import json

data = """{
    "type": "DELIVER",
    "receiver": {
        "name": "John Smith",
        "email": "mr.smith@example.com",
        "phone": "+1-917-685-3957",
        "zipcode": "10003-1502",
        "address": "228 Park Ave S",
        "city": "New York",
        "state": "NY",
        "country": "USA"
    },
    "packages": [
        {
            "items": [
                {
                    "sku": "13",
                    "quantity": 2
                }
            ],
            "dimensions": {
                "unit": "IMPERIAL",
                "height": 1,
                "width": 6,
                "length": 9,
                "weight": 2.25
            },
            "specialCondition": "Extremly heavy, handle with care"
        }
    ]
}"""

# Create Shipment
response = requests.request(
    'POST', 'http://localhost:5000/shipments', data=data)
print(response.text)

# # Buy Shipment
# response = requests.request(
#     'POST', 'http://localhost:5000/shipments/shp_d6ix6whetqsvj8uq3utjw0s3auwhdk69/buy')
# print(response.text)

# # Retrieve Shipment
# response = requests.request(
#     'GET', 'http://localhost:5000/shipments/shp_d6ix6whetqsvj8uq3utjw0s3auwhdk69')
# print(response.text)

# # Retrieve Tracker
# response = requests.request(
#     'GET', 'http://localhost:5000/trackers/shp_d6ix6whetqsvj8uq3utjw0s3auwhdk69')
# print(response.text)
