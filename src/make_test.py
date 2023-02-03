import numpy as np

from package_name.question import new_question
from package_name.test import new_test
from package_name.file import file_class


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
