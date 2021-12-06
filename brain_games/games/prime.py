import random

NUMBER_MIN = 1
NUMBER_MAX = 99
INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_question_and_correct_answer():
    random_number = random.randint(NUMBER_MIN, NUMBER_MAX)
    correct_answer = 'yes' if is_it_prime(random_number) else 'no'
    return random_number, correct_answer


def is_it_prime(number):
    if number % 2 == 0:
        return number == 2

    d = 3
    while d * d <= number and number % d != 0:
        d += 2
    return d * d > number
