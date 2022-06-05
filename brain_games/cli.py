"""Set of functions to be used in comandline."""

import prompt


def ask_user(question):
    """Asks user a passed questin and waits for input.

    Args:
        question: Text with question for user.

    Returns:
        User's input.
    """
    return prompt.string(question)


def welcome_user():
    """Asks for username and greets in response.

    Returns:
        Username.
    """
    user_name = ask_user('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    return user_name
