import requests
import json

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic 123abc'
}

ep_data = """{
    "shipment":{
        "carrier_account":{"id":"ca_..."},
        "from_address":{
            "name":"Sara Rivera",
            "street1":"16 Mulford Avenue",
            "street2":"",
            "city":"East Hanover",
            "state":"NJ",
            "zip":"07936",
            "country":"US",
            "phone":"9738867458"
        },
        "to_address":{
            "name":"John Smith",
            "company":"",
            "street1":"228 Park Ave S",
            "street2":"",
            "city":"New York",
            "state":"NY",
            "zip":"10003",
            "country":"US",
            "phone":"7531592522",
            "email":"example@example.com"
        },
        "buyer_address":{
            "name":"John Smith",
            "company":"",
            "street1":"228 Park Ave S",
            "street2":"",
            "city":"New York",
            "state":"NY",
            "zip":"10003",
            "country":"US",
            "phone":"7531592522",
            "email":"example@example.com"
        },         
        "parcel":{
            "length":2.0,
            "width":2.0,
            "height":2.0,
            "weight":20
        }
    }
}"""

# Create Shipment
response = requests.request(
    'POST', 'http://localhost:5000/shipments', data=ep_data, headers=headers)
print(response.text)

# # Buy Shipment
# response = requests.request(
#     'POST', 'http://localhost:5000/shipments/shp_ydnr3z2gkkxsu8myjue8ckze7wyovjox/buy')
# print(response.text)

# # Retrieve Shipment
# response = requests.request(
#     'GET', 'http://localhost:5000/shipments/shp_ydnr3z2gkkxsu8myjue8ckze7wyovjox')
# print(response.text)

# # Refund Shipment
# response = requests.request(
#     'POST', 'http://localhost:5000/shipments/shp_ydnr3z2gkkxsu8myjue8ckze7wyovjox/refund')
# print(response.text)

# # Retrieve Tracker
# response = requests.request(
#     'GET', 'http://localhost:5000/trackers/shp_ydnr3z2gkkxsu8myjue8ckze7wyovjox')
# print(response.text)
