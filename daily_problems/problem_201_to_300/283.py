"""
A regular number in mathematics is defined as one which evenly
divides some power of 60. Equivalently, we can say that a regular
number is one whose only prime divisors are 2, 3, and 5.
These numbers have had many applications, from helping ancient Babylonians
keep time to tuning instruments according to the diatonic scale.
Given an integer N, write a program that returns,
in order, the first N regular numbers.
"""
import sys
from typing import List


def regular_numbers(n: int) -> List[int]:
    if n < 1:
        return [0]

    powers = [2, 3, 5]
    numbers = [0] * n
    numbers[0] = 60

    for i in range(1, n):
        last_num = numbers[i - 1]
        next_num = sys.maxsize

        for j in range(i):
            for k in range(3):
                if next_num > numbers[j] * powers[k] > last_num:
                    next_num = numbers[j] * powers[k]

        numbers[i] = next_num

    return numbers


if __name__ == "__main__":
    assert regular_numbers(0) == [0]
    assert regular_numbers(1) == [60]
    assert regular_numbers(2) == [60, 120]
    assert regular_numbers(5) == [60, 120, 180, 240, 300]
