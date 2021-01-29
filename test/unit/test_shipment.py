import json

import requests
import vcr

HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic abc123'
}


@vcr.use_cassette('test/fixtures/cassettes/test_shipment_create.yml')
def test_shipment_create(mock_shipment):
    """Test creating a shipment and receiving an EasyPost response
    """
    response = requests.post(
        'http://localhost:5000/shipments',
        json=mock_shipment,
        headers=HEADERS
    )

    assert response.status_code == 200


@vcr.use_cassette('test/fixtures/cassettes/test_shipment_retrieve.yml')
def test_shipment_retrieve():
    """Test retrieving a shipment and receiving an EasyPost response
    """
    response = requests.get(
        'http://localhost:5000/shipments/shp_5l76p1fp2fovc8vwntmg76mniiygdkl1'
    )

    assert response.status_code == 200


@vcr.use_cassette('test/fixtures/cassettes/test_shipment_buy.yml')
def test_shipment_buy():
    """Test buying a shipment and receiving a label
    """
    response = requests.post(
        'http://localhost:5000/shipments/shp_5l76p1fp2fovc8vwntmg76mniiygdkl1/buy'
    )

    assert response.status_code == 200


@vcr.use_cassette('test/fixtures/cassettes/test_shipment_refund.yml')
def test_shipment_refund():
    """Test refunding a shipment and receiving an EasyPost response
    """
    response = requests.post(
        'http://localhost:5000/shipments/shp_d9nkhebsxwlba32u4zopnoyxn3xgstvt/refund'
    )
    json_data = json.loads(response.text)

    assert response.status_code == 200
    assert json_data['status'] == 'CANCELLED'
