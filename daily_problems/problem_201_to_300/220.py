"""
In front of you is a row of N coins, with values v1, v1, ..., vn.
You are asked to play the following game. You and an opponent take
turns choosing either the first or last coin from the row,
removing it from the row, and receiving the value of the coin.
Write a program that returns the maximum amount of money you can win
with certainty, if you move first, assuming your opponent plays optimally.
"""
from typing import List, Tuple


def _max_amount_rec(row: List[int], size: int, row_sum: int) -> Tuple[int, int]:
    """
    At each turn, you try to maximize current + rest of the pile for you.
    :returns: tuple[value for curr player, value for other player] with given elements
    """
    if size == 1:
        return row_sum, 0
    if size == 2:
        return max(row), min(row)

    first = row[0] + _max_amount_rec(row[1:], size - 1, row_sum - row[0])[1]
    second = row[-1] + _max_amount_rec(row[:-1], size - 1, row_sum - row[-1])[1]
    max_val = max(first, second)
    return max_val, row_sum - max_val


def max_amount_recursive(row: List[int]) -> int:
    row_sum = sum(row)
    size = len(row)

    return _max_amount_rec(row, size, row_sum)[0]


def max_amount_dp(row: List[int]) -> int:
    """
    Max(i, j) = Max(
        row[i] + min(Max(i+2, j), Max(i+1, j-1)),
        row[j] + min(Max(i+1, j-1), Max(i, j-2))
    )
    """
    size = len(row)
    max_amount = [[0] * size for _ in range(size)]

    for index in range(size):
        max_amount[index][index] = row[index]

        if index < size - 1:
            max_amount[index][index + 1] = max(row[index: index + 2])

    for row_size in range(3, size + 1):
        for i in range(0, size - row_size + 1):
            j = i + row_size - 1

            max_amount[i][j] = max(
                row[i] + min(max_amount[i + 1][j - 1], max_amount[i + 2][j]),
                row[j] + min(max_amount[i + 1][j - 1], max_amount[i][j - 2]),
            )

    return max_amount[0][size - 1]


if __name__ == "__main__":
    assert max_amount_recursive([1]) == 1
    assert max_amount_recursive([5, 10]) == 10
    assert max_amount_recursive([10, 15, 20]) == 30
    assert max_amount_recursive([1, 9, 15, 2]) == 16
    assert max_amount_recursive([1, 10, 15, 5]) == 16
    assert max_amount_recursive([5, 3, 7, 10]) == 15
    assert max_amount_recursive([8, 15, 3, 7]) == 22

    assert max_amount_dp([1]) == 1
    assert max_amount_dp([5, 10]) == 10
    assert max_amount_dp([10, 15, 20]) == 30
    assert max_amount_dp([1, 9, 15, 2]) == 16
    assert max_amount_dp([1, 10, 15, 5]) == 16
    assert max_amount_dp([5, 3, 7, 10]) == 15
    assert max_amount_dp([8, 15, 3, 7]) == 22
