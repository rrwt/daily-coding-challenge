"""
Given N point on a 2D plane as pair of (x, y) co-ordinates,
find maximum number of point which lie on the same line.
"""
from collections import defaultdict
from typing import List, Tuple


def greatest_common_divisor(a: int, b: int) -> int:
    if b == 0:
        return a

    return greatest_common_divisor(b, a % b)


def max_points(points: List[Tuple[int]]) -> int:
    length: int = len(points)

    if length < 3:
        return length

    max_count: int = 1

    for i in range(length - 1):
        hash_table: dict = defaultdict(int)

        for j in range(i + 1, length):
            x_diff = points[j][0] - points[i][0]
            y_diff = points[j][1] - points[i][1]
            gcd = greatest_common_divisor(x_diff, y_diff)
            x_diff //= gcd
            y_diff //= gcd

            hash_table[(x_diff, y_diff)] += 1
            max_count = max(hash_table[(x_diff, y_diff)], max_count)

    return max(max_count + 1, 2)


if __name__ == "__main__":
    points = [(-1, 1), (0, 0), (1, 1), (2, 2), (3, 3), (3, 4)]
    assert max_points(points) == 4
    points = [(0, 2), (2, 4), (2, 0), (4, 2), (6, 4)]
    assert max_points(points) == 2
