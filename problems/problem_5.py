"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of
that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Implement car and cdr.
"""


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(func):
    return func.__closure__[0].cell_contents


def cdr(func):
    return func.__closure__[1].cell_contents


def car2(func):
    return func(lambda a, b: a)


def cdr2(func):
    return func(lambda a, b: b)
