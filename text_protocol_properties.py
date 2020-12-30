"""
Name: Omer Feldman

Class Name: text_protocol_properties.py

Purpose:  Submarines solution

Date: 29/12/2020

Changelog:   29/12/2020 - Init Project
"""

from game_status import GameErrorStatuses, BoardAttemptStatuses, GameStatuses


class TextProtocolProperties:
    PROTOCOL_VERSION = 1.0

    class PacketFields:
        VERSION_FIELD = "VERSION"
        TYPE_FIELD = "TYPE"
        STATUS_FIELD = "STATUS"
        X_COORDINATE = "X-COOR"
        Y_COORDINATE = "Y-COOR"

    class Types:
        READY = "READY"
        ATTEMPT = "ATTEMPT"
        ANSWER = "ANSWER"
        ERROR = "ERROR"

    class Statuses:
        class ErrorStatues:
            COORDINATE_OUT_OF_RANGE = "OUT-OF-RANGE"
            ATTEMPT_NOT_IN_TURN = "ATTEMPT-NOT-IN-TURN"
            CLOSED = "CLOSED"
            INVALID_PACKET = "UNEXPECTED"

        class AnswerStatus:
            CORRECT_ATTEMPT = "CORRECT"
            INCORRECT_ATTEMPT = "INCORRECT"
            FULL_SUB_HIT_ATTEMPT = "FULL-SUB"
            VICTORY_ATTEMPT = "VICTORY"

    ANSWER_STATUSES_TO_GAME_STATUSES = {
        Statuses.AnswerStatus.CORRECT_ATTEMPT: GameStatuses.PLAYER_ATTACK_SUCCESS,
        Statuses.AnswerStatus.VICTORY_ATTEMPT: GameStatuses.VICTORY_STATUS,
        Statuses.AnswerStatus.FULL_SUB_HIT_ATTEMPT: GameStatuses.PLAYER_ATTACK_FULL,
        Statuses.AnswerStatus.INCORRECT_ATTEMPT: GameStatuses.PLAYER_ATTACK_MISS
    }

    FORMATTED_GAME_STATUSES = {
        GameErrorStatuses.UNEXPECTED_MESSAGE: Statuses.ErrorStatues.INVALID_PACKET,
        GameErrorStatuses.UNEXPECTED_CLOSE: Statuses.ErrorStatues.CLOSED,
        GameErrorStatuses.ATTEMPT_NOT_IN_TURN: Statuses.ErrorStatues.ATTEMPT_NOT_IN_TURN,
        BoardAttemptStatuses.ENEMY_ATTACK_OUT_OF_MAP: Statuses.ErrorStatues.COORDINATE_OUT_OF_RANGE
    }