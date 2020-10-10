"""
Pascal's triangle is a triangular array of integers constructed with the following formula:
    The first row consists of the number 1.
    For each subsequent row, each element is the sum
    of the numbers directly above it, on either side.

For example, here are the first few rows:
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

Given an input k, return the kth row of Pascal's triangle.
Bonus: Can you do this using only O(k) space?
"""
from typing import List


def pascal_triangle(k: int) -> List[int]:
    if k < 1:
        return []
    if k == 1:
        return [1]

    prev_row = [0] * k
    res = [0] * k
    prev_row[0] = res[0] = 1

    for row in range(2, k + 1):
        for col in range(1, row):
            if col == row - 1:
                res[col] = prev_row[col - 1]
            elif col == 0:
                res[col] = prev_row[0]
            else:
                res[col] = prev_row[col - 1] + prev_row[col]

        prev_row = res[:]

    return res


if __name__ == "__main__":
    assert pascal_triangle(1) == [1]
    assert pascal_triangle(2) == [1, 1]
    assert pascal_triangle(3) == [1, 2, 1]
    assert pascal_triangle(4) == [1, 3, 3, 1]
    assert pascal_triangle(5) == [1, 4, 6, 4, 1]
    assert pascal_triangle(6) == [1, 5, 10, 10, 5, 1]
    assert pascal_triangle(7) == [1, 6, 15, 20, 15, 6, 1]
    assert pascal_triangle(8) == [1, 7, 21, 35, 35, 21, 7, 1]
