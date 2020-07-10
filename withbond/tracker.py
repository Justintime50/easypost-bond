import json
from .shipment import Shipment

class Tracker():
    """All tracking methods"""
    @classmethod
    def retrieve(cls, data):
        """Retrieve a shipment and return its tracking status"""
        shipment = Shipment.retrieve(data)
        tracking_status = shipment['status']
        mapped_status = Tracker.map_statuses(tracking_status)

        json_status = json.dumps(mapped_status, indent=4)
        return json_status

    # TODO: Change this from a classmethod as it should not be accessible outside itself
    @classmethod
    def map_statuses(cls, tracking_status):
        """Map the Withbond statuses to the EasyPost equivalent"""
        map = {
            'PENDING': {"status": "pre_transit"},
            'READY_FOR_DELIVERY': '"{status": "in_transit"}',
            'ON_THE_WAY': 'out_for_delivery',
            'SERVICING': 'delivered',
            'DONE': 'delivered',
            'CANCELLED': 'cancelled',
        }
        
        return map.get(tracking_status, 'Invalid tracking status')
