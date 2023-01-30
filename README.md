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


# ExamStylo
Latex style to reproduce the Dutch central exam format.

## Features / TODO
 - [ ] Seperate ExamStylo from testgeneration a seperate module, include this either as a submodule (during development) or as a LaTeX package (when published to CTAN)