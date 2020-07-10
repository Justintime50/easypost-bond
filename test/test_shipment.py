import unittest
import os
import json
import vcr
import requests
import withbond


class TestShipment(unittest.TestCase):

    @vcr.use_cassette()
    def test_shipment_create(self):
        """Test creating a shipment and receiving an EasyPost response"""
        data = """
            {
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

        response = requests.request(
            'POST', 'http://localhost:5000/shipments', data=data)

        assert response.status_code == 200
        assert json.loads(response.text) == {
            "created_at": "2020-07-10T15:40:45.365Z",
            "is_return": "false",
            "messages": [],
            "mode": "test",
            "options": {
                "currency": "USD",
                "payment": {
                    "type": "SENDER"
                },
                "date_advance": 0
            },
            "reference": "null",
            "status": "pre_transit",
            "tracking_code": "BObeJ2R8uV",
            "updated_at": "2020-07-10T15:40:45.365Z",
            "batch_id": "null",
            "batch_status": "null",
            "batch_message": "null",
            "customs_info": "null",
            "from_address": {
                "id": "null",
                "object": "Address",
                "created_at": "null",
                "updated_at": "null",
                "name": "null",
                "company": "null",
                "street1": "null",
                "street2": "",
                "city": "null",
                "state": "null",
                "zip": "null",
                "country": "null",
                "phone": "null",
                "email": "null",
                "mode": "null",
                "carrier_facility": "null",
                "residential": "null",
                "federal_tax_id": "null",
                "state_tax_id": "null",
                "verifications": {}
            },
            "insurance": "null",
            "order_id": "null",
            "parcel": {
                "id": "null",
                "object": "Parcel",
                "created_at": "2020-07-10T15:40:45.365Z",
                "updated_at": "2020-07-10T15:40:45.365Z",
                "length": 2,
                "width": 2,
                "height": 2,
                "predefined_package": "null",
                "weight": 20,
                "mode": "test"
            },
            "postage_label": {
                "object": "PostageLabel",
                "id": "null",
                "created_at": "2020-07-10T15:40:45.365Z",
                "updated_at": "2020-07-10T15:40:45.365Z",
                "date_advance": 0,
                "integrated_form": "none",
                "label_date": "2020-07-10T15:40:45.365Z",
                "label_resolution": 300,
                "label_size": "4x6",
                "label_type": "default",
                "label_file_type": "image/pdf",
                "label_url": "null",
                "label_pdf_url": "null",
                "label_zpl_url": "null",
                "label_epl2_url": "null",
                "label_file": "null"
            },
            "rates": [
                {
                    "id": "null",
                    "object": "Rate",
                    "created_at": "2020-07-10T15:40:45.365Z",
                    "updated_at": "2020-07-10T15:40:45.365Z",
                    "mode": "test",
                    "service": "Standard",
                    "carrier": "WithBond",
                    "rate": 10,
                    "currency": "USD",
                    "retail_rate": 10,
                    "retail_currency": "USD",
                    "list_rate": 10,
                    "list_currency": "USD",
                    "delivery_days": "null",
                    "delivery_date": "null",
                    "delivery_date_guaranteed": "false",
                    "est_delivery_days": "null",
                    "shipment_id": "shp_k35ifn9gsq507i0nm3tdrv69cy7hagch",
                    "carrier_account_id": "null"
                }
            ],
            "refund_status": "null",
            "scan_form": "null",
            "selected_rate": {
                "id": "null",
                "object": "Rate",
                "created_at": "2020-07-10T15:40:45.365Z",
                "updated_at": "2020-07-10T15:40:45.365Z",
                "mode": "test",
                "service": "Standard",
                "carrier": "WithBond",
                "rate": 10,
                "currency": "USD",
                "retail_rate": 10,
                "retail_currency": "USD",
                "list_rate": 10,
                "list_currency": "USD",
                "delivery_days": "null",
                "delivery_date": "null",
                "delivery_date_guaranteed": "false",
                "est_delivery_days": "null",
                "shipment_id": "shp_k35ifn9gsq507i0nm3tdrv69cy7hagch",
                "carrier_account_id": "null"
            },
            "tracker": {
                "id": "null",
                "object": "Tracker",
                "mode": "test",
                "tracking_code": "BObeJ2R8uV",
                "status": "pre_transit",
                "status_detail": "pre_transit",
                "created_at": "2020-07-10T15:40:45.365Z",
                "updated_at": "2020-07-10T15:40:45.365Z",
                "signed_by": "null",
                "weight": "null",
                "est_delivery_date": "null",
                "shipment_id": "shp_k35ifn9gsq507i0nm3tdrv69cy7hagch",
                "carrier": "WithBond",
                "tracking_details": [],
                "fees": [],
                "carrier_detail": "null",
                "public_url": "null"
            },
            "to_address": {
                "id": "null",
                "object": "Address",
                "created_at": "2020-07-10T15:40:45.365Z",
                "updated_at": "2020-07-10T15:40:45.365Z",
                "name": "John Smith",
                "company": "",
                "street1": "228 Park Ave S",
                "street2": "",
                "city": "New York",
                "state": "NY",
                "zip": "10003",
                "country": "US",
                "phone": "John Smith",
                "email": "example@example.com",
                "mode": "test",
                "carrier_facility": "null",
                "residential": "null",
                "federal_tax_id": "null",
                "state_tax_id": "null",
                "verifications": {}
            },
            "usps_zone": 1,
            "return_address": {
                "id": "null",
                "object": "Address",
                "created_at": "null",
                "updated_at": "null",
                "name": "null",
                "company": "null",
                "street1": "null",
                "street2": "",
                "city": "null",
                "state": "null",
                "zip": "null",
                "country": "null",
                "phone": "null",
                "email": "null",
                "mode": "null",
                "carrier_facility": "null",
                "residential": "null",
                "federal_tax_id": "null",
                "state_tax_id": "null",
                "verifications": {}
            },
            "buyer_address": {
                "id": "null",
                "object": "Address",
                "created_at": "2020-07-10T15:40:45.365Z",
                "updated_at": "2020-07-10T15:40:45.365Z",
                "name": "John Smith",
                "company": "",
                "street1": "228 Park Ave S",
                "street2": "",
                "city": "New York",
                "state": "NY",
                "zip": "10003",
                "country": "US",
                "phone": "John Smith",
                "email": "example@example.com",
                "mode": "test",
                "carrier_facility": "null",
                "residential": "null",
                "federal_tax_id": "null",
                "state_tax_id": "null",
                "verifications": {}
            },
            "forms": [],
            "fees": [
                {
                    "object": "Fee",
                    "type": "LabelFee",
                    "amount": "0.01000",
                    "charged": "true",
                    "refunded": "false"
                }
            ],
            "id": "shp_k35ifn9gsq507i0nm3tdrv69cy7hagch",
            "object": "Shipment"
        }

    @vcr.use_cassette()
    def test_shipment_retrieve(self):
        """Test retrieving a shipment and receiving an EasyPost response"""
        response = requests.request(
            'GET', 'http://localhost:5000/shipments/shp_k35ifn9gsq507i0nm3tdrv69cy7hagch')

        assert response.status_code == 200

    @vcr.use_cassette()
    def test_shipment_buy(self):
        """Test buying a shipment and receiving a label"""
        response = requests.request(
            'GET', 'http://localhost:5000/trackers/shp_d6ix6whetqsvj8uq3utjw0s3auwhdk69')

        assert response.status_code == 200
        # assert os.path.isfile(
        #     'labels/shp_d6ix6whetqsvj8uq3utjw0s3auwhdk69.pdf')

    @vcr.use_cassette()
    def test_shipment_refund(self):
        """Test retrieving a shipment and receiving an EasyPost response"""
        response = requests.request(
            'POST', 'http://localhost:5000/shipments/shp_d6ix6whetqsvj8uq3utjw0s3auwhdk69/refund')

        assert response.status_code == 200
