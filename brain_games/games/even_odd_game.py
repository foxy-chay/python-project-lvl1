from brain_games.games import functions


def start():
    name = functions.greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    functions.response_to_user(name, game)


def game():
    random_number = make_question()
    user_answer = functions.request_answer()
    is_answer_correct, right_answer = check(random_number, user_answer)
    return (right_answer, user_answer, is_answer_correct)


def make_question():
    num1 = 1
    num2 = 99
    random_number = functions.random_number(num1, num2)
    print('Question: {}'.format(random_number))
    return random_number


def check(number, answer):
    if (number % 2 == 0 and answer == 'yes') or \
       (number % 2 == 1 and answer == 'no'):
        print('Correct!')
        right_answer = answer
        return (True, right_answer)
    else:
        if (number % 2 == 0):
            right_answer = 'yes'
        else:
            right_answer = 'no'
        return (False, right_answer)
