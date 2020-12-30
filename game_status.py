"""
Name: Omer Feldman

Class Name: game_status.py

Purpose:  Submarines solution

Date: 29/12/2020

Changelog:   29/12/2020 - Init Project
"""


class BoardAttemptStatuses:
    ENEMY_ATTACK_MISS = 0
    ENEMY_ATTACK_SUCCESS = 1
    ENEMY_ATTACK_FULL = 2
    ENEMY_ATTACK_OUT_OF_MAP = 3
    ENEMY_ATTACKED_ALL_SUBMARINES = 4


class GameStatuses:
    ERROR_STATUS = 5
    VICTORY_STATUS = 6
    ENEMY_ATTEMPT_HIT = 7
    PLAYER_ATTACK_MISS = 8
    PLAYER_ATTACK_SUCCESS = 9
    PLAYER_ATTACK_FULL = 10


class GameErrorStatuses:
    UNEXPECTED_MESSAGE = 11
    UNEXPECTED_CLOSE = 12
    ATTEMPT_NOT_IN_TURN = 13
