"""Implements Brain Even gamepaly."""

from random import randint

from brain_games.cli import ask_user


def start_game(game_rounds, numbers_range):
    """Manage the game process.

    Args:
        game_rounds: Integer that represents number of rounds
        numbers_range: A tuple with the first element as the maximum and \
    the second element as the minimum of the random range.

    Returns:
        True or False as a result of a successful or unsuccessful game.
    """
    for _ in range(game_rounds):
        # Generate and show user a number
        number = _generate_number(numbers_range)
        print('Question: {0}'.format(number))

        # Ask user for answer
        answer = ask_user('Your answer: ')

        # Check answer correcteness
        correct = _is_correct(number, answer)
        if correct:
            print('Correct!')
        else:
            return False

    return True


def _is_correct(generated_number, user_answer):
    user_answer = user_answer.lower()
    correct_answer = 'Yes' if _is_even(generated_number) else 'No'

    if user_answer.lower() != correct_answer.lower():
        print('"{0}" is wrong answer ;(. Correct answer was "{1}".'.format(
            user_answer, correct_answer,
        ))
        return False

    return True


def _generate_number(numbers_range):
    (minimal, maximal) = numbers_range
    return randint(minimal, maximal)


def _is_even(number):
    return number % 2 == 0
