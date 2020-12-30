"""
Name: Omer Feldman

Class Name: game_initializer.py

Purpose:  Submarines solution

Date: 29/12/2020

Changelog:   29/12/2020 - Init Project
"""

from board import Board
from game_properties import BoardSubmarines
from text_enemy_connection import TextEnemyConnection
from one_vs_one_game_runner import OneVsOneGameRunner
from client import Client
from server import Server
from game import Game


class GameInitializer:
    def __init__(self, board_height: int,
                 board_length: int,
                 is_player_first: bool,
                 port: int,
                 player_server_ip: str,
                 enemy_server_ip: str):
        self._board_height = board_height
        self._board_length = board_length
        self._is_player_first = is_player_first
        self._port = port
        self._player_server_ip = player_server_ip
        self._enemy_server_ip = enemy_server_ip

    def create_game(self):
        if self._is_player_first:
            socket_stream = Client(self._enemy_server_ip, self._port)
        else:
            socket_stream = Server(self._player_server_ip, self._port)

        socket_stream.connect_to_enemy()

        board = Board(self._board_length, self._board_height)
        board.add_submarine(BoardSubmarines.FIRST_SUBMARINE,
                            BoardSubmarines.FIRST_SUBMARINE_COORDINATES)
        board.add_submarine(BoardSubmarines.SECOND_SUBMARINE,
                            BoardSubmarines.SECOND_SUBMARINE_COORDINATES)
        board.add_submarine(BoardSubmarines.THIRD_SUBMARINE,
                            BoardSubmarines.THIRD_SUBMARINE_COORDINATES)
        board.add_submarine(BoardSubmarines.FOURTH_SUBMARINE,
                            BoardSubmarines.FOURTH_SUBMARINE_COORDINATES)
        board.add_submarine(BoardSubmarines.FIFTH_SUBMARINE,
                            BoardSubmarines.FIFTH_SUBMARINE_COORDINATES)
        enemy_connection = TextEnemyConnection(socket_stream)
        enemy_connection.initiate_connection(self._is_player_first)
        game_runner = OneVsOneGameRunner(board, enemy_connection)
        return Game(game_runner, self._is_player_first)
