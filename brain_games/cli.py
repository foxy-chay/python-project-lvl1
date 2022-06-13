"""Set of functions to be used in comandline."""

import prompt


def welcome_user():
    """Ask for username and greet in response.

    Returns:
        Username.
    """
    print('Welcome to the Brain Games!')
    user_name = ask_user('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    return user_name


def ask_user(question):
    """Ask user a questin and wait for input.

    Args:
        question: Text with question for user.

    Returns:
        User's input.
    """
    return prompt.string(question)


def tell_user_correct_answer(expected_answer, user_answer):
    """Tell user what was the correct answer.

    Args:
        expected_answer: What game expects to get from user.
        user_answer: User's on task answers.
    """
    print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
        user_answer, expected_answer,
    ))


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
