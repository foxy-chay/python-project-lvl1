import random

PROGRESSION_LENGHT_MIN = 5
PROGRESSION_LENGHT_MAX = 10
COMMON_DIF_MIN = 1
COMMON_DIF_MAX = 9
START_NUMBER_MIN = 1
START_NUMBER_MAX = 30
INSTRUCTION = 'What number is missing in the progression?'


def make_progression(progression_length, start_number, common_difference):
    
    progression = [start_number]
    number_of_elements = len(progression)

    for _ in range(number_of_elements, progression_length):
        start_number = start_number + common_difference
        progression.append(start_number)
        number_of_elements += 1

    return progression


def make_question_and_correct_answer():

    progression_length = random.randint(PROGRESSION_LENGHT_MIN,
                                        PROGRESSION_LENGHT_MAX)
    start_number = random.randint(START_NUMBER_MIN,
                                  START_NUMBER_MAX)
    common_difference = random.randint(COMMON_DIF_MIN,
                                       COMMON_DIF_MAX)
    progression = make_progression(progression_length, start_number, common_difference)
    hidden_element = random.randint(0, len(progression) - 1)
    correct_answer = str(progression[hidden_element])
    progression[hidden_element] = '..'
    question = (' '.join(map(str, progression)))

    return question, correct_answer
