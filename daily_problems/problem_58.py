"""
An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time.
If the element doesn't exist in the array, return null.
For example, given the array [13, 18, 25, 2, 8, 10] and the element 8,
return 4 (the index of 8 in the array).
You can assume all the integers in the array are unique.
"""
from typing import Optional


def find_index(arr: list, k: int) -> Optional[int]:
    start, end = 0, len(arr) - 1

    while start <= end:
        mid: int = (start + end) >> 1

        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            if k < arr[0] < arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if k > arr[0] > arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return None


if __name__ == "__main__":
    sorted_rotated_array: list = [13, 18, 25, 2, 8, 10]

    assert find_index(sorted_rotated_array, 13) == 0
    assert find_index(sorted_rotated_array, 18) == 1
    assert find_index(sorted_rotated_array, 25) == 2
    assert find_index(sorted_rotated_array, 2) == 3
    assert find_index(sorted_rotated_array, 8) == 4
    assert find_index(sorted_rotated_array, 10) == 5
    assert find_index(sorted_rotated_array, 1) is None
