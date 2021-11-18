import random


INSTRUCTION = 'What number is missing in the progression?'


def make_progression():
    progression_length = random.randint(5, 10)
    start_number = random.randint(1, 30)
    common_difference = random.randint(1, 9)
    progression = [start_number]
    number_of_elements = len(progression)

    while number_of_elements < progression_length:
        start_number = start_number + common_difference
        progression.append(start_number)
        number_of_elements += 1

    return progression


def make_question_and_correct_answer():
    progression = make_progression()
    hidden_element = random.randint(0, len(progression) - 1)
    correct_answer = str(progression[hidden_element])
    progression[hidden_element] = '..'
    question = (' '.join(map(str, progression)))

    return question, correct_answer
