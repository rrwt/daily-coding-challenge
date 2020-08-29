"""
You are given an N by M matrix of 0s and 1s. Starting from the top left corner,
how many ways are there to reach the bottom right corner?
You can only move right and down.
0 represents an empty space while 1 represents a wall you cannot walk through.

For example, given the following matrix:
[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]

Return two, as there are only two ways to get to the bottom right:
    Right, down, down, right
    Down, right, down, right
"""
from typing import List


def num_ways(matrix: List[List[int]]) -> int:
    width = len(matrix[0])
    height = len(matrix)

    dp = [[0] * width for _ in range(height)]

    for _ in range(1, width):
        if matrix[0][_] == 1:
            break
        else:
            dp[0][_] = 1

    for _ in range(1, height):
        if matrix[_][0] == 1:
            break
        else:
            dp[_][0] = 1

    for h in range(1, height):
        for w in range(1, width):
            if matrix[h][w] == 0:
                dp[h][w] = dp[h - 1][w] + dp[h][w - 1]

    return dp[height - 1][width - 1]


if __name__ == "__main__":
    assert num_ways([[0, 0, 1], [0, 0, 1], [1, 0, 0]]) == 2
