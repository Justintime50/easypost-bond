import withbond
import uuid

# this is a temporary work around
# the brandPackageId of a withbond request
# must be unique every call, so this is
# a workaroud so we don't have to manually 
# change the id each time we run tests
brandPackageId = uuid.uuid1()

withbond_shipment = withbond.Shipment.create(
	data="{\n    \"type\": \"DELIVER\",\n    \"requestedDeliveryDate\": \"2020-07-11T00:00:00.000Z\",\n    \"customer\": {\n        \"brandContactId\": \"256\",\n        \"name\": \"John Smith\",\n        \"email\": \"mr.smith@example.com\",\n        \"phone\": \"+1-917-685-3957\",\n        \"zipcode\": \"10003-1502\",\n        \"address\": \"228 Park Ave S\",\n        \"city\": \"New York\",\n        \"state\": \"NY\",\n        \"country\": \"USA\",\n        \"notes\": \"Leave in front of the door\"\n    },\n    \"receiver\": {\n        \"brandContactId\": \"256\",\n        \"name\": \"John Smith\",\n        \"email\": \"mr.smith@example.com\",\n        \"phone\": \"+1-917-685-3957\",\n        \"zipcode\": \"10003-1502\",\n        \"address\": \"228 Park Ave S\",\n        \"city\": \"New York\",\n        \"state\": \"NY\",\n        \"country\": \"USA\",\n        \"notes\": \"Leave in front of the door\"\n    },\n    \"notes\": \"Make sure it's fresh\",\n    \"packages\": [\n        {\n            \"brandPackageId\": \"" + str(brandPackageId) + "\",\n            \"items\": [\n                {\n                    \"sku\": \"12\",\n                    \"quantity\": 2\n                }\n            ],\n            \"dimensions\": {\n                \"unit\": \"IMPERIAL\",\n                \"height\": 1,\n                \"width\": 6,\n                \"length\": 9,\n                \"weight\": 2.25\n            },\n            \"specialCondition\": \"Extremly heavy, handle with care\"\n        }\n    ]\n}"
)

print(withbond_shipment)