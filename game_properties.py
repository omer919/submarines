"""
Name: Omer Feldman

Class Name: game_properties.py

Purpose:  Submarines solution

Date: 29/12/2020

Changelog:   29/12/2020 - Init Project
"""


class BoardProperties:
    BOARD_LENGTH = 10
    BOARD_HEIGHT = 10


class SocketProperties:
    PORT = 3000
    MY_SERVER_IP = '0.0.0.0'
    MY_CLIENT_IP = '127.0.0.1'
    ENEMY_SERVER_IP = ''#FILL THIS PLEASE


class ProtocolProperties:
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


class BoardAttemptStatues:
    SUBMARINE_HIT_SUCCESS = 0
    SUBMARINE_HIT_MISS = 1
    SUBMARINE_SINK = 2