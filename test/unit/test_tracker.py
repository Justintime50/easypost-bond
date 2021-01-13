"""Import modules"""
import unittest
import json
import vcr
import requests


class TestTracker(unittest.TestCase):
    """Test Tracking functionality"""
    @vcr.use_cassette('test/fixtures/cassettes/test_tracker_retrieve.yml')
    @classmethod
    def test_tracker_retrieve(cls):
        """Test retrieving a tracker and receiving an EasyPost response"""
        response = requests.request(
            'GET', 'http://localhost:5000/trackers/shp_d6ix6whetqsvj8uq3utjw0s3auwhdk69')

        assert response.status_code == 200
        assert json.loads(response.text) == {
            "id": "trk_...",
            "object": "Tracker",
            "mode": "test",
            "tracking_code": "shp_d6ix6whetqsvj8uq3utjw0s3auwhdk69",
            "status": "cancelled",
            "created_at": "2020-07-10T01:42:13.203Z",
            "updated_at": "2020-07-10T01:42:13.203Z",
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
                    "status": "cancelled",
                    "datetime": "2020-07-10T01:42:13.203Z",
                    "source": "WithBond",
                    "tracking_location": {
                        "object": "TrackingLocation",
                        "city": "New York",
                        "state": "New York",
                        "country": "US",
                        "zip": "10003"
                    }
                }
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
