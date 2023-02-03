# TestGeneration
Python to LaTeX test generator.

## Features / TODO
 - [ ] Think of a better name ;-)
 - [ ] Split LaTeX and python
 - [ ] CLI-options (use as module)
   - [ ] set output directory (default= ./build/{date_time})
   - [ ] set number of test versions (default= 10)
   - [ ] set input files (serialized question files)
 - [ ] Split package into modules to be imported
   - [ ] question.py
   - [ ] test.py
 - [ ] Question (class)
   - [ ] Serialization (use json for compatibility)
   - [ ] Rework to an skeleton / options / variables system; the value of the variable determines the options filled in in the skeleton 
   - [ ] Answer generation
 - [ ] Test (class)
   - [ ] Serialization (use json for compatibility)

## Overview

 - `Exam()`: Collection of `Question`-s 
   - contains:
     - `preamble: str`
     - `questions: [Question]`
   - Keeps track of counters
   - implements:
     - `add_question(q: Question)`
     - `serialize() -> JSON`
     - `render_latex() -> TexString`
   
   - `Question(dict)`: 
     - contains:
       - `options: [QuestionOption]`
       - `parts: [str]`
       - `tokens: []`:  list of all things, used for rendering
       - TODO: `parts: [Question or str]` (ugly...)
     - implements:
       - `add_option()`
       - `add_part()`
       - `serialize() -> JSON`
       - `render_latex() -> TexString`
  
    - `QuestionOptions()`
      - `__init__(text, params, seed=None)`
      - `text`: f-string
      - `params`:
        - `{ lower_bound: float, upper_bound: float }` `->` `NUMERICAL`
        - `{ options: [str] }` `->` `CHOICE`
        - `{ options: [[str]] }` `->` `SINGLE_CHOICE`
      - `seed`
      - contains:
        - `type`:
          - `CHOICE`
          - `NUMERICAL`
            - requires a lower_bound and an upper_bound
          - `SINGLE_CHOICE`
      - implements:
        - `__iter__()`: returns this object
        - `__next__()`: returns next formatted string including value
        - `set_seed()`: Provide a seed value for the randomness
        - `get_value()`: returns the unformatted value of the current choice/numerical value
        - `get_numerical()`: get a next numerical value (based on seed)
        - `get_choice()`: get next choice (based on seed)



# ExamStylo
Latex style to reproduce the Dutch central exam format.

## Features / TODO
 - [ ] Seperate ExamStylo from testgeneration a seperate module, include this either as a submodule (during development) or as a LaTeX package (when published to CTAN)