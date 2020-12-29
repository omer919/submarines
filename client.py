"""
Name: Omer Feldman

Class Name: client.py

Purpose:  Submarines solution

Date: 29/12/2020

Changelog:   29/12/2020 - Init Project
"""

from socket_stream import SocketStream
import socket


class Client(SocketStream):
    def __init__(self, server_ip: str, server_port: int):
        try:
            self.client_socket = socket.socket(socket.AF_INET,
                                               socket.SOCK_STREAM)
            self._server_ip = server_ip
            self._server_port = server_port
            self._is_connected = False
        except socket.error as socket_error:
            raise socket_error

    def connect_to_server(self):
        try:
            self.client_socket.connect((self._server_ip, self._server_port))
            self._is_connected = True
        except socket.error as socket_error:
            raise socket_error

    def send_message(self, message: bytearray):
        if self._is_connected:
            try:
                self.client_socket.send(message)
            except socket.error as socket_error:
                raise socket_error

    def receive_message(self, message_size: int):
        if self._is_connected:
            try:
                return self.client_socket.recv(message_size)
            except socket.error as socket_error:
                raise socket_error
