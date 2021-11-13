import random


INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question():

    num_min = 1
    num_max = 99
    question = random.randint(num_min, num_max)
    correct_answer = check(question)
    
    return (question, correct_answer)


def check(number):

    if number % 2 == 0:
        return 'yes'
    
    else:
        return 'no'
