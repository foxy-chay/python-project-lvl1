import random


INSTRUCTION = 'What number is missing in the progression?'


def make_question():

    line_length = random.randint(5, 10)
    first_number = random.randint(1, 30)
    step = random.randint(1, 9)
    hidden_element = random.randint(0, line_length - 1)
    numbers_list = [first_number]
    number_of_elements = len(numbers_list)

    while number_of_elements < line_length:
        first_number = first_number + step
        numbers_list.append(first_number)
        number_of_elements += 1

    correct_answer = str(numbers_list[hidden_element])
    numbers_list[hidden_element] = '..'
    question = (' '.join(map(str, numbers_list)))


    return (question, correct_answer)
