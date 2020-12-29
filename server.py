"""
Name: Omer Feldman

Class Name: server.py

Purpose:  Submarines solution

Date: 29/12/2020

Changelog:   29/12/2020 - Init Project
"""

from socket_stream import SocketStream
import socket


class Server(SocketStream):
    def __init__(self, server_ip: str, server_port: int, clients_listen: int):
        try:
            self.server_socket = socket.socket(socket.AF_INET,
                                               socket.SOCK_STREAM)
            self.server_socket.bind((server_ip, server_port))
            self.server_socket.listen(clients_listen)
            self.client_socket = None
        except socket.error as socket_error:
            raise socket_error

    def accept_connection(self):
        try:
            self.client_socket, _ = self.server_socket.accept()
        except socket.error as socket_error:
            raise socket_error

    def send_message(self, message: bytearray):
        if self.client_socket:
            try:
                self.client_socket.send(message)
            except socket.error as socket_error:
                raise socket_error

    def receive_message(self, message_size: int):
        if self.client_socket:
            try:
                return self.client_socket.recv(message_size)
            except socket.error as socket_error:
                raise socket_error
