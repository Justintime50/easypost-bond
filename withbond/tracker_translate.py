import json
from .static_data import FLAT_RATE, SERVICE_LEVEL


def ep_response(jsonData):

    data = json.loads(jsonData)

    ep_response = {
        "id": "trk_...",
        "object": "Tracker",
        "mode": "test",
        "tracking_code": data["id"],
        "status": data["status"],
        "created_at": data["created_at"],
        "updated_at": data["created_at"],
        "signed_by": "null",
        "weight": "null",
        "est_delivery_date": "null",
        "shipment_id": "null",
        "carrier": "WithBond",
        "public_url": "https://track.easypost.com/djE6...",
        "tracking_details": [
            {
                "object": "TrackingDetail",
                "message": "Shipping Label Created",
                "status": data["status"],
                "datetime": data["created_at"],
                "source": "WithBond",
                "tracking_location": {
                    "object": "TrackingLocation",
                    "city": "New York",
                    "state": "New York",
                    "country": "US",
                    "zip": "10003"
                }
            },
        ],
        "carrier_detail": "null",
        "fees": [
            {
                "object": "Fee",
                "type": "TrackerFee",
                "amount": "0.00000",
                "charged": True,
                "refunded": False
            }
        ]
    }

    return json.dumps(ep_response)
