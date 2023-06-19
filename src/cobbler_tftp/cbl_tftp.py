#!/usr/bin/env python3
# This source code is licensed under the MIT license

"""
tftp server with static file handling
"""

import os
import xmlrpc.client as xmlrpc

from fbtftp.base_handler import BaseHandler
from fbtftp.base_server import BaseServer
from jinja2 import Environment, FileSystemLoader, StrictUndefined


class CobblerConnection:
    def __init__(self, settings) -> None:
        self.hostname = settings.hostname
        self.user = settings.user
        self.password = settings.password
        self.password_file = settings.password_file
        self._connection = None

    def __repr__():
        print("Connection details:")
        print("hostname: {hostmane}")
        print("user: {user}")
        print("password: {password}")
        print("password file path: {password_file}")

    @property
    def connection(self):
        """Get current connection"""
        return self._connection

    @connection.setter
    def connection(self, user, password, hostname):
        self._connection = xmlrpc.ServerProxy("http://{user}:{password}@{hostname}")

    @connection.deleter
    def connection(self):
        del self._connection


# Represends the File returned by the cobbler server
class ReturnedFile:
    def __init__(self, filename):
        path = os.path.join(TFTP_ROOT, filename)
        self._size = os.stat(path).st_size
        self._reader = open(path, "rb")

    def read(self, data):
        return self._reader.read(data)

    def get_size(self):
        return self._size

    def close(self):
        self._reader.close()


class StaticHandler(BaseHandler):
    def get_response_data(self):
        return ReturnedFile(self._path)


class TftpServer(BaseServer):
    def get_handler(self, server_addr, peer, path, options):
        return StaticHandler(server_addr, peer, path, options, session_stats)


# render config template
def render_template(template, **kwargs):
    env = Environment(
        loader=FileSystemLoader(TEMPLATES_PATH),
        undefined=StrictUndefined,
        trim_blocks=True,
    )

    template = env.get_template(template)
    return template.render(**kwargs)


def session_stats(stats):
    print("")
    print("#" * 60)
    print("Peer: {} UDP/{}".format(stats.peer[0], stats.peer[1]))
    print("File: {}".format(stats.file_path))
    print("Sent Packets: {}".format(stats.packets_sent))
    print("#" * 60)
