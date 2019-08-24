"""
Given an array in which all numbers except two are repeated once.
(i.e. we have 2n+2 numbers and n numbers are occurring twice and remaining two have occurred once).
Find those two numbers in the most efficient way.
"""
from typing import Tuple


def non_repeating(arr: list) -> Tuple[int, int]:
    xor: int = 0

    for el in arr:
        xor ^= el

    last_set_bit: int = xor & ~(xor - 1)
    x, y = 0, 0

    for el in arr:
        if el & last_set_bit:
            x ^= el
        else:
            y ^= el

    return x, y


if __name__ == "__main__":
    print(non_repeating([2, 4, 7, 9, 2, 4]))
