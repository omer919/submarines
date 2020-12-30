"""
Name: Omer Feldman

Class Name: board.py

Purpose:  Submarines solution

Date: 29/12/2020

Changelog:   29/12/2020 - Init Project
"""

from submarine import Submarine
from typing import List
from typing import Tuple
from game_status import BoardAttemptStatuses

X_INDEX = 0
Y_INDEX = 1
MIN_POSSIBLE_X = 0
MIN_POSSIBLE_Y = 0
SUBMARINE_INDEX = 0
ALREADY_ATTACKED_INDEX = 1


class Board:
    def __init__(self, height: int, length: int):
        self._height = height
        self._length = length
        self._coordinates_with_submarines = {}

    def __str__(self):
        board_visualize = \
            [["-" for _ in range(self._length)] for _ in range(self._height)]
        for coordinate in self._coordinates_with_submarines:
            if self._coordinates_with_submarines[coordinate][ALREADY_ATTACKED_INDEX]:
                board_visualize[coordinate[Y_INDEX]][coordinate[X_INDEX]] = "*"
            else:
                board_visualize[coordinate[Y_INDEX]][coordinate[X_INDEX]] = "X"

        final_buffer = ""
        for y in range(self._height):
            temp_buffer = ""
            for x in range(self._length):
                temp_buffer += board_visualize[y][x]
            final_buffer += temp_buffer + "\n"

        return final_buffer

    @property
    def height(self):
        return self._height

    @property
    def length(self):
        return self._length

    def is_coordinate_on_map(self, coordinate: Tuple[int, int]) -> bool:
        return (MIN_POSSIBLE_X <= coordinate[X_INDEX] < self._length) and\
               (MIN_POSSIBLE_Y <= coordinate[Y_INDEX] < self._height)

    def is_submarine_at_coordinate(self, coordinate: Tuple[int, int]) -> bool:
        return coordinate in self._coordinates_with_submarines

    def are_all_submarines_sunken(self) -> bool:
        for coordinate in self._coordinates_with_submarines:
            if not self._coordinates_with_submarines[coordinate][SUBMARINE_INDEX].is_sunken:
                return False
        return True

    def are_all_coordinates_on_map(self,
                                   coordinates: List[Tuple[int, int]]) -> bool:
        for coordinate in coordinates:
            if not self.is_coordinate_on_map(coordinate):
                return False
        return True

    def add_submarine(self, submarine: Submarine,
                      coordinates: List[Tuple[int, int]]):
        if self.are_all_coordinates_on_map(coordinates):
            for coordinate in coordinates:
                self._coordinates_with_submarines[coordinate] = [submarine, False]

    def hit_submarine_at_coordinate(self, coordinate: Tuple[int, int]) -> int:
        if self.is_coordinate_on_map(coordinate):
            if self.is_submarine_at_coordinate(coordinate) and not self._coordinates_with_submarines[coordinate][ALREADY_ATTACKED_INDEX]:
                submarine = self._coordinates_with_submarines[coordinate][SUBMARINE_INDEX]
                if not submarine.is_sunken:
                    submarine.hit_submarine()
                    self._coordinates_with_submarines[coordinate][ALREADY_ATTACKED_INDEX] = True
                    if submarine.is_sunken:
                        if self.are_all_submarines_sunken():
                            return BoardAttemptStatuses.\
                                ENEMY_ATTACKED_ALL_SUBMARINES
                        return BoardAttemptStatuses.ENEMY_ATTACK_FULL
                    else:
                        return BoardAttemptStatuses.ENEMY_ATTACK_SUCCESS
            return BoardAttemptStatuses.ENEMY_ATTACK_MISS
        return BoardAttemptStatuses.ENEMY_ATTACK_OUT_OF_MAP
