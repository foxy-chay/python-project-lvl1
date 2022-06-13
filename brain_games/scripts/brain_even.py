#!/usr/bin/env python3
"""Entrypoint of Brain Even game."""

from brain_games.cli import cheer_user_up, welcome_user
from brain_games.games.brain_even import start_game


def main():
    """Start Brain Even game."""
    user_name = welcome_user()

    # Game parameters
    game_rounds = 3
    numbers_range = (1, 100)

    success = start_game(game_rounds, numbers_range)
    cheer_user_up(user_name, success)


if __name__ == '__main__':
    main()
