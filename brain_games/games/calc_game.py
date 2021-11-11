from operator import mul, add, sub
from brain_games.games import functions


def start():

    name = functions.greeting()
    print('What is the result of the expression?')
    functions.response_to_user(name, game)


def game():

    right_answer = make_question()
    user_answer = functions.request_answer()
    is_answer_correct = functions.check_user_answer(right_answer, user_answer)

    return (right_answer, user_answer, is_answer_correct)


def make_question():

    num1 = 1
    num2 = 99
    random_number1 = functions.random_number(num1, num2)
    random_number2 = functions.random_number(num1, num2)
    random_math_symbol = functions.get_math_symbol()
    ask = '{} {} {}'.format(random_number1, random_math_symbol, random_number2)
    print('Question: {}'.format(ask))
    result = calculation(random_number1, random_number2, random_math_symbol)

    return result


def calculation(first_number, second_number, math_symbol):

    dic = {'+': add, '-': sub, '*': mul}
    try:
        result = dic[math_symbol](first_number, second_number)

    except KeyError:
        return "Invalid Operator"

    return result
