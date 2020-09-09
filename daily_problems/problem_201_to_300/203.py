"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.
For example, given [5, 7, 10, 3, 4], return 3.
"""
from typing import List


def min_element(arr: List[int]) -> int:
    length = len(arr)

    if length == 0:
        return -1
    if length == 1 or arr[0] < arr[-1]:
        return arr[0]  # sorted
    if arr[-1] < arr[-2]:
        return arr[-1]  # last element

    start, end = 0, length - 1

    while start <= end:
        mid = (start + end) >> 1

        if arr[mid] < arr[mid + 1] < arr[mid - 1]:
            return arr[mid]
        elif arr[mid] < arr[end]:
            end = mid - 1
        else:
            start = mid + 1


if __name__ == "__main__":
    assert min_element([5, 7, 10, 3, 4]) == 3
    assert min_element([5, 7, 8, 10, 3, 4]) == 3
    assert min_element([5, 7, 8, 9, 10, 3, 4]) == 3
    assert min_element([5, 7, 8, 9, 10, 3]) == 3
    assert min_element([6, 7, 8, 9, 10, 3, 4, 5]) == 3
