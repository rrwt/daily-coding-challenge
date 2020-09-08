"""
Let X be a set of n intervals on the real line. We say that a set of points P
"stabs" X if every interval in X contains at least one point in P.
Compute the smallest set of points that stabs X.

For example,
    given the intervals [(1, 4), (4, 5), (7, 9), (9, 12)], you should return [4, 9].
"""
from collections import defaultdict
from typing import List, Tuple, Set


def stabbing_points(intervals: List[Tuple]) -> Set[int]:
    """
    Time Complexity: O(n*log(n))
    Space Complexity: O(n)
    """
    count = defaultdict(int)

    for x, y in intervals:
        count[x] += 1

        if x != y:
            count[y] += 1

    sorted_count = sorted(count.items(), key=lambda _: _[1], reverse=True)
    stabbers = set()
    count_el = 0
    length = len(intervals)
    processed = set()

    for element, _ in sorted_count:
        stabbers.add(element)

        for x, y in intervals:
            if (x, y) not in processed and (x == element or y == element):
                count_el += 1
                processed.add((x, y))

        if count_el >= length:
            break

    return stabbers


if __name__ == "__main__":
    assert stabbing_points([(1, 4), (4, 5), (7, 9), (9, 12)]) == {4, 9}
