import prompt


NUMBER_OF_ROUNDS = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(game.INSTRUCTION)

    for _ in range(NUMBER_OF_ROUNDS):
        question, correct_answer = game.make_question_and_correct_answer()
        print('Question: {}'.format(question))
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. "
                  "Correct answer was '{}'".format(user_answer, correct_answer))
            print("Let's try again, {}!".format(name))

            exit()

    print('Congratulations, {}!'. format(name))
