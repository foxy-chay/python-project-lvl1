#!/usr/bin/env python3
"""Main script to run brain_games app."""

from brain_games.cli import welcome_user


def main():
    """Beggining of Brain Games app."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
