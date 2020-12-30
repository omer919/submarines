"""
Name: Omer Feldman

Class Name: text_enemy_connection.py

Purpose:  Submarines solution

Date: 29/12/2020

Changelog:   29/12/2020 - Init Project
"""

from enemy_connection import EnemyConnection
from socket_stream import SocketStream
from typing import Tuple
from game_status import GameErrorStatuses, GameStatuses
from text_protocol_properties import TextProtocolProperties
import text_protocol_formatter
import text_protocol_parser


class TextEnemyConnection(EnemyConnection):
    def __init__(self, socket_stream: SocketStream):
        self._socket_stream = socket_stream
        self._last_error = ""

    def send_message_to_enemy(self, message: str):
        self._socket_stream.send_message(message.encode())

    def get_message_from_enemy(self) -> str:
        return self._socket_stream.receive_message(4096).decode()

    def send_enemy_attack_miss(self, coordinate: Tuple[int, int]):
        miss_error = text_protocol_formatter.create_answer_message(
            coordinate,
            [TextProtocolProperties.Statuses.AnswerStatus.INCORRECT_ATTEMPT])
        self.send_message_to_enemy(miss_error)

    def send_enemy_attack_success(self, coordinate: Tuple[int, int]):
        attack_success_message = text_protocol_formatter.create_answer_message(
            coordinate,
            [TextProtocolProperties.Statuses.AnswerStatus.CORRECT_ATTEMPT])
        self.send_message_to_enemy(attack_success_message)

    def send_enemy_attack_full_submarine(self, coordinate: Tuple[int, int]):
        attack_full_message = text_protocol_formatter.create_answer_message(
            coordinate,
            [TextProtocolProperties.Statuses.AnswerStatus.CORRECT_ATTEMPT,
             TextProtocolProperties.Statuses.AnswerStatus.FULL_SUB_HIT_ATTEMPT]
        )
        self.send_message_to_enemy(attack_full_message)

    def send_error(self, error_status: int):
        error_message = text_protocol_formatter.create_error_message(
            TextProtocolProperties.FORMATTED_GAME_STATUSES[error_status])
        self.send_message_to_enemy(error_message)

    def send_enemy_victory(self, coordinate: Tuple[int, int]):
        victory_message = text_protocol_formatter.create_answer_message(
            coordinate,
            [TextProtocolProperties.Statuses.AnswerStatus.CORRECT_ATTEMPT,
             TextProtocolProperties.Statuses.AnswerStatus.VICTORY_ATTEMPT])
        self.send_message_to_enemy(victory_message)

    def attempt_hit_at_coordinate(self, coordinate: Tuple[int, int]):
        attempt_hit_message = text_protocol_formatter.create_attempt_message(
            coordinate)
        self.send_message_to_enemy(attempt_hit_message)

    def get_answer(self) -> int:
        message = self.get_message_from_enemy()
        is_valid, parsed_message = text_protocol_parser.parse_message(message)

        type_field = TextProtocolProperties.PacketFields.TYPE_FIELD
        status_field = TextProtocolProperties.PacketFields.STATUS_FIELD
        error_type = TextProtocolProperties.Types.ERROR

        correct = TextProtocolProperties.Statuses.AnswerStatus.CORRECT_ATTEMPT
        incorrect = TextProtocolProperties.Statuses.AnswerStatus.INCORRECT_ATTEMPT
        victory = TextProtocolProperties.Statuses.AnswerStatus.VICTORY_ATTEMPT
        full_sub = TextProtocolProperties.Statuses.AnswerStatus.FULL_SUB_HIT_ATTEMPT

        if parsed_message[type_field] == error_type:
            self._last_error = parsed_message[status_field]
            return GameStatuses.ERROR_STATUS
        if victory in parsed_message[status_field]:
            answer_status = victory
        elif full_sub in parsed_message[status_field]:
            answer_status = full_sub
        else:
            answer_status = parsed_message[status_field]
        return TextProtocolProperties.ANSWER_STATUSES_TO_GAME_STATUSES[
            answer_status]

    def get_attempt(self) -> Tuple[int, Tuple[int, int]]:
        message = self.get_message_from_enemy()
        is_valid, parsed_message = text_protocol_parser.parse_message(message)


        type_field = TextProtocolProperties.PacketFields.TYPE_FIELD
        status_field = TextProtocolProperties.PacketFields.STATUS_FIELD
        x_cord_field = TextProtocolProperties.PacketFields.X_COORDINATE
        y_cord_field = TextProtocolProperties.PacketFields.Y_COORDINATE
        error_type = TextProtocolProperties.Types.ERROR

        attempt_cords = (-1, -1)
        if parsed_message[type_field] == error_type:
            self._last_error = parsed_message[status_field]
            return GameStatuses.ERROR_STATUS, attempt_cords
        attempt_cords = (int(parsed_message[x_cord_field]), int(parsed_message[y_cord_field]))

        return GameStatuses.ENEMY_ATTEMPT_HIT, attempt_cords

    def get_last_error(self):
        return self._last_error

    def close_connection(self, expected_close: bool):
        if not expected_close:
            self.send_error(GameErrorStatuses.UNEXPECTED_CLOSE)
        self._socket_stream.close_connection()

    def send_ready_message(self):
        ready_message = text_protocol_formatter.create_ready_message()
        self.send_message_to_enemy(ready_message)

    def initiate_connection(self, is_player_first: bool):
        if is_player_first:
            self.send_ready_message()
            _ = self.get_message_from_enemy()
        else:
            _ = self.get_message_from_enemy()
            self.send_ready_message()