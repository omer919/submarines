"""
Name: Omer Feldman

Class Name: socket_stream.py

Purpose:  Submarines solution

Date: 29/12/2020

Changelog:   29/12/2020 - Init Project
"""

from abc import ABCMeta, abstractmethod


class SocketStream(metaclass=ABCMeta):
    @abstractmethod
    def connect_to_enemy(self):
        pass

    @abstractmethod
    def send_message(self, message: bytes):
        pass

    @abstractmethod
    def receive_message(self, message_size: int):
        pass

    @abstractmethod
    def close_connection(self):
        pass
