"""
You are given an array of arrays of integers,
where each array corresponds to a row in a triangle of numbers.
For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:
      1
     2 3
    1 5 1

We define a path in the triangle to start at the top and go down one row at a time
to an adjacent value, eventually ending with an entry on the bottom row.
For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.
Write a program that returns the weight of the maximum weight path.
"""
from typing import List


def max_prev_row(row: List[int], h: int, w: int) -> int:
    if w == 0:
        return row[0]
    if w == h + 1:
        return row[w - 1]

    return max(row[w - 1], row[w])


def max_weight_path(rows: List[List[int]]) -> int:
    height = len(rows)

    for h in range(1, height):
        for w, _ in enumerate(rows[h]):
            rows[h][w] += max_prev_row(rows[h - 1], h - 1, w)

    return max(rows[-1])


if __name__ == "__main__":
    triangle = [[1], [2, 3], [1, 5, 1]]
    assert max_weight_path(triangle) == 9
