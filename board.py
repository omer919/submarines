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
from game_properties import BoardAttemptStatues


class Board:
    def __init__(self):
        self._coordinates_with_submarines = {}

    def is_submarine_at_coordinate(self, coordinate: Tuple):
        return coordinate in self._coordinates_with_submarines

    def are_all_submarines_sunken(self):
        for coordinate in self._coordinates_with_submarines:
            if not self._coordinates_with_submarines[coordinate].is_sunken:
                return False
        return True

    def add_submarine(self, submarine: Submarine, coordinates: List[Tuple]):
        for coordinate in coordinates:
            self._coordinates_with_submarines[coordinate] = submarine

    def hit_submarine_at_coordinate(self, coordinate: Tuple) -> int:
        if self.is_submarine_at_coordinate(coordinate):
            submarine = self._coordinates_with_submarines[coordinate]
            if not submarine.is_sunken:
                submarine.hit_submarine()
                if submarine.is_sunken:
                    return BoardAttemptStatues.SUBMARINE_SINK
                else:
                    return BoardAttemptStatues.SUBMARINE_HIT_SUCCESS
        return BoardAttemptStatues.SUBMARINE_HIT_MISS
