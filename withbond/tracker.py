"""Import modules"""
import withbond.tracker_translate as convertJson
from .shipment import Shipment


class Tracker():
    """All tracking methods"""
    @classmethod
    def retrieve(cls, data):
        """Retrieve a shipment and return its tracking status"""
        shipment = Shipment.retrieve(data)
        # tracking_status = shipment['status']
        # mapped_status = Tracker.map_statuses(tracking_status)
        json_data = convertJson.ep_response(shipment)

        return json_data

    # TODO: Change this from a classmethod as it should not be accessible outside itself
    # TODO: This is deprecated and may be removed? Or we can move this to the translate files
    @ classmethod
    def map_statuses(cls, tracking_status):
        """Map the Withbond statuses to the EasyPost equivalent"""
        map_values = {
            'PENDING': 'pre_transit',
            'READY_FOR_DELIVERY': 'in_transit',
            'ON_THE_WAY': 'out_for_delivery',
            'SERVICING': 'delivered',
            'DONE': 'delivered',
            # TODO: Should this instead map to "refunded"?
            'CANCELLED': 'cancelled',
        }

        return map_values.get(tracking_status, 'Invalid tracking status')
