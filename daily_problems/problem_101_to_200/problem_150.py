"""
Given a list of points, a central point, and an integer k,
find the nearest k points from the central point.

For example,
    given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2,
    return [(0, 0), (3, 1)].
"""
from math import sqrt
from typing import List, Tuple


def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    """
    Calculate Euclidean distance
    """
    return round(sqrt(pow(y2 - y1, 2) + pow(x2 - x1, 2)), 2)


def k_nearest(
    coordinates: List[Tuple[int, int]], x: int, y: int, k: int
) -> List[Tuple[int, int]]:
    """
    Time Complexity: O(n*log(n))
    Space Complexity: O(n)
    """
    size = len(coordinates)
    dist = [0] * size

    for index, (x2, y2) in enumerate(coordinates):
        dist[index] = distance(x, y, x2, y2)

    return [c for (d, c) in sorted(zip(dist, coordinates), key=lambda _: _[0])][:k]


if __name__ == "__main__":
    assert k_nearest([(0, 0), (5, 4), (3, 1)], 1, 2, 2) == [(0, 0), (3, 1)]
