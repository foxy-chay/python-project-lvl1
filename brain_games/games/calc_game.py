import prompt
from operator import mul, add, sub
from brain_games.games import functions


def start():
    name = functions.greeting()
    print('What is the result of the expression?')
    functions.response_to_user(name, game)


def game():
    right_answer = make_question()
    user_answer = functions.request_answer()
    is_answer_correct = check_user_answer(right_answer, user_answer)
    return (right_answer, user_answer, is_answer_correct)


def make_question():
    random_number1 = functions.random_number()
    random_number2 = functions.random_number()
    random_math_symbol = functions.get_math_symbol()
    print('Question: {} {} {}'.format(random_number1, random_math_symbol, random_number2))
    result = calculation(random_number1, random_number2, random_math_symbol)
  #  print ('Right answer: {}'.format(result))
    return result


def calculation(first_number, second_number, math_symbol):
    dic = {'+':add, '-':sub, '*':mul}
    try:
        result = dic[math_symbol](first_number, second_number)
    except KeyError:
        return "Invalid Operator"
    return result


def check_user_answer(right_answer, user_answer):
    x = int(right_answer)
    y = int(user_answer)
    if x == y:
        print ('Correct!')
        return True
    return False
