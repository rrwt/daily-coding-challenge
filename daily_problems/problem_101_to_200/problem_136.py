"""
Given an N by M matrix consisting only of 1's and 0's,
find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:
    [[1, 0, 0, 0],
     [1, 0, 1, 1],
     [1, 0, 1, 1],
     [0, 1, 0, 0]]
Return 4.
"""
from typing import List


def get_rectangular_area(
    matrix: List[List[int]], h: int, w: int, n: int, m: int
) -> int:
    cur_x = m - w
    max_area = 0
    cur_y = 0

    for i in range(h, n):
        cur_y += 1

        for j in range(w, w + cur_x):
            if matrix[i][j] == 0:
                cur_x = min(cur_x, j - w)
                break

        if cur_x == 0:
            break

        max_area = max(cur_x * cur_y, max_area)

    return max_area


def largest_rectangle(matrix: List[List[int]], n: int, m: int) -> int:
    max_area = 0

    for h in range(n):
        for w in range(m):
            if max_area > (n - h) * (m - w):
                break
            if matrix[h][w] == 1:
                max_area = max(max_area, get_rectangular_area(matrix, h, w, n, m))

    return max_area


if __name__ == "__main__":
    arr = [[1, 0, 0, 0], [1, 0, 1, 1], [1, 0, 1, 1], [0, 1, 0, 0]]
    assert largest_rectangle(arr, 4, 4) == 4
