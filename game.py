"""
Name: Omer Feldman

Class Name: game.py

Purpose:  Submarines solution

Date: 29/12/2020

Changelog:   29/12/2020 - Init Project
"""

from game_runner import GameRunner


class Game:
    def __init__(self, game_runner: GameRunner, is_player_first: bool):
        self._game_runner = game_runner
        self._is_player_first = is_player_first

    def run_game(self):
        self._game_runner.run_game(self._is_player_first)
