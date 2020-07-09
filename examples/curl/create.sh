#!/bin/bash

source ../../.env

curl --location --request POST https://public-api.int01.withbond.io/api/v1/orders \
    --header "X-BOND-KEY: $WITHBOND_API_KEY" \
    --header "Content-Type: application/json" \
    --data-raw '{
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
    }'
