"""
You are given a 2-d matrix where each cell represents number of coins in that cell.
Assuming we start at matrix[0][0], and can only move right or down,
find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix
    0 3 1 1
    2 0 0 4
    1 5 3 1

The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
"""
from typing import List


def max_sum(matrix: List[List[int]]) -> int:
    """
    Dynamic programming
    Time Complexity: O(n*n)
    Space Complexity: O(1)
    """
    height = len(matrix)
    width = len(matrix[0])

    for row in range(1, height):
        matrix[row][0] += matrix[row - 1][0]

    for col in range(1, width):
        matrix[0][col] += matrix[0][col - 1]

    for row in range(1, height):
        for col in range(1, width):
            matrix[row][col] += max(matrix[row - 1][col], matrix[row][col - 1])

    return matrix[-1][-1]


if __name__ == "__main__":
    assert max_sum([[0, 3, 1, 1], [2, 0, 0, 4], [1, 5, 3, 1]]) == 12
