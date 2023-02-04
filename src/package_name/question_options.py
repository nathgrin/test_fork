from abc import abstractmethod, ABC
from typing import Iterator

import numpy as np


class QuestionOptions(ABC):

    def __init__(self, text, options=None, params=None, seed=None, **kwargs):
        # Save initial values
        # TODO: Set self.text to the correct replacement token if an empty string is passed
        self.text = text
        self.value = None  # Not required, use history[-1]
        self.value_history = []
        # self.options = options
        # self.params = params

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> str:
        self.update()
        return self.render_latex()

    @abstractmethod
    def update(self) -> None:
        """Generate a new value and append it to the value_history
        If necessary check for uniqueness
        """
        pass

    @abstractmethod
    def render_latex(self) -> str:
        pass

    def reset(self) -> None:
        """Clear the value history
        """
        self.value_history = []
        self.update()

    # def __repr__(self) -> str:
    #     return f"""{{
    #         'type': {type(self)},
    #         'text': {self.text}
    #         }}"""


class NumericalQuestionOption(QuestionOptions):
    def __init__(self, text: str, lower_bound: float, upper_bound: float, **kwargs):
        super().__init__(text, **kwargs)
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def update(self) -> None:
        self.value = np.random.randint(self.lower_bound, self.upper_bound)

    def render_latex(self) -> str:
        return self.text % self.value


class ChoiceQuestionOption(QuestionOptions):
    def __init__(self, text: str, options: list, **kwargs):
        super().__init__(text, **kwargs)
        self.options = options

    def update(self) -> None:
        self.value = np.random.choice(self.options)

    def render_latex(self) -> str:
        return self.text % self.value


class LabelQuestionOption(QuestionOptions):
    def __init__(self, text: str, **kwargs):
        super().__init__(text, **kwargs)

    def render_latex(self) -> str:
        return self.text


def checktypes(conditions_list) -> bool:
    """Check a list of variable types

    Args:
        conditions_list (_type_): List of variable, type-lists/tuples(?)

    Returns:
        bool: True is all type conditions are met, otherwise False
    """
    for condition in conditions_list:
        if not isinstance(condition[0], condition[1]):
            return False
    return True


def create_question_options(*args, **kwargs) -> QuestionOptions:
    # NumericalQuestionOption
    try:
        if checktypes([[args[0], str],
                       [args[1], float],
                       [args[2], float]]):
            print('  qo=num')
            return NumericalQuestionOption(args[0], args[1], args[2], **kwargs)
    except IndexError:
        # print('Not a NumericalQuestionOption')
        pass
    except Exception as e:
        print(e)

    # ChoiceQuestionOption
    try:
        if checktypes([[args[0], str],
                       [args[1], list]]):
            return ChoiceQuestionOption(args[0], args[1], **kwargs)
    except IndexError:
        # print('Not a NumericalQuestionOption')
        pass
    except Exception as e:
        print(e)

    # LabelQuestionOption
    try:
        if checktypes([[args[0], str]]):
            return LabelQuestionOption(args[0], **kwargs)
    except IndexError:
        raise TypeError(
            f'create_question_options expected at least 1 argument, got {len(args)}')
    # except Exception as e:
    #     print(e)
