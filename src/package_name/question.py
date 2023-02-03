import numpy as np

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
