"""
Given a collection of intervals, find the minimum number of intervals
you need to remove to make the rest of the intervals non-overlapping.
Intervals can "touch", such as [0, 1] and [1, 2],
but they won't be considered overlapping.
For example,
    given the intervals (7, 9), (2, 4), (5, 8), return 1
    as the last interval can be removed and the first two won't overlap.

The intervals are not necessarily sorted in any order.
"""
from typing import List, Tuple


def min_intervals_to_remove(intervals: List[Tuple[int, int]]) -> int:
    intervals.sort(key=lambda x: x[1])  # sort by increasing end time
    stack = []
    count = 0

    for interval in intervals:
        if not stack or stack[-1][1] <= interval[0]:
            stack.append(interval)
        else:
            count += 1

    return count


if __name__ == "__main__":
    assert min_intervals_to_remove([(7, 9), (2, 4), (5, 8)]) == 1
    assert min_intervals_to_remove([(0, 1), (1, 2)]) == 0
    assert min_intervals_to_remove([(7, 9), (2, 4), (5, 8), (1, 3)]) == 2
