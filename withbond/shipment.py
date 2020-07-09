"""All Shipment methods are housed here"""
from withbond.client import Client


class Shipment():
    """Shipment methods"""
    @classmethod
    def retrieve(cls, data):
        """Retrieve a shipment by ID"""
        endpoint = f'{Client.API_BASE_URL}/orders/brand-order/{data}'
        response = Client.request("GET", endpoint, data)
        return response.json()

    @classmethod
    def create(cls, data):
        """Create a shipment based on the data passed"""
        endpoint = f'{Client.API_BASE_URL}/orders'
        response = Client.request("POST", endpoint, data)
        return response.json()

    @classmethod
    def buy(cls, data):
        """Buy a shipment based on the data passed"""
        endpoint =f'{Client.API_BASE_URL}/labels'
        response = Client.request("POST", endpoint, data)
        return response.json()
