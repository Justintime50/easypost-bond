"""This file builds the API request and houses shared constants"""
import requests


class Client():
    """The client class builds the API request and is used throughout the library"""
    VERSION = '1.0.0'
    API_BASE_URL = "https://public-api.int01.withbond.io/api/v1/"

    @classmethod
    def response(cls, data, endpoint):
        """Build the API request and return it to the method invoking it"""
        request = requests.post(endpoint, data=data)
        return request
