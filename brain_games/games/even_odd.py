import random

NUMBER_MIN = 1
NUMBER_MAX = 99
INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question_and_correct_answer():
    question = random.randint(NUMBER_MIN, NUMBER_MAX)
    correct_answer = 'yes' if is_it_even(question) else 'no'

    return question, correct_answer


def is_it_even(number):
    return number % 2 == 0
