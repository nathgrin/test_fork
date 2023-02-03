import numpy as np

# TODO: Rename to Exam


class test_class(list):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_question(self, question):
        self.append(question)

    def __add__(self, *args, **kwargs):  # Overwrite to return the proper class
        return generation_class(super().__add__(*args, **kwargs))

    def serialize(self, key: str) -> str:
        return [entry[key] for entry in self]

    def tex_preamble(self, exc_name, clearpage=False, vfill=False):
        out = "\n%%% NEW\n"
        if clearpage:
            out += r"""\clearpage"""
            out += "\n"
        if vfill:
            out += r"""\vfill"""
            out += "\n"
        out += new_exercise(exc_name)
        out += "\n"
        return out

    def question_order(self, random_order: bool = True):
        if random_order:
            return np.random.permutation(len(self))
        else:
            return range(len(self))


def new_test(*args, **kwargs):
    return test_class(*args, **kwargs)


def new_exercise(exc_name):
    return r"""\newexercise{%s}\setcounter{question}{0}""" % (exc_name)
