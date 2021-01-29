import os

from dotenv import load_dotenv
from flask import Flask, request

from withbond.shipment import Shipment
from withbond.tracker import Tracker

load_dotenv()
API = Flask(__name__)
HOST = os.getenv('HOST', '127.0.0.1')
PORT = os.getenv('PORT', 5000)
DEBUG = os.getenv('DEBUG', True)


# Create a shipment
@API.route('/shipments', methods=['POST'])
def create_shipment():
    response = Shipment.create(request)
    if bool(DEBUG) is True:
        print(response)
    return response


# Retrieve a shipment
@API.route('/shipments/<shipment_id>', methods=['GET'])
def retrieve_shipment(shipment_id):
    response = Shipment.retrieve(shipment_id)
    if bool(DEBUG) is True:
        print(response)
    return response


# Buy a shipment
@API.route('/shipments/<shipment_id>/buy', methods=['POST'])
def buy_shipment(shipment_id):
    response = Shipment.buy(shipment_id)
    if bool(DEBUG) is True:
        print(response)
    return response


# Retrieve a tracker
@API.route('/trackers/<tracker_id>', methods=['GET'])
def retrieve_tracker(tracker_id):
    response = Tracker.retrieve(tracker_id)
    if bool(DEBUG) is True:
        print(response)
    return response


# Refund a shipment
@API.route('/shipments/<shipment_id>/refund', methods=['POST'])
def refund_shipment(shipment_id):
    response = Shipment.refund(shipment_id)
    if bool(DEBUG) is True:
        print(response)
    return response


if __name__ == '__main__':
    API.run(host=HOST, port=PORT, debug=bool(DEBUG))
