import json
from typing import Iterator

from package_name.question_options import create_question_options


class Question:

    preamble = r"\question "
    postamble = r""

    part_preamble = r"  \part "
    part_postamble = '\n'
    parts_preamble = '\n' + r"\begin{parts}" + '\n'
    parts_postamble = r"\end{parts}" + '\n'

    def __init__(self, is_part=False):
        # self.options = []  # list of QuestionOptions
        # self.parts = []   # list of QuestionText
        self.tokens = []  # full list of all...

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> str:
        return self.render_latex()

    def add_token(self, token):
        self.tokens.append(token)

    def add_option(self, option):
        self.tokens.append(create_question_options(*option))

    def add_parts(self, parts):
        self.add_token(self.parts_preamble)
        for part in parts:
            q = create_question(part, is_part=True)
            self.add_token(q)
        self.add_token(self.parts_postamble)

    # WIP
    # def serialize(self):
    #     return json.dumps(self)

    def render_latex(self):
        return ''.join(
            [self.preamble] +
            [token if type(token) is str else next(token) for token in self.tokens] +
            [self.postamble])


# WIP
def create_question(content_list: list, is_part=False) -> Question:
    question = Question()
    if is_part:
        question.preamble = Question.part_preamble
        question.postamble = Question.part_postamble

    for element in content_list:
        # if the type is text -> append token
        if type(element) is str:
            question.add_token(element)

        # if type is list:
        if (type(element) is list) and (len(element) > 0):
            # if first element is text -> append questionoptions with the list
            if type(element[0]) is str:
                question.add_option(element)

            if type(element[0]) is list:
                question.add_parts(element[0])
            #   if first element is a list -> append a question part
            #   if first element is neither -> Exception
            # if type is QuestionOptions-> append
        pass
    return question
