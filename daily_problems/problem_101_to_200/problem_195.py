"""
Let A be an N by M matrix in which every row and every column is sorted.
Given i1, j1, i2, and j2, compute the number of elements of M
smaller than M[i1, j1] and larger than M[i2, j2].

For example, given the following matrix:
    [[ 1,  3,  7, 10, 15, 20],
     [ 2,  6,  9, 14, 22, 25],
     [ 3,  8, 10, 15, 25, 30],
     [10, 11, 12, 23, 30, 35],
     [20, 25, 30, 35, 40, 45]]

And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 14 as there are
15 numbers in the matrix smaller than 6 or greater than 23.
"""
from typing import List


def count_less_than(
    matrix: List[List[int]], height: int, width: int, i: int, j: int
) -> int:
    num = matrix[i][j]
    count = i * j

    end_w = width

    for a in range(i):
        for b in range(j, end_w):
            if matrix[a][b] < num:
                count += 1
            else:
                end_w = b
                break

    end_w = j

    for a in range(i, height):
        for b in range(0, end_w):
            if matrix[a][b] < num:
                count += 1
            else:
                end_w = b
                break

    return count


def count_greater_than(
    matrix: List[List[int]], height: int, width: int, i: int, j: int
) -> int:
    num = matrix[i][j]
    count = (height - 1 - i) * (width - 1 - j)

    w = j

    for a in range(i, -1, -1):
        for b in range(width - 1, w, -1):
            if matrix[a][b] > num:
                count += 1
            else:
                w = b
                break

    w = -1

    for a in range(height - 1, i, -1):
        for b in range(j, w, -1):
            if matrix[a][b] > num:
                count += 1
            else:
                w = b
                break

    return count


def count_elements(matrix: List[List[int]], i1: int, j1: int, i2: int, j2: int) -> int:
    height = len(matrix)
    width = len(matrix[0])

    return count_less_than(matrix, height, width, i1, j1) + count_greater_than(
        matrix, height, width, i2, j2
    )


if __name__ == "__main__":
    elements = [
        [1, 3, 7, 10, 15, 20],
        [2, 6, 9, 14, 22, 25],
        [3, 8, 10, 15, 25, 30],
        [10, 11, 12, 23, 30, 35],
        [20, 25, 30, 35, 40, 45],
    ]
    assert count_elements(elements, 1, 1, 3, 3) == 14
    assert count_elements(elements, 2, 2, 2, 2) == 27
