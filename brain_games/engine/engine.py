import prompt


def game_logic(game):
    name = greeting()
    print(game.INSTRUCTION)
    
    index = 0
    number_of_rounds = 3

    while index < number_of_rounds:
        question, correct_answer = game.make_question()
        print('Question: {}'.format(question))
        user_answer = request_answer()
        
        if user_answer == correct_answer:
            print('Correct!')
            index += 1
        else:
            game_over(user_answer, correct_answer, name)
   
    print('Congratulations, {}!'. format(name))


def greeting():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    
    return name


def request_answer():
    answer = prompt.string('Your answer: ')
    
    return answer


def game_over(user_answer, correct_answer, name):
    print("'{}' is wrong answer ;(. "\
    "Correct answer was '{}'".format(user_answer, correct_answer))
    print("Let's try again, {}!".format(name))
    
    exit()
