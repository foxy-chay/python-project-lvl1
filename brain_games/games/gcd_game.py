from brain_games.games import functions


def start():
    name = functions.greeting()
    print('Find the greatest common divisor of given numbers.')
    functions.response_to_user(name, game)


def game():
    right_answer = make_question()
    user_answer = functions.request_answer()
    is_answer_correct = functions.check_user_answer(right_answer, user_answer)
    return (right_answer, user_answer, is_answer_correct)


def calculation(first_number, second_number):
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number
    result = first_number + second_number
    return result


def make_question():
    num1 = 1
    num2 = 99
    random_number1 = functions.random_number(num1, num2)
    random_number2 = functions.random_number(num1, num2)
    question = '{} {}'.format(random_number1, random_number2)
    print('Question: {}'.format(question))
    result = calculation(random_number1, random_number2)
    return result
