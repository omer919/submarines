"""
Name: Omer Feldman

Class Name: enemy_connection.py

Purpose:  Submarines solution

Date: 29/12/2020

Changelog:   29/12/2020 - Init Project
"""

from abc import ABCMeta, abstractmethod
from typing import Tuple


class EnemyConnection(metaclass=ABCMeta):
    @abstractmethod
    def send_enemy_attack_miss(self, coordinate: Tuple[int, int]):
        pass

    @abstractmethod
    def send_enemy_attack_success(self, coordinate: Tuple[int, int]):
        pass

    @abstractmethod
    def send_enemy_attack_full_submarine(self, coordinate: Tuple[int, int]):
        pass

    @abstractmethod
    def send_error(self, error_status: int):
        pass

    @abstractmethod
    def send_enemy_victory(self, coordinate: Tuple[int, int]):
        pass

    @abstractmethod
    def initiate_connection(self, is_player_first: bool):
        pass

    @abstractmethod
    def get_last_error(self) -> str:
        pass

    @abstractmethod
    def get_answer(self) -> int:
        pass

    @abstractmethod
    def attempt_hit_at_coordinate(self, coordinate: Tuple[int, int]):
        pass

    @abstractmethod
    def get_attempt(self) -> Tuple[int, Tuple[int, int]]:
        pass

    @abstractmethod
    def close_connection(self, expected_close: bool):
        pass

