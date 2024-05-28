#!python3
# func.py - A function within a function that also takes a function
#           as an argument.


def apply(func: object, value: object) -> object:
    return func(value)