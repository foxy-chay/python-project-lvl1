from brain_games.games import functions


def start():
    name = functions.greeting()
    print('What number is missing in the progression?')
    functions.response_to_user(name, game)


def game():

    right_answer = make_question()
    user_answer = functions.request_answer()
    is_answer_correct = functions.check_user_answer(right_answer, user_answer)

    return (right_answer, user_answer, is_answer_correct)


def make_question():

    line_length = functions.random_number(5, 10)
    first_number = functions.random_number(1, 30)
    step = functions.random_number(1, 9)
    hidden_element = functions.random_number(0, line_length - 1)
    numbers_list = [first_number]
    number_of_elements = len(numbers_list)

    while number_of_elements < line_length:
        first_number = first_number + step
        numbers_list.append(first_number)
        number_of_elements += 1

    right_answer = numbers_list[hidden_element]
    numbers_list[hidden_element] = '..'
    subsequence = (' '.join(map(str, numbers_list)))

    print('Question: {}'.format(subsequence))

    return right_answer
