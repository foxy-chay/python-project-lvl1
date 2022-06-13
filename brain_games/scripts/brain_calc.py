#!/usr/bin/env python3
"""Entrypoint of Brain Calc game."""

from brain_games.brain_calc import start_game
from brain_games.cli import cheer_user_up, welcome_user


def main():
    """Start Brain Calc game."""
    user_name = welcome_user()

    # Game parameters
    game_rounds = 3
    max_number = 1000

    success = start_game(game_rounds, max_number)
    cheer_user_up(user_name, success)


if __name__ == '__main__':
    main()
