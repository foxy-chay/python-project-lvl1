#!/usr/bin/env python3
"""Entrypoint of Brain Games app."""

from brain_games.cli import welcome_user


def main():
    """Start Brain Games app."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
