"""
Name: Omer Feldman

Class Name: game_io.py

Purpose:  Submarines solution

Date: 29/12/2020

Changelog:   29/12/2020 - Init Project
"""

from typing import Tuple
from game_properties import GameMessages, ErrorMessages
from game_status import BoardAttemptStatuses, GameStatuses
from board import Board

GAME_STATUSES_MESSAGES = {
    BoardAttemptStatuses.ENEMY_ATTACK_MISS:
        GameMessages.ENEMY_HIT_MISSED_MESSAGE,
    BoardAttemptStatuses.ENEMY_ATTACK_SUCCESS:
        GameMessages.ENEMY_HIT_SUCCESSFUL_MESSAGE,
    BoardAttemptStatuses.ENEMY_ATTACK_FULL:
        GameMessages.ENEMY_HIT_FULL_SUBMARINE_MESSAGE,
    BoardAttemptStatuses.ENEMY_ATTACK_OUT_OF_MAP:
        ErrorMessages.ENEMY_HIT_OUT_OF_RANGE,
    BoardAttemptStatuses.ENEMY_ATTACKED_ALL_SUBMARINES:
        GameMessages.LOSE_MESSAGE,
    GameStatuses.PLAYER_ATTACK_MISS:
        GameMessages.PLAYER_HIT_MISSED_MESSAGE,
    GameStatuses.PLAYER_ATTACK_SUCCESS:
        GameMessages.PLAYER_HIT_SUCCESSFUL_MESSAGE,
    GameStatuses.PLAYER_ATTACK_FULL:
        GameMessages.PLAYER_HIT_FULL_SUBMARINE_MESSAGE,
    GameStatuses.VICTORY_STATUS:
        GameMessages.VICTORY_MESSAGE}


def is_cord_valid(cord: str, boarder: int) -> bool:
    return cord.isdigit() and (0 <= int(cord) < boarder)


def get_coordinate(boarder: int, coordinate_information: str) -> str:
    return input(f"Enter the {coordinate_information} (must be between 0"
                 f" and {boarder} [not including]): ")


def get_valid_coordinate(boarder: int, coordinate_information: str) -> int:
    cord = get_coordinate(boarder, coordinate_information)
    while not is_cord_valid(cord, boarder):
        print("Invalid Input, please try again")
        cord = get_coordinate(boarder, coordinate_information)
    return int(cord)


def get_coordinate_to_hit(board_length: int, board_height: int) -> Tuple[int,
                                                                         int]:
    print("> Enter coordinate to attempt hitting <")
    x = get_valid_coordinate(board_length, 'X')
    y = get_valid_coordinate(board_height, 'Y')
    return x, y


def print_status_message(status: int):
    print(GAME_STATUSES_MESSAGES[status])


def print_error(error_message: str):
    print(f"Error: {error_message}")


def print_enemy_attempt_coordinate(coordinate: Tuple[int, int]):
    print(f"Enemy attempt hitting at: {coordinate}")


def print_board(board: Board):
    print(f"> Your Board <\n{board}")