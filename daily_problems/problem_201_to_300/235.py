"""
Given an array of numbers of length N, find both the minimum
and maximum using less than 2 * (N - 2) comparisons.
"""
from typing import List, Tuple


def min_max(arr: List[int]) -> Tuple[int, int]:
    """
    3 * n / 2
    """
    size = len(arr)

    if size < 2:
        return arr[0], arr[0]

    if arr[0] > arr[1]:
        min_val = arr[1]
        max_val = arr[0]
    else:
        min_val = arr[0]
        max_val = arr[1]

    index = 2

    for index in range(2, size - 1, 2):
        if arr[index] < arr[index + 1]:
            min_val = min(arr[index], min_val)
            max_val = max(arr[index + 1], max_val)
        else:
            min_val = min(arr[index + 1], min_val)
            max_val = max(arr[index], max_val)

    if index == size - 1:
        if min_val > arr[index]:
            min_val = arr[index]
        elif max_val < arr[index]:
            max_val = arr[index]

    return min_val, max_val


if __name__ == "__main__":
    assert min_max([1000, 11, 445, 1, 330, 3000]) == (1, 3000)
