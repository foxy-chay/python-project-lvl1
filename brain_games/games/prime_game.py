import random


INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_question():

    num_min = 1
    num_max = 99
    random_number = random.randint(num_min, num_max)
    is_number_Prime = isPrime(random_number)
    correct_answer = get_correct_answer(is_number_Prime)

    return (random_number, correct_answer)


def isPrime(number):

    if number % 2 == 0:
        return number == 2

    d = 3
    while d * d <= number and number % d != 0:
        d += 2
    return d * d > number


def get_correct_answer(is_number_prime):

    if is_number_prime:
        return 'yes'
    else:
        return 'no'
