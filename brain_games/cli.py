"""Set of functions to be used in comandline."""

import prompt


def welcome_user():
    """Says hello to user.

    Returns:
        Greeting with user name.
    """
    name = prompt.string('May I have your name? ')
    return 'Hello, {0}!'.format(name)
