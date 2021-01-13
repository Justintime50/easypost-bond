import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('WITHBOND_API_KEY')
HEADERS = {
    'X-BOND-KEY': API_KEY,
    'Content-Type': 'application/json'
}
BASE_URL = os.getenv('BASE_URL')


class Client():
    """The client class builds the API requests
    """
    API_BASE_URL = BASE_URL
    # Run some sanity checks on configuration
    if API_KEY is None:
        sys.exit(
            'No Withbond API key present. Please correct and restart the service.')
    if HEADERS is None:
        sys.exit(
            'No Withbond headers present. Please correct and restart the service.')
    if API_BASE_URL is None:
        sys.exit(
            'No Withbond base URL present. Please correct and restart the service.')

    @staticmethod
    def request(cls, http_method, endpoint, data=None):
        """Build the API request and return it to the method invoking it
        """
        request = requests.request(
            http_method, endpoint, headers=HEADERS, data=data)
        return request
