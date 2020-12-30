"""
Name: Omer Feldman

Class Name: game_properties.py

Purpose:  Submarines solution

Date: 29/12/2020

Changelog:   29/12/2020 - Init Project
"""

from submarine import Submarine


IS_PLAYER_FIRST = True


class BoardProperties:
    BOARD_LENGTH = 10
    BOARD_HEIGHT = 10


class BoardSubmarines:
    FIRST_SUBMARINE = Submarine(3)
    FIRST_SUBMARINE_COORDINATES = [(1, 1), (1, 2), (1, 3)]

    SECOND_SUBMARINE = Submarine(3)
    SECOND_SUBMARINE_COORDINATES = [(2, 5), (2, 6), (2, 7)]

    THIRD_SUBMARINE = Submarine(2)
    THIRD_SUBMARINE_COORDINATES = [(9, 7), (9, 8)]

    FOURTH_SUBMARINE = Submarine(4)
    FOURTH_SUBMARINE_COORDINATES = [(4, 8), (5, 8), (6, 8), (7, 8)]

    FIFTH_SUBMARINE = Submarine(5)
    FIFTH_SUBMARINE_COORDINATES = [(7, 1), (7, 2), (7, 3), (7, 4), (7, 5)]


class SocketProperties:
    PORT = 3000
    PLAYER_SERVER_IP = '0.0.0.0'
    ENEMY_SERVER_IP = '192.168.77.21'#FILL THIS PLEASE


class GameMessages:
    PLAYER_HIT_SUCCESSFUL_MESSAGE = "You hit an enemy's submarine!"
    PLAYER_HIT_MISSED_MESSAGE = "Your hit missed!"
    PLAYER_HIT_FULL_SUBMARINE_MESSAGE = "Your hit sank an enemy's submarine!"
    ENEMY_HIT_SUCCESSFUL_MESSAGE = "Enemy hit a submarine!"
    ENEMY_HIT_MISSED_MESSAGE = "Enemy hit missed!"
    ENEMY_HIT_FULL_SUBMARINE_MESSAGE = "Enemy hit sank a submarine!"
    VICTORY_MESSAGE = "All of the enemy's submarines sank, you won!"
    LOSE_MESSAGE = "All your submarines sank, you lost!"


class ErrorMessages:
    ENEMY_HIT_OUT_OF_RANGE = "Error: Enemy tried hitting" \
                             " a coordinate out of the map"
