"""
Implement a function that takes a string of four digits as its argument,
with each digit from 1 ──► 9 (inclusive) with repetitions allowed, and returns
an arithmetic expression that evaluates to the number 24. If no such solution
exists, return "no solution exists."

Rules:
Only the following operators/functions are allowed:
    multiplication, division, addition, subtraction
Division should use floating point or rational arithmetic, etc, to preserve
remainders.
Forming multiple digit numbers from the supplied digits is disallowed.
(So an answer of 12+12 when given 1, 2, 2, and 1 is wrong).
The order of the digits when given does not have to be preserved.
"""
from operator import add, sub, mul
from itertools import product, permutations
import math


def div(n, d):
    return n/d if d else math.inf


operators = [add, sub, mul, div]
op = {sym: ch for sym, ch in zip(operators, '+-*/')}


# O(n! * 27) ~ O(n!)
def game(num_str):
    digits = [int(s) for s in num_str]

    if digits[0] * digits[1] * digits[2] * digits[4] < 24:
        print('no solution')
        return None

    for a, b, c, d in permutations(digits):
        for p, q, r in product(operators, repeat=3):
            if int(r(q(p(a, b), c), d)) == 24:
                print(f'((({a}{op[p]}{b}){op[q]}{c}){op[r]}{d})')


if __name__ == '__main__':
    game('1234')
