"""
Given a sorted array of n distinct integers where each integer is in the range
from 0 to m-1 and m > n. Find the smallest number that is missing from the array.
"""


def smallest_missing(arr: list) -> int:
    """
    A modified version of binary search can be applied.
    If the number mid index == value, then the missing value
    is on the right, else on the left side.
    Time Complexity: O(log(n))
    """
    beg, end = 0, len(arr) - 1

    while beg <= end:
        if arr[beg] != beg:
            return beg

        m = (beg + end) >> 1

        if arr[m] == m:
            beg = m + 1
        else:
            end = m - 1

    return end + 1


if __name__ == "__main__":
    print(smallest_missing([]))
    print(smallest_missing([0]))
    print(smallest_missing([0, 1, 2, 3, 4, 5, 6, 7, 9, 10]))
    print(smallest_missing([0, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(smallest_missing([0, 1, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(smallest_missing([0, 1, 2, 3, 5, 6, 7, 8, 9, 10]))
