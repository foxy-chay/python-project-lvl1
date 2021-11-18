from operator import mul, add, sub
import random


INSTRUCTION = 'What is the result of the expression?'


def make_question_and_correct_answer():

    num_min = 1
    num_max = 99
    random_number1 = random.randint(num_min, num_max)
    random_number2 = random.randint(num_min, num_max)
    operators = ('+', '-', '*')
    random_math_symbol = random.choice(operators)

    question = '{} {} {}'.format(random_number1,
                                 random_math_symbol, random_number2)
    correct_answer = str(calculate(random_number1,
                                   random_number2, random_math_symbol))

    return question, correct_answer


def calculate(first_number, second_number, math_symbol):
    dic = {'+': add, '-': sub, '*': mul}

    try:
        correct_answer = dic[math_symbol](first_number, second_number)
    except KeyError:
        print('Wrong math symbol')

    return correct_answer
