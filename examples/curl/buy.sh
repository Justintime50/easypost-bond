#!/bin/bash

source ../../.env

curl --location --request POST https://public-api.int01.withbond.io/api/v1/labels \
    --header "X-BOND-KEY: $WITHBOND_API_KEY" \
    --header "Content-Type: application/json" \
    --data-raw '{
        "bondIds": "BOBqGdTTrX"
    }'
