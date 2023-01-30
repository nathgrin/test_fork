import numpy as np


def new_exercise(exc_name):

    return r"""\newexercise{%s}\setcounter{question}{0}""" % (exc_name)


class file_class():
    fname = ""

    def __init__(self, fname):
        self.fname = fname

    def clearfile(self):
        open(self.fname, 'w').close()

    def write_appline(self, writeline):
        with open(self.fname, 'a') as thefile:
            thefile.write(writeline)


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


class question_class(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self['text'] = kwargs.get('text', "")
        self['options'] = kwargs.get('options', [])
        self['n'] = (len(o) for o in self['options'])  # doesnt work

    def set_options(self, options):
        self['options'] = options
        self['n'] = (len(o) for o in self['options'])  # doesnt work

    def generate_text(self):

        inds = [np.random.randint(len(opt)) for opt in self['options']]
        print(self['text'])
        thingies = [self['options'][i][ind] for i, ind in enumerate(inds)]
        print(thingies)
        out = self['text'].format(*thingies)
        # print(">",out)
        return out


def new_question(*args, **kwargs):
    return question_class(*args, **kwargs)


def main():
    print('hi')

    """
    Use double {{curlies}} for tex when combining latex with string.format()
    remember the rawstring! 
    
    
    """

    fname = "question_file.tex"
    n_tests = 24

    test = new_test()

    # Questions
    # >< #
    q = new_question()
    q['text'] = r"""Bereken de concentratie van een oplossing van {0} {1} in {2} water"""
    q.set_options([[r"$%.1f\,\mrm{g}$" % (np.random.uniform(0.8, 5)) for i in range(5)],
                   [r"\ch{Cl}", r"\ch{NO2}", r"\ch{SO4}", r"\ch{CO2}"],
                   [r"$%.1f\,\mrm{mL}$" % (np.random.uniform(0.8, 5))
                    for i in range(5)],
                   ])

    test.add_question(q)

    # >< #
    q = new_question()
    q['text'] = r"""Bereken de massa {1} in een oplossing van {2} met een concentratie {0}"""
    q.set_options([[r"$%.1f\,\mrm{%smol L^{\sm1}}$" % (np.random.uniform(0.8, 5), np.random.choice(['', 'k', 'm', r'\micro'])) for i in range(5)],
                   [r"\ch{Cl}", r"\ch{NO2}", r"\ch{SO4}", r"\ch{CO2}"],
                   [r"$%.1f\,\mrm{%sL}$" % (np.random.uniform(0.8, 5), np.random.choice(
                       ['', 'k', 'm', r'\mu '])) for i in range(5)],
                   ])

    test.add_question(q)

    # >< #
    q = new_question()
    q['text'] = r"""Bereken het aantal $\mrm{{mmol}}$ {1} in een berg van {0}"""
    q.set_options([[r"$%.1f\,\mrm{%sg}$" % (np.random.uniform(0.8, 5), np.random.choice(['', 'k', 'm', r'\mu '])) for i in range(5)] + [],
                   [r"\ch{Cl}", r"\ch{NO2}", r"\ch{SO4}", r"\ch{CO2}"],
                   ])

    test.add_question(q)

    thefile = file_class(fname)
    thefile.clearfile()

    toggle = False

    for i in range(n_tests):
        print(" > Test", i)
        exc_name = r"""SO Chemisch rekenen \hfill 1337H4X0r"""
        out = test.tex_preamble(
            exc_name, clearpage=toggle, vfill=not toggle)  # is not rly a preamble

        order = test.question_order(random_order=True)
        print(i, order)
        for ind in order:
            q = test[ind]
            out += "\n"
            out += r"""\newquestion[2]{"""
            out += q.generate_text()
            out += r"""}"""
            out += "\n"

        print(out)

        thefile.write_appline(out)
        toggle = not toggle

    # \usepackage{chemformula}


if __name__ == "__main__":
    main()
