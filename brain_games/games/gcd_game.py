import random


INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def calculation(first_number, second_number):

    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number
    result = first_number + second_number

    return result


def make_question():

    num_min = 1
    num_max = 99
    random_number1 = random.randint(num_min, num_max)
    random_number2 = random.randint(num_min, num_max)
    question = '{} {}'.format(random_number1, random_number2)

    correct_answer = str(calculation(random_number1, random_number2))

    return (question, correct_answer)
