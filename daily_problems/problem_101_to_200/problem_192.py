"""
You are given an array of non-negative integers.
Let's say you start at the beginning of the array and are trying to advance to the end.
You can advance at most, the number of steps that you're currently on.
Determine whether you can get to the end of the array.

For example,
    given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1 -> 3 -> 5, so return true.
    given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.
"""
from typing import List


def can_reach_end(arr: List[int]) -> bool:
    if arr[0] == 0:
        return False

    length = len(arr)
    max_reach = 0
    index = 0

    while index <= max_reach:
        max_reach = max(max_reach, arr[index] + index)

        if max_reach >= length - 1:
            return True

        index += 1

    return False


if __name__ == "__main__":
    assert can_reach_end([1, 3, 1, 2, 0, 1]) is True
    assert can_reach_end([1, 2, 1, 0, 0]) is False
