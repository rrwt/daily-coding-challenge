"""Cutting a rod
Given a rod of length n inches and an array of prices that contains prices
of all pieces of size smaller than n. Determine the maximum value obtainable
by cutting up the rod and selling the pieces
"""
from typing import List


def cut_naive(length: int, prices: list) -> int:
    if length <= 0:
        return 0
    if length == 1:
        return prices[0]

    if length <= len(prices):
        max_amount = prices[length - 1]

    for index in range(length):
        max_amount = max(max_amount, prices[index] + cut_naive(length - index - 1, prices))

    return max_amount


def cut_tabulated(prices: list) -> int:
    length: int = len(prices)
    values: List[int] = [0] * (length + 1)

    for l in range(1, length + 1):
        max_val = 0

        for c in range(l):
            max_val = max(max_val, prices[c] + values[l - c - 1])

        values[l] = max_val

    return values[length]


if __name__ == "__main__":
    assert cut_naive(8, [1, 5, 8, 9, 10, 17, 17, 20]) == 22
    assert cut_naive(8, [3, 5, 8, 9, 10, 17, 17, 20]) == 24

    assert cut_tabulated([1, 5, 8, 9, 10, 17, 17, 20]) == 22
    assert cut_tabulated([3, 5, 8, 9, 10, 17, 17, 20]) == 24
