"""
Given an array of elements, return the length of the longest subarray
where all its elements are distinct.

For example,
    given the array [5, 1, 3, 5, 2, 3, 4, 1],
    return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
"""
from typing import List


def length_of_longest_subarray(arr: List[int]) -> int:
    visited = set()

    start = 0
    max_len = 0

    for index, val in enumerate(arr):
        if val not in visited:
            visited.add(val)
        else:
            if max_len < len(visited):
                max_len = len(visited)

            while start < index and arr[start] != val:
                visited.remove(arr[start])
                start += 1

            start += 1

    return max(max_len, len(visited))


if __name__ == "__main__":
    assert length_of_longest_subarray([5, 1, 3, 5, 2, 3, 4, 1]) == 5
