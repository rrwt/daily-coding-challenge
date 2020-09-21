"""
The ancient Egyptians used to express fractions as a sum
of several terms where each numerator is one. For example,
    4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.

Create an algorithm to turn an ordinary fraction a / b,
where a < b, into an Egyptian fraction.
"""
import math
from fractions import Fraction
from typing import List, Union


def egyptian_fractions(fraction: Fraction) -> List[Union[Fraction, int]]:
    """
    Greedy algorithm
    """
    if fraction.numerator == 0:
        return [0]

    if fraction.numerator == 1:
        return [fraction]

    num_ceil = math.ceil(fraction.denominator / fraction.numerator)
    cur_fraction = Fraction(1, num_ceil)
    remaining_fractions = egyptian_fractions(fraction - cur_fraction)

    if remaining_fractions[0] != 0:
        return [cur_fraction] + remaining_fractions

    return [cur_fraction]


if __name__ == "__main__":
    assert egyptian_fractions(Fraction(4, 13)) == [
        Fraction(1, 4),
        Fraction(1, 18),
        Fraction(1, 468),
    ]
