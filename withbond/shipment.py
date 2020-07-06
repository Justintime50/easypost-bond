"""All Shipment methods are housed here"""
from withbond.client import Client


class Shipment():
    """Shipment methods"""
    @classmethod
    def create(cls, data):
        """Create a customer based on the data passed"""
        endpoint = f'{Client.API_BASE_URL}orders'
        response = Client.response(data, endpoint)
        return response.json()
