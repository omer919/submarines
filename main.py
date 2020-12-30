"""
Name: Omer Feldman

Class Name: main.py

Purpose:  Submarines solution

Date: 29/12/2020

Changelog:   29/12/2020 - Init Project
"""

from game_initializer import GameInitializer
from game_properties import BoardProperties, SocketProperties, IS_PLAYER_FIRST


def main():
    """

    """
    game_initializer = GameInitializer(BoardProperties.BOARD_LENGTH,
                                       BoardProperties.BOARD_HEIGHT,
                                       IS_PLAYER_FIRST,
                                       SocketProperties.PORT,
                                       SocketProperties.PLAYER_SERVER_IP,
                                       SocketProperties.ENEMY_SERVER_IP)
    game = game_initializer.create_game()
    game.run_game()




if __name__ == '__main__':
    main()
