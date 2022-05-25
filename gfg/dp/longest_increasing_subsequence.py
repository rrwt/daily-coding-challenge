"""Longest Increasing Subsequence

Given an array of integers, find the length of the longest increasing subarray.
"""
from typing import List


def lis_recursive(arr: List[int], cur_index: int, length: int, last_element: int) -> int:
    """
    Time Complexity: Exponential
    """
    if cur_index >= length:
        return 0

    incl = 0
    if arr[cur_index] > last_element:
        incl = 1 + lis_recursive(arr, cur_index + 1, length, arr[cur_index])

    exc = lis_recursive(arr, cur_index + 1, length, last_element)

    return max(incl, exc)


def lis_dp_tabulation(arr: List[int]) -> int:
    """
    Time Complexity: O(n*n)
    """
    length: int = len(arr)
    result: List[int] = [1] * length

    for i in range(1, length):
        for j in range(i - 1, -1, -1):
            if arr[i] > arr[j] and result[j] >= result[i]:
                result[i] = result[j] + 1

    return result[length - 1]


if __name__ == "__main__":
    assert lis_recursive([10, 22, 9, 33, 21, 50, 41, 60, 80], 0, 9, -1) == 6
    assert lis_dp_tabulation([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 6
