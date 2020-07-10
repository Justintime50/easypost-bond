"""Import API modules"""
import json
import os
from flask import Flask, request, abort
import withbond

API = Flask(__name__)


@API.route('/shipments', methods=['POST'])
def create_shipment():
    """Create a shipment"""
    response = json.dumps(withbond.Shipment.create(request.data))
    print(response)  # TODO: For debugging only, remove when done

    return response


@API.route('/shipments/<shipment_id>', methods=['GET'])
def retrieve_shipment(shipment_id):
    """Retrieve a shipment"""
    response = withbond.Shipment.retrieve(shipment_id)
    print(response)  # TODO: For debugging only, remove when done

    return response


@API.route('/shipments/<shipment_id>/buy', methods=['POST'])
def buy_shipment(shipment_id):
    """Buy a shipment"""
    response = withbond.Shipment.buy(shipment_id)
    print(response)  # TODO: For debugging only, remove when done

    return response


@API.route('/trackers/<tracker_id>', methods=['GET'])
def retrieve_tracker(tracker_id):
    """Retrieve a tracker"""
    response = withbond.Tracker.retrieve(tracker_id)
    print(response)  # TODO: For debugging only, remove when done

    return response


@API.route('/shipments/<shipment_id>/refund', methods=['POST'])
def refund_shipment(shipment_id):
    """Refund a shipment"""
    response = withbond.Shipment.refund(shipment_id)
    print(response)  # TODO: For debugging only, remove when done

    return response


if __name__ == '__main__':
    API.run(host='0.0.0.0')
