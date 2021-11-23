import random

NUMBER_MIN = 1
NUMBER_MAX = 99
INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def calculate_result(first_number, second_number):
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number
    result = first_number + second_number

    return result


def make_question_and_correct_answer():
    random_number1 = random.randint(NUMBER_MIN, NUMBER_MAX)
    random_number2 = random.randint(NUMBER_MIN, NUMBER_MAX)
    question = '{} {}'.format(random_number1, random_number2)

    correct_answer = str(calculate_result(random_number1, random_number2))

    return question, correct_answer
