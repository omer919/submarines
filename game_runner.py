"""
Name: Omer Feldman

Class Name: game_runner.py

Purpose:  Submarines solution

Date: 29/12/2020

Changelog:   29/12/2020 - Init Project
"""

from abc import ABCMeta, abstractmethod


class GameRunner(metaclass=ABCMeta):
    @abstractmethod
    def run_game(self, this_player_turn: bool):
        pass
