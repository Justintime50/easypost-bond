"""This file builds the API request and houses shared constants"""
import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv('WITHBOND_API_KEY')
headers = {
            'X-BOND-KEY': API_KEY,
            'Content-Type': 'application/json'
          }

class Client():
    """The client class builds the API request and is used throughout the library"""
    VERSION = '1.0.0'
    API_BASE_URL = "https://public-api.int01.withbond.io/api/v1"
    

    @classmethod
    def request(cls, httpMethod, endpoint, data):
        
        """Build the API request and return it to the method invoking it"""
        response = requests.request(httpMethod, endpoint, headers=headers, data=data)
        return response
