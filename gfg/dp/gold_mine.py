"""
Given a gold mine of n*m dimensions. Each field in this mine contains a positive integer
which is the amount of gold in tons. Initially the miner is at first column but can be at any row.
He can move only right, right-up, right-down that is from a given cell,
the miner can move to the cell diagonally up towards the right, or right, or diagonally down
towards the right. Find out maximum amount of gold he can collect.
"""
from typing import List


def gold_dp(mine: List[List[int]]) -> int:
    """
    O(width * height) & O(1)
    """
    height = len(mine)
    width = len(mine[0])

    for column in range(1, width):
        for row in range(height):
            val = mine[row][column-1]

            if row > 0:
                val = max(mine[row-1][column-1], val)
            if row < height-1:
                val = max(mine[row+1][column-1], val)

            mine[row][column] += val

    max_val = mine[0][width-1]

    for row in range(1, height):
        max_val = max(max_val, mine[row][width-1])

    return max_val


if __name__ == "__main__":
    assert gold_dp([[1, 3, 3], [2, 1, 4], [0, 6, 4]]) == 12
    assert gold_dp([[1, 3, 1, 5], [2, 2, 4, 1], [5, 0, 2, 3], [0, 6, 1, 2]]) == 16
