from operator import mul, add, sub
import random

NUMBER_MIN = 1
NUMBER_MAX = 99
INSTRUCTION = 'What is the result of the expression?'


def make_question_and_correct_answer():
    random_number1 = random.randint(NUMBER_MIN, NUMBER_MAX)
    random_number2 = random.randint(NUMBER_MIN, NUMBER_MAX)
    operators = ('+', '-', '*')
    random_math_symbol = random.choice(operators)

    question = '{} {} {}'.format(random_number1,
                                 random_math_symbol, random_number2)
    correct_answer = str(calculate_result(random_number1,
                                          random_number2, random_math_symbol))

    return question, correct_answer


def calculate_result(first_number, second_number, math_symbol):
    dic = {'+': add, '-': sub, '*': mul}

    try:
        correct_answer = dic[math_symbol](first_number, second_number)
    except KeyError:
        error_message = "Wrong math symbol"
        print(error_message)
        raise KeyError(error_message)

    return correct_answer
