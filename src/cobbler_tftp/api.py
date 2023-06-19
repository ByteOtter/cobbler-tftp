"""
Handle authentication and requests against cobbler's XMLRPC-API.
"""

import xmlrpc.client as xmlrpc

import requests
from cbl_tfpt import CobblerConnection


def authenticate(settings):
    pass


def create_connection(settings):
    connection = xmlrpc.ServerProxy(
        "http://{settings['username']}:{settings['password']}@{settings['uri']}"
    )
    return connection


def get_config_schema():
    """
    Get boot configuration schema from Cobbler.
    """
    pass
