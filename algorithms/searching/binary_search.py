"""
Binary Search: Given a sorted array, return the position of element x in it. If not return -1.
Time complexity: O(logn)
Space Complexity: O(logn) in case of recursive and O(1) in case of iterative implementation.
"""
import math
from array import array


def bin_search_recursive(arr: array, element: int, start: int, end: int) -> int:
    if start <= end:
        mid = math.floor(start + (end - start) / 2)

        if element == arr[mid]:
            return mid
        elif element > arr[mid]:
            return bin_search_recursive(arr, element, mid + 1, end)

        return bin_search_recursive(arr, element, start, mid - 1)

    return -1


def bin_search_iterative(arr: array, element: int, start: int, end: int) -> int:
    while start <= end:
        mid = math.floor(start + (end - start) / 2)

        if element == arr[mid]:
            return mid
        elif element > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


if __name__ == "__main__":
    from random import randint

    arr = array("B", (2, 3, 4, 10, 40))
    el1, el2, el3, end = 10, 2, randint(0, 100), len(arr) - 1

    print("Recursive position of", el1, ":", bin_search_recursive(arr, el1, 0, end))
    print("Recursive position of", el2, ":", bin_search_recursive(arr, el2, 0, end))
    print("Recursive position of", el3, ":", bin_search_recursive(arr, el3, 0, end))
    print("Iterative position of", el1, ":", bin_search_iterative(arr, el1, 0, end))
    print("Iterative position of", el2, ":", bin_search_iterative(arr, el2, 0, end))
    print("Iterative position of", el3, ":", bin_search_iterative(arr, el3, 0, end))
