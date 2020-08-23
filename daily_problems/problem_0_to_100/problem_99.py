"""
Given an unsorted array of integers,
find the length of the longest consecutive elements sequence.

For example,
    given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4].
    Return its length: 4.

Your algorithm should run in O(n) complexity.
"""
from typing import List


def longest_consecutive_subsequence(arr: List[int]) -> int:
    """
    1. Put the array in a set
    2. For each array element i:
        i. check if i-1 exists in set.
        ii. if not, it is the starting point of a new subsequence.
        iii. Count consecutive.
    3. return max

    O(n) & O(n)
    """
    set_arr = set(arr)
    max_count = 0

    for el in arr:
        cur_count = 0

        if el - 1 not in set_arr:
            while el in set_arr:
                cur_count += 1
                el += 1

            max_count = max(max_count, cur_count)

    return max_count


if __name__ == "__main__":
    assert longest_consecutive_subsequence([100, 4, 200, 1, 3, 2]) == 4
