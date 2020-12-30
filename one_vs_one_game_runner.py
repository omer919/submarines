"""
Name: Omer Feldman

Class Name: game_runner.py

Purpose:  Submarines solution

Date: 29/12/2020

Changelog:   29/12/2020 - Init Project
"""

from game_runner import GameRunner
from board import Board
from enemy_connection import EnemyConnection
import game_io
from typing import Tuple
from game_status import BoardAttemptStatuses, GameStatuses

GAME_STATUSES_ARGUMENTS = {
    GameStatuses.PLAYER_ATTACK_MISS: (False, False),
    GameStatuses.PLAYER_ATTACK_SUCCESS: (False, True),
    GameStatuses.PLAYER_ATTACK_FULL: (False, True),
    BoardAttemptStatuses.ENEMY_ATTACK_MISS: (False, True),
    BoardAttemptStatuses.ENEMY_ATTACK_SUCCESS: (False, False),
    BoardAttemptStatuses.ENEMY_ATTACK_FULL: (False, False),
    BoardAttemptStatuses.ENEMY_ATTACKED_ALL_SUBMARINES: (True, False),
    GameStatuses.ERROR_STATUS: (True, False),
    GameStatuses.VICTORY_STATUS: (True, False)}


class OneVsOneGameRunner(GameRunner):
    def __init__(self, board: Board, enemy_connection: EnemyConnection):
        self._board = board
        self._enemy_connection = enemy_connection
        self._connection_board_commands = {}
        self._expected_close = True
        self.fill_connection_board_commands()

    def fill_connection_board_commands(self):
        self._connection_board_commands[
            BoardAttemptStatuses.ENEMY_ATTACK_MISS] =\
            self._enemy_connection.send_enemy_attack_miss
        self._connection_board_commands[
            BoardAttemptStatuses.ENEMY_ATTACK_SUCCESS] =\
            self._enemy_connection.send_enemy_attack_success
        self._connection_board_commands[
            BoardAttemptStatuses.ENEMY_ATTACK_FULL] =\
            self._enemy_connection.send_enemy_attack_full_submarine
        self._connection_board_commands[
            BoardAttemptStatuses.ENEMY_ATTACK_OUT_OF_MAP] =\
            self._enemy_connection.send_error
        self._connection_board_commands[
            BoardAttemptStatuses.ENEMY_ATTACKED_ALL_SUBMARINES] =\
            self._enemy_connection.send_enemy_victory

    def handle_enemy_answer(self, status: int):
        if status == GameStatuses.ERROR_STATUS:
            return self.handle_error(status)
        game_io.print_status_message(status)
        return GAME_STATUSES_ARGUMENTS[status]

    def handle_error(self, error_code: int):
        if error_code == BoardAttemptStatuses.ENEMY_ATTACK_OUT_OF_MAP:
            self._connection_board_commands[error_code](error_code)
            game_io.print_status_message(error_code)
        else:
            game_io.print_error(self._enemy_connection.get_last_error())
        self._expected_close = False
        return GAME_STATUSES_ARGUMENTS[GameStatuses.ERROR_STATUS]

    def handle_board_status(self, status: int, coordinate: Tuple[int, int]):
        if status == BoardAttemptStatuses.ENEMY_ATTACK_OUT_OF_MAP or\
                status == GameStatuses.ERROR_STATUS:
            return self.handle_error(status)
        game_io.print_enemy_attempt_coordinate(coordinate)
        game_io.print_status_message(status)
        self._connection_board_commands[status](coordinate)
        return GAME_STATUSES_ARGUMENTS[status]

    def do_player_turn(self) -> Tuple[bool, bool]:
        coordinate = game_io.get_coordinate_to_hit(self._board.length,
                                                   self._board.height)
        self._enemy_connection.attempt_hit_at_coordinate(coordinate)
        return self.handle_enemy_answer(self._enemy_connection.get_answer())

    def do_enemy_turn(self) -> Tuple[bool, bool]:
        status, coordinate = self._enemy_connection.get_attempt()
        if status == GameStatuses.ENEMY_ATTEMPT_HIT:
            return self.handle_board_status(
                self._board.hit_submarine_at_coordinate(coordinate),
                coordinate)
        return self.handle_board_status(status, coordinate)

    def run_game(self, is_this_player_turn: bool):
        end_game = False
        while not end_game:
            game_io.print_board(self._board)
            if is_this_player_turn:
                end_game, is_this_player_turn = self.do_player_turn()
            else:
                end_game, is_this_player_turn = self.do_enemy_turn()
        self._enemy_connection.close_connection(self._expected_close)
