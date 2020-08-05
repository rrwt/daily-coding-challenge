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

    max_amount = prices[length - 1] if length <= len(prices) else 0

    for index in range(length):
        max_amount = max(max_amount, prices[index] + cut_naive(length - index - 1, prices))

    return max_amount


def cut_tabulated(prices: List[int]) -> int:
    rod_length: int = len(prices)
    values: List[int] = [0] * (rod_length + 1)

    for cur_length in range(1, rod_length + 1):
        values[cur_length] = prices[cur_length - 1]

        for cut in range(cur_length // 2 + 1):
            values[cur_length] = max(values[cur_length], values[cut] + values[cur_length - cut])

    return values[rod_length]


if __name__ == "__main__":
    assert cut_naive(8, [1, 5, 8, 9, 10, 17, 17, 20]) == 22
    assert cut_naive(8, [3, 5, 8, 9, 10, 17, 17, 20]) == 24

    assert cut_tabulated([1, 5, 8, 9, 10, 17, 17, 20]) == 22
    assert cut_tabulated([3, 5, 8, 9, 10, 17, 17, 20]) == 24
