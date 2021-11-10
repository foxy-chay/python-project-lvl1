import prompt
import random


def greeting():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def random_number():
    i = random.randint(1, 99)
    return i


def request_answer():
    answer = prompt.string('Your answer: ')
    return answer


def response_to_user(name, func_user_response):
    index = 0
    number_of_rounds = 3
    while index < number_of_rounds:
        right_answer, user_answer, is_answer_correct = func_user_response()
        if is_answer_correct:
            index += 1
        else:
            print("'{}' is wrong answer ;(. \
            Correct answer was '{}'".format(user_answer, right_answer))
            print("Let's try again, {}!".format(name))
            break
        print('Congratulations, {}!'.format(name))


def get_math_symbol():
    math_symbols = ('+', '-', '*')
    index = random.randint(0, 2)
    return math_symbols[index]


def check_user_answer(right_answer, user_answer):
    x = int(right_answer)
    y = int(user_answer)
    if x == y:
        print('Correct!')
        return True
    return False
