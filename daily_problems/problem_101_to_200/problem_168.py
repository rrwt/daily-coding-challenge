"""
Given an N by N matrix, rotate it by 90 degrees clockwise.
For example, given the following matrix:
    [[1, 2, 3],                           [[7, 4, 1],
     [4, 5, 6],     you should return      [8, 5, 2],
     [7, 8, 9]]                            [9, 6, 3]]

Follow-up: What if you couldn't use any extra space?
"""
from typing import List


def rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Time Complexity: O(width * height)
    Space Complexity: O(1)
    """
    height = width = len(matrix) - 1
    i = j = 0

    while i < height:
        for k in range(width - j):
            val = matrix[i][j + k]
            matrix[i][j + k] = matrix[height - k][j]
            matrix[height - k][j] = matrix[height][width - k]
            matrix[height][width - k] = matrix[i + k][width]
            matrix[i + k][width] = val

        i += 1
        j += 1
        height -= 1
        width -= 1

    return matrix


if __name__ == "__main__":
    mat = [[1, 2], [4, 5]]
    print(mat)
    print(rotate_matrix(mat))
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(mat)
    print(rotate_matrix(mat))
    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(mat)
    print(rotate_matrix(mat))
