import json

import requests
import vcr


@vcr.use_cassette('test/fixtures/cassettes/test_tracker_retrieve.yml')
def test_tracker_retrieve():
    """Test retrieving a tracker and receiving an EasyPost response
    """
    response = requests.get(
        'http://localhost:5000/trackers/shp_5l76p1fp2fovc8vwntmg76mniiygdkl1'
    )
    json_data = json.loads(response.text)

    assert response.status_code == 200
    assert json_data['tracking_details'][0]['message'] == 'Shipping Label Created'
    assert json_data['tracking_details'][0]['status'] == 'pre_transit'
