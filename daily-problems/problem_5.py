"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of
that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
https://en.wikipedia.org/wiki/CAR_and_CDR
Implement car and cdr.
"""


def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


def car(func):
    """Extract the first pointer of cons

    >>> car(cons(1, 2))
    1
    >>> car(cons(5, 3))
    5

    Args:
        func (functon): Function returned by higher order function cons

    Returns:
        int: value of first array element.
    """
    return func.__closure__[0].cell_contents


def cdr(func):
    """Extrac the second pointer of cons

    >>> cdr(cons(1, 2))
    2
    >>> cdr(cons(5, 3))
    3

    Args:
        func (function): Function returned by cons

    Returns:
        int: value of second array element.
    """
    return func.__closure__[1].cell_contents


def car2(func):
    return func(lambda a, b: a)


def cdr2(func):
    return func(lambda a, b: b)
