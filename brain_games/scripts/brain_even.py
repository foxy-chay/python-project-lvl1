#!/usr/bin/env python3
"""Entrypoint of Brain Even game."""

from brain_games.brain_even import start_game
from brain_games.cli import welcome_user


def _cheer_up(user_name, success):
    if success:
        print('Congratulations, {0}!'.format(user_name))
    else:
        print("Let's try again, {0}!".format(user_name))


def main():
    """Start Brain Even game."""
    print('Welcome to the Brain Games!')
    user_name = welcome_user()

    # Game parameters
    game_rounds = 3
    numbers_range = (1, 100)

    success = start_game(game_rounds, numbers_range)
    _cheer_up(user_name, success)


if __name__ == '__main__':
    main()
