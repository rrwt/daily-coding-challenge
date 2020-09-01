"""
You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}.
By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.
"""
from typing import List


def find_duplicate_arithmetic_series(arr: List[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    length = len(arr)
    return int(sum(arr) - (length * (length - 1) / 2))


def find_duplicate_set(arr: List[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    s = set()

    for element in arr:
        if element in s:
            return element
        s.add(element)


def find_duplicate_sign(arr: List[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for element in arr:
        val = abs(element)
        if arr[val] < 0:
            return val
        else:
            arr[val] = -arr[val]


if __name__ == "__main__":
    nums = [4, 5, 1, 7, 3, 2, 6, 5]
    assert find_duplicate_arithmetic_series(nums) == 5
    assert find_duplicate_set(nums) == 5
    assert find_duplicate_sign(nums) == 5
