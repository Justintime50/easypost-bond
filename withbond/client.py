"""This file builds the API request and houses shared constants"""
import os
import sys
from dotenv import load_dotenv
import requests

# Setup headers and variables
load_dotenv()
API_KEY = os.getenv('WITHBOND_API_KEY')
HEADERS = {
    'X-BOND-KEY': API_KEY,
    'Content-Type': 'application/json'
}
BASE_URL = os.getenv('BASE_URL')


class Client():
    """The client class builds the API requests"""
    API_BASE_URL = BASE_URL
    # Run some sanity checks on configuration
    if API_KEY == None:
        sys.exit(
            'No Withbond API key present. Please correct and restart the service.')
    if HEADERS == None:
        sys.exit(
            'No Withbond headers present. Please correct and restart the service.')
    if API_BASE_URL == None:
        sys.exit(
            'No Withbond base URL present. Please correct and restart the service.')

    @classmethod
    def request(cls, httpMethod, endpoint, data=None):
        """Build the API request and return it to the method invoking it"""
        request = requests.request(
            httpMethod, endpoint, headers=HEADERS, data=data)
        return request
