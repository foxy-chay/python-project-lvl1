from brain_games.games import functions


def start():

    name = functions.greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    functions.response_to_user(name, game)


def game():

    right_answer = make_question()
    user_answer = functions.request_answer()
    is_answer_correct = functions.check_user_answer(right_answer, user_answer)

    return (right_answer, user_answer, is_answer_correct)


def make_question():

    num1 = 1
    num2 = 99
    random_number = functions.random_number(num1, num2)
    print('Question: {}'.format(random_number))
    is_number_Prime = isPrime(random_number)
    right_answer = get_right_answer(is_number_Prime)

    return right_answer


def isPrime(number):

    if number % 2 == 0:
        return number == 2

    d = 3
    while d * d <= number and number % d != 0:
        d += 2
    return d * d > number


def get_right_answer(is_number_prime):

    if is_number_prime:
        return 'yes'
    else:
        return 'no'
