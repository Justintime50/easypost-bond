"""All Shipment methods are housed here"""
import random
import string
from withbond.client import Client


class Shipment():
    """Shipment methods"""
    @classmethod
    def retrieve(cls, data):
        """Retrieve a shipment by ID"""
        endpoint = f'{Client.API_BASE_URL}/orders/brand-order/{data}'
        response = Client.request('GET', endpoint)
        return response.json()

    @classmethod
    def create(cls, data):
        """Create a shipment based on the data passed"""
        # First we create the shipment
        create_endpoint = f'{Client.API_BASE_URL}/orders'
        create_shipment = Client.request('POST', create_endpoint, data)
        bond_shipment_data = create_shipment.json()

        # For mocking purposes only, when complete, EasyPost would generate this
        ep_shipment_id = f'shp_{"".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(32))}'

        # Next we update the shipment to associate it with the EasyPost shipment_id
        data = f'{{"brandOrderId": "{ep_shipment_id}" }}'
        update_shipment = Shipment.update(data, bond_shipment_data['id'])
        return update_shipment

    # TODO: This should not be an externally available method, only used internally to update the shipment_id
    @classmethod
    def update(cls, data, bond_id=None):
        """Update a shipment"""
        endpoint = f'{Client.API_BASE_URL}/orders/bond-order/{bond_id}'
        response = Client.request('PATCH', endpoint, data)
        return response.json()

    @classmethod
    def buy(cls, data):
        """Buy a shipment based on the data passed"""
        # First we retrieve the shipment to get the bondId which is required to generate the label
        retrieved_shipment = Shipment.retrieve(data)

        # Next we actually buy the shipment based on the retrieved data in the previous call
        endpoint = f'{Client.API_BASE_URL}/labels'
        data = f'{{"bondIds": "{retrieved_shipment["id"]}" }}'
        response = Client.request('POST', endpoint, data)

        # TODO: Move to storing this in a DB instead of to disk
        with open(f'{retrieved_shipment["brandOrderId"]}.pdf', 'wb') as label:
            label.write(response.content)
        return "Label bought and saved to disk!"
