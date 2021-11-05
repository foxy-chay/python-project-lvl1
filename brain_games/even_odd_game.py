import prompt
import random


def greeting():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game(name)


def game(name):
    i = 0
    while i < 3:
        a = random_number()
        is_answer_correct = answer_check(a)
        if is_answer_correct:
            i += 1
        else:
            print("It is wrong answer ;(")
            print("Let's try again, {}!".format(name))
            break
        print('Congratulations, {}!'.format(name))


def random_number():
    i = random.randint(1, 99)
    return i


def answer_check(number):
    i = number
    print('Question: {}'.format(number))
    answer = prompt.string('Your answer: ')
    if (i % 2 == 0 and answer == 'yes') or (i % 2 == 1 and answer == 'no'):
        print('Correct!')
        return True
    return False
