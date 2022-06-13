"""Implements Brain Calc gameplay."""

from random import choice, randint

from brain_games.cli import ask_user


def start_game(game_rounds, max_number):
    """Manage Brain Calc gamplay.

    Args:
        game_rounds: Integer that represents number of rounds.
        max_number: Intergre that defines max value of generated numbers.

    Returns:
        True or False as a result of a successful or unsuccessful game.
    """
    for _ in range(game_rounds):
        # Generate and show user a number
        expected_answer = _generate_math_task(max_number)

        # Ask user for answer
        user_answer = ask_user('Your answer: ')

        # Check answer correcteness
        correct = _is_correct(expected_answer, user_answer)
        if correct:
            print('Correct!')
        else:
            return False

    return True


def _is_correct(expected_answer, user_answer):
    if int(user_answer) != int(expected_answer):
        print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
            user_answer, expected_answer,
        ))
        return False

    return True


def _generate_math_task(max_number):
    operation = _generate_operation()
    first_operand = randint(0, max_number)
    second_operand = randint(0, max_number)
    print('Question: {1} {0} {2}'.format(
        operation, first_operand, second_operand,
    ))
    if operation == '+':
        return first_operand + second_operand
    elif operation == '-':
        return first_operand - second_operand
    elif operation == '*':
        return first_operand * second_operand
    raise ValueError('Application generated incorrect math operation')


def _generate_operation():
    return choice('+-*')
