import json
from .static_data import FLAT_RATE, SERVICE_LEVEL


def wb_to_ep_request(jsonData):

    tmp = json.dumps(jsonData)
    wb_data = json.loads(tmp)

    status = ""

    if(wb_data["status"] == "PENDING"):
        status = "pre_transit"

    if(wb_data["status"] == "READY_FOR_DELIVERY"):
        status = "in_transit"

    if(wb_data["status"] == "ON_THE_WAY"):
        status = "out_for_delivery"

    if(wb_data["status"] == "SERVICING"):
        status = "delivered"

    if(wb_data["status"] == "DONE"):
        status = "delivered"

    if(wb_data["status"] == "CANCELLED"):
        status = "cancelled"

    ep_response = {
        "id": "trk_...",
        "object": "Tracker",
        "mode": "test",
        "tracking_code": wb_data["id"],
        "status": status,
        "created_at": wb_data["creationDate"],
        "updated_at": wb_data["creationDate"],
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
                "status": status,
                "datetime": wb_data["creationDate"],
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
