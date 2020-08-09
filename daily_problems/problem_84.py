"""
Given a matrix of 1s and 0s, return the number of "islands" in the matrix.
A 1 represents land and 0 represents water, so an island is a group of 1s
that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.
1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
"""
from typing import List


def mark_neighbors(matrix: List[List[int]], h: int, w: int, height: int, width: int) -> None:
    """
    Mark unmarked and island neighbors in all directions.
    """
    if 0 <= w < width and 0 <= h < height:
        matrix[h][w] = -1

        if w > 0 and matrix[h][w-1] == 1:
            mark_neighbors(matrix, h, w-1, height, width)
        if h > 0 and matrix[h-1][w] == 1:
            mark_neighbors(matrix, h-1, w, height, width)
        if w < width - 1 and matrix[h][w+1] == 1:
            mark_neighbors(matrix, h, w+1, height, width)
        if h < height - 1 and matrix[h+1][w] == 1:
            mark_neighbors(matrix, h+1, w, height, width)


def num_islands(matrix: List[List[int]]) -> int:
    islands = 0
    h, height = 0, len(matrix)
    w, width = 0, len(matrix[0])

    while h < height and w < width:
        if matrix[h][w] == 1:
            mark_neighbors(matrix, h, w, height, width)
            islands += 1

        w += 1
        if w == width:
            h += 1
            w = 0

    return islands


if __name__ == "__main__":
    assert num_islands([[1, 0, 0, 0, 0],
                        [0, 0, 1, 1, 0],
                        [0, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0],
                        [1, 1, 0, 0, 1],
                        [1, 1, 0, 0, 1]]) == 4
