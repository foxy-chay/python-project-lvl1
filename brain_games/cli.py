"""Set of functions to be used in comandline."""

import prompt


def ask_user(question):
    """Ask user a questin and wait for input.

    Args:
        question: Text with question for user.

    Returns:
        User's input.
    """
    return prompt.string(question)


def welcome_user():
    """Ask for username and greet in response.

    Returns:
        Username.
    """
    print('Welcome to the Brain Games!')
    user_name = ask_user('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    return user_name


def cheer_user_up(user_name, success):
    """Show the user an encouraging message.

    Args:
        user_name: Name user used for the game.
        success: Boolean value of the game outcome.
    """
    if success:
        print('Congratulations, {0}!'.format(user_name))
    else:
        print("Let's try again, {0}!".format(user_name))
