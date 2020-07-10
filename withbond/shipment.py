"""All Shipment methods are housed here"""
import random
import string
import json
import os
import withbond.translate as convertJson
from .client import Client


class Shipment():
    """Shipment methods"""
    @classmethod
    def retrieve(cls, data):
        """Retrieve a shipment by ID"""
        endpoint = f'{Client.API_BASE_URL}/orders/brand-order/{data}'
        response = Client.request('GET', endpoint)

        bond_shipment_data = response.json()
        json_data = convertJson.wb_to_ep_response(bond_shipment_data)

        return json_data

    @classmethod
    def create(cls, data):
        """Create a shipment based on the data passed"""
        json_data = convertJson.ep_to_wb_request(data)

        # First we create the shipment
        create_endpoint = f'{Client.API_BASE_URL}/orders'
        create_shipment = Client.request('POST', create_endpoint, json_data)
        bond_shipment_data = create_shipment.json()

        # For mocking purposes only, when complete, EasyPost would generate this
        ep_shipment_id = 'shp_' + \
            "".join(random.choice(string.ascii_lowercase + string.digits)
                    for _ in range(32))

        # Next we update the shipment to associate it with the EasyPost shipment_id
        data = f'{{"brandOrderId": "{ep_shipment_id}" }}'
        update_shipment = Shipment.update(data, bond_shipment_data['id'])

        json_data = convertJson.wb_to_ep_response(update_shipment)

        return json_data  # don't return `.json()` here as this is already done by update above

    # TODO: This should not be an externally available method,
    # TODO: cont... - only used internally to update the shipment_id
    @ classmethod
    def update(cls, data, bond_id=None):
        """Update a shipment"""
        endpoint = f'{Client.API_BASE_URL}/orders/bond-order/{bond_id}'
        response = Client.request('PATCH', endpoint, data)
        return response.json()

    @ classmethod
    def buy(cls, data):
        """Buy a shipment based on the data passed"""
        # First we retrieve the shipment to get the bondId which is required to generate the label
        retrieved_shipment = Shipment.retrieve(data)
        json_data = json.loads(retrieved_shipment)
        print(json_data['id'])

        # Next we actually buy the shipment based on the retrieved data in the previous call
        endpoint = f'{Client.API_BASE_URL}/labels'
        # TODO: Use the bondID we store in the tracking/rate field - mocked
        data = f'{{"bondIds": "{json_data["tracking_code"]}"}}'
        response = Client.request('POST', endpoint, data)

        # TODO: Move to storing this in a DB instead of to disk
        if not os.path.exists('labels'):
            os.makedirs('labels')
        with open(os.path.join('labels', json_data["id"]
                               + '.pdf'), 'wb') as label:
            label.write(response.content)
        return "Label bought and saved to disk!"

    @ classmethod
    def refund(cls, shipment_id):
        """Refund/void/cancel a shipment"""
        # First we retrieve the shipment by the brandOrderId
        shipment = Shipment.retrieve(shipment_id)

        # Next we refund the shipment with the bondOrderId
        data = '{"status": "CANCELLED"}'
        refund = Shipment.update(data, shipment['id'])
        return refund
