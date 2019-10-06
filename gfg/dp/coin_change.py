"""Coin Change
Given a value N, if we want to make change for N cents, and we have
infinite supply of each of S = { S1, S2, .. , Sm} valued coins,
how many ways can we make the change? The order of coins doesn’t matter.
"""
from typing import Sequence, List


def change_coin_naive(amount: int, denominations: Sequence[int], index: int) -> int:
    """
    Time Complexity: Exponential
    """
    if amount == 0:
        return 1

    if amount < 0 or index < 0:
        return 0

    count = 0

    if amount >= denominations[index]:
        count = change_coin_naive(amount - denominations[index], denominations, index)  # take
    count += change_coin_naive(amount, denominations, index - 1)  # leave

    return count


def change_coin_tabulated(amount: int, denominations: Sequence[int]) -> int:
    """
    For amount m, only the coins with value <= m are considered repeatedly
    """
    len_denoms: int = len(denominations)
    matrix: Sequence[List[int]] = [[0] * (len_denoms + 1) for _ in range(amount + 1)]

    for index in range(1, len_denoms + 1):
        # amount = 0 -> 1 solution
        matrix[0][index] = 1

    for a in range(1, amount + 1):
        for b in range(len_denoms):
            if denominations[b] <= a:
                matrix[a][b + 1] = matrix[a - denominations[b]][b + 1]  # include
            matrix[a][b + 1] += matrix[a][b]  # excludee

    return matrix[amount][len_denoms]


if __name__ == "__main__":
    assert change_coin_naive(4, [1, 2, 3], 2) == 4
    assert change_coin_naive(10, [2, 5, 3, 6], 3) == 5

    assert change_coin_tabulated(4, [1, 2, 3]) == 4
    assert change_coin_tabulated(10, [2, 5, 3, 6]) == 5
