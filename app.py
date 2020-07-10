"""Import API modules"""
import json
import os
from flask import Flask, request
from dotenv import load_dotenv
import withbond

load_dotenv()
API = Flask(__name__)
HOST = os.getenv('HOST', '127.0.0.1')
PORT = os.getenv('PORT', 5000)
DEBUG = os.getenv('DEBUG', True)


@API.route('/shipments', methods=['POST'])
def create_shipment():
    """Create a shipment"""
    response = withbond.Shipment.create(request.data)
    if bool(DEBUG) is True:
        print(response)
    return response


@API.route('/shipments/<shipment_id>', methods=['GET'])
def retrieve_shipment(shipment_id):
    """Retrieve a shipment"""
    response = withbond.Shipment.retrieve(shipment_id)
    if bool(DEBUG) is True:
        print(response)
    return response


@API.route('/shipments/<shipment_id>/buy', methods=['POST'])
def buy_shipment(shipment_id):
    """Buy a shipment"""
    response = withbond.Shipment.buy(shipment_id)
    if bool(DEBUG) is True:
        print(response)
    return response


@API.route('/trackers/<tracker_id>', methods=['GET'])
def retrieve_tracker(tracker_id):
    """Retrieve a tracker"""
    response = withbond.Tracker.retrieve(tracker_id)
    if bool(DEBUG) is True:
        print(response)
    return response


@API.route('/shipments/<shipment_id>/refund', methods=['POST'])
def refund_shipment(shipment_id):
    """Refund a shipment"""
    response = withbond.Shipment.refund(shipment_id)
    if bool(DEBUG) is True:
        print(response)
    return response


if __name__ == '__main__':
    API.run(host=HOST, port=PORT, debug=bool(DEBUG))
