import json

import pytest


@pytest.fixture
def mock_shipment():
    return json.dumps({
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
    })
