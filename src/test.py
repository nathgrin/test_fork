# Make available via __init__
from package_name.question import Question
from package_name.question import create_question
from package_name.question_options import QuestionOptions
from package_name.question_options import create_question_options


def question_tests():
    # Tests for Question class:
    q = Question()
    q.tokens.append('')

    # deprecated: REMOVE
    # q.tokens.append(QuestionOptions('This is just text.'))
    # q.tokens.append(QuestionOptions('The next should be a random value.'))
    # qo = QuestionOptions(r'%f')
    # qo.type = 'NUMERICAL'
    # q.tokens.append(qo)
    # q.tokens.append(QuestionOptions('Something else'))

    print(q.render_latex())
    print(q.render_latex())
    print(q.render_latex())
    print(q.render_latex())


def create_question_options_tests():
    # Tests for create_question_options() -> QuestionOptions:

    # returns LabelQuestionOptions
    q = create_question_options('This is text')
    print(type(q))

    # returns NumericalQuestionOptions
    q = create_question_options('This is text', 0.0, 1.0)
    print(type(q))

    # returns ChoiceQuestionOptions
    q = create_question_options('This is text', ['opt1', 'opt2'])
    print(type(q))

    # raises IndexError -> TypeError
    q = create_question_options()
    print(type(q))


def create_question_tests():
    # Creates a two-label question
    q = create_question(['token 1', 'token 2'])
    print(q.render_latex())

    # Creates a label-num question
    q = create_question(['token 1',
                         ['%i', 0.0, 10.0]])
    # Returns a label, random float-token
    print(q.render_latex())
    print(q.render_latex())
    print(q.render_latex())

    # Creates a label-choice question
    q = create_question(['token 1',
                         ['%s', ['a', 'b', 'c'] ]])
    # Returns a label, random choice-token
    print(q.render_latex())
    print(q.render_latex())
    print(q.render_latex())

    # Creates a subquestion question
    q = create_question(['token 1',
                         [['part 1', 'part 2', 'part 3'] ]])
    # Returns a label, random choice-token
    print(q.render_latex())

if __name__ == '__main__':
    # question_tests()
    # create_question_options_tests()
    create_question_tests()
