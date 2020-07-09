#!/bin/bash

source ../../.env

curl --location --request GET https://public-api.int01.withbond.io/api/v1/orders/brand-order/194f64f2-c188-11ea-bd2b-acde48001122 \
    --header "X-BOND-KEY: $WITHBOND_API_KEY" \
    --header "Content-Type: application/json"
