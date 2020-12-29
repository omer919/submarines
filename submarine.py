"""
Name: Omer Feldman

Class Name: submarine.py

Purpose:  Submarines solution

Date: 29/12/2020

Changelog:   29/12/2020 - Init Project
"""


class Submarine:
    def __init__(self, size: int):
        self._size = size
        self._hits = 0
        self._is_sunken = False

    @property
    def is_sunken(self):
        return self._is_sunken

    def should_sink_submarine(self):
        return self._hits == self._size

    def sink_submarine(self):
        self._is_sunken = True

    def hit_submarine(self):
        if not self._is_sunken:
            self._hits += 1
            if self.should_sink_submarine():
                self.sink_submarine()
