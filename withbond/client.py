"""This file builds the API request and houses shared constants"""
import os
from dotenv import load_dotenv
import requests

# Setup headers
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

    @classmethod
    def request(cls, httpMethod, endpoint, data=None):
        """Build the API request and return it to the method invoking it"""
        request = requests.request(
            httpMethod, endpoint, headers=HEADERS, data=data)
        return request
