"""Import API modules"""
from threading import Thread
import json
import os
from flask import Flask, request, abort

API = Flask(__name__)


@API.route('/shipment', methods=['POST'])
def shipment():
    """Create a shipment"""
    # TODO


if __name__ == '__main__':
    API.run(host='0.0.0.0')
