"""Cutting a rod
Given a rod of length n inches and an array of prices that contains prices
of all pieces of size smaller than n. Determine the maximum value obtainable
by cutting up the rod and selling the pieces
"""
from typing import List


def cut_naive(length: int, prices: List[int]) -> int:
    if length <= 0:
        return 0
    if length == 1:
        return prices[0]

    if length <= len(prices):
        max_amount = prices[length - 1]
    else:
        max_amount = 0

    for index in range(length):
        max_amount = max(max_amount, prices[index] + cut_naive(length - index - 1, prices))

    return max_amount


def cut_tabulated(prices: List[int]) -> int:
    rod_length: int = len(prices)
    values: List[int] = [0] * (rod_length + 1)

    for cur_length in range(1, rod_length + 1):
        max_val = 0

        for c in range(cur_length):
            max_val = max(max_val, prices[c] + values[cur_length - c - 1])

        values[cur_length] = max_val

    return values[rod_length]


if __name__ == "__main__":
    assert cut_naive(8, [1, 5, 8, 9, 10, 17, 17, 20]) == 22
    assert cut_naive(8, [3, 5, 8, 9, 10, 17, 17, 20]) == 24

    assert cut_tabulated([1, 5, 8, 9, 10, 17, 17, 20]) == 22
    assert cut_tabulated([3, 5, 8, 9, 10, 17, 17, 20]) == 24
