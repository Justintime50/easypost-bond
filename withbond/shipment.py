import os
import random
import string

from withbond.client import Client
from withbond.translate import (ep_to_wb_request_shipment,
                                wb_to_ep_response_shipment)


class Shipment():
    @staticmethod
    def retrieve(data):
        """Retrieve a shipment by ID
        """
        response = Client.request(
            'GET',
            f'{Client.API_BASE_URL}/orders/brand-order/{data}'
        )
        json_data = wb_to_ep_response_shipment(response.json())

        return json_data

    @staticmethod
    def create(data):
        """Create a shipment based on the data passed
        """
        json_data = ep_to_wb_request_shipment(data.json)

        # First we create the shipment
        create_shipment = Client.request(
            'POST',
            f'{Client.API_BASE_URL}/orders',
            json_data
        )
        bond_shipment_data = create_shipment.json()
        print('lala3', bond_shipment_data)

        # For mocking purposes only, when complete, EasyPost would generate this
        ep_shipment_id = 'shp_' + \
            ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(32))

        # Next we update the shipment to associate it with the EasyPost shipment_id
        data = {
            'brandOrderId': ep_shipment_id,
            'displayId': ep_shipment_id
        }
        update_shipment = Shipment._update(data, bond_shipment_data['id'], 'bond-order')

        json_data = wb_to_ep_response_shipment(update_shipment.json())

        return json_data

    @staticmethod
    def buy(data):
        """Buy a shipment based on the data passed
        """
        # First we retrieve the shipment to get the bondId which is required to generate the label
        retrieved_shipment = Shipment.retrieve(data)

        # Next we actually buy the shipment based on the retrieved data in the previous call
        # TODO: Use the bondID we store in the tracking/rate field - mocked
        data = {
            'bondIds': retrieved_shipment["tracking_code"]
        }
        response = Client.request(
            'POST',
            f'{Client.API_BASE_URL}/labels',
            data
        )

        # TODO: Move to storing this in a DB instead of to disk
        # We only did it this way for the hackathon
        label_name = retrieved_shipment['id'] + '.pdf'
        if not os.path.exists('labels'):
            os.makedirs('labels')
        with open(os.path.join('labels', label_name), 'wb') as label:
            label.write(response.content)
        return f'Label bought and saved to disk at labels/{label_name}!'

    @staticmethod
    def refund(shipment_id):
        """Refund/void/cancel a shipment
        """
        # First we retrieve the shipment by the brandOrderId
        shipment = Shipment.retrieve(shipment_id)

        # Next we refund the shipment with the bondOrderId
        data = {
            'status': 'CANCELLED',
            'displayId': shipment['id']
        }
        refund = Shipment._update(data, shipment['id'], 'brand-order')
        return refund.json()

    @staticmethod
    def _update(data, bond_id, prefix):
        """Update a shipment
        """
        response = Client.request(
            'PATCH',
            f'{Client.API_BASE_URL}/orders/{prefix}/{bond_id}',
            data
        )
        return response
