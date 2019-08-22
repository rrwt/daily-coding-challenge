"""
Given an unsorted array arr[0..n-1] of size n, find the minimum length subarray arr[s..e]
such that sorting this subarray makes the whole array sorted.
"""
from typing import Tuple


def unsorted_array(arr: list) -> Tuple[list, int, Tuple[int, int]]:
    """
    Time Complexity: O(n)
    """
    start, end = 0, len(arr) - 1

    while start < end and arr[start] < arr[start + 1]:
        start += 1

    while start < end and arr[end] > arr[end - 1]:
        end -= 1

    for el in arr[start : end + 1]:
        # another way of implementing this part would be to find the min and
        # max of the subarray and keep on decrementing start/incrementing end
        while el < arr[start]:
            start -= 1
        while el > arr[end]:
            end += 1

    if start + 1 < end - 1:
        return arr[start + 1 : end], end - start - 1, (start + 1, end - 1)
    return [], 0, (-1, -1)


if __name__ == "__main__":
    arr_list: list = [
        [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60],
        [0, 1, 15, 25, 6, 7, 30, 40, 50],
    ]

    for arr in arr_list:
        print("input:", arr, "\nOutput:", unsorted_array(arr))
