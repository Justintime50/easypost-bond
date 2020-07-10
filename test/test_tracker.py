import unittest
import os
import json
import vcr
import requests
import withbond


class TestTracker(unittest.TestCase):

    @vcr.use_cassette()
    def test_tracker_retrieve(self):
        """Test retrieving a tracker and receiving an EasyPost response"""
        response = requests.request(
            'GET', 'http://localhost:5000/trackers/shp_d6ix6whetqsvj8uq3utjw0s3auwhdk69')

        assert response.status_code == 200
