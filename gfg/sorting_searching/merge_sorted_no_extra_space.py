"""
We are given two sorted array. We need to merge these two arrays such that
the initial numbers (after complete sorting) are in the first array and the
remaining numbers are in the second array without any extra space
"""
from typing import Tuple


def merge_sorted_arrays(a: list, b: list) -> Tuple[list, list]:
    """
    Time Complexity: O(m*n)
    Space Complexity: O(1)
    """
    i, la, lb = 0, len(a), len(b)

    while i < la:
        while i < la and a[i] < b[0]:
            i += 1

        if i >= la:
            break

        a[i], b[0] = b[0], a[i]
        j = 0

        while j < lb - 1 and b[j] > b[j + 1]:
            b[j], b[j + 1] = b[j + 1], b[j]
            j += 1

    return a, b


if __name__ == "__main__":
    arr1_list: list = [[10], [1, 5, 9, 10, 15, 20]]
    arr2_list: list = [[2, 3], [2, 3, 8, 13]]

    for a, b in zip(arr1_list, arr2_list):
        print(a, b)
        print(merge_sorted_arrays(a, b))
