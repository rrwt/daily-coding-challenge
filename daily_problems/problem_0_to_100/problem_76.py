"""
You are given an N by M 2D matrix of lowercase letters.
Determine the minimum number of columns that can be removed to ensure
that each row is ordered from top to bottom lexicographically.
That is, the letter at each column is lexicographically later as you go down each row.
It does not matter whether each row itself is ordered lexicographically.

For example, given the following table:
    cba
    daf
    ghi

  This is not ordered because of the a in the center.
  We can remove the second column to make it ordered:
    ca
    df
    gi
"""
from typing import List


def make_lexicographic(matrix: List[List[str]]) -> int:
    height = len(matrix)
    width = len(matrix[0])
    count_removal = 0

    for w in range(width):
        for h in range(1, height):
            if matrix[h][w] < matrix[h - 1][w]:
                count_removal += 1
                break

    return count_removal


if __name__ == "__main__":
    assert make_lexicographic([["c", "b", "a"], ["d", "a", "f"], ["g", "h", "i"]]) == 1
    assert make_lexicographic([["a", "b", "c", "d", "e", "f"]]) == 0
    assert make_lexicographic([["z", "y", "x"], ["w", "v", "u"], ["t", "s", "r"]]) == 3
