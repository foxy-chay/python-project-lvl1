"""Implements Brain Even gamepaly."""

from random import randint

from brain_games.cli import ask_user, tell_user_correct_answer


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
        generated_number = _generate_number(numbers_range)
        print('Question: {0}'.format(generated_number))

        # Ask user for answer
        user_answer = ask_user('Your answer: ')

        # Check answer correcteness
        expected_answer = 'yes' if _is_even(generated_number) else 'no'
        if user_answer.lower() != expected_answer:
            tell_user_correct_answer(expected_answer, user_answer.lower())
            return False

        print('Correct!')

    return True


def _generate_number(numbers_range):
    (minimal, maximal) = numbers_range
    return randint(minimal, maximal)


def _is_even(number):
    return number % 2 == 0
