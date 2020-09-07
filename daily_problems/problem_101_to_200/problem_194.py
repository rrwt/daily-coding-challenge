"""
Suppose you are given two lists of n points,
one list p1, p2, ..., pn on the line y = 0
and the other list q1, q2, ..., qn on the line y = 1.
Imagine a set of n line segments connecting each point pi to qi.
Write an algorithm to determine how many pairs of the line segments intersect.
"""
from typing import List


def num_intersections(p: List[int], q: List[int]) -> int:
    size = len(p)
    count = 0

    for i in range(size - 1):
        for j in range(i + 1, size):
            if (p[i] < p[j] and q[i] < q[j]) or (p[i] > p[j] and q[i] > q[j]):
                continue
            count += 1

    return count


if __name__ == "__main__":
    assert num_intersections([1, 4, 5], [4, 2, 3]) == 2
    assert num_intersections([1, 4, 5], [2, 3, 4]) == 0
