import random


INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question_and_correct_answer():
    num_min = 1
    num_max = 99
    question = random.randint(num_min, num_max)
    correct_answer = 'yes' if is_it_even(number) else 'no'

    return question, correct_answer


def is_it_even(number):
    if number % 2 == 0:
        return True

    else:
        return False
