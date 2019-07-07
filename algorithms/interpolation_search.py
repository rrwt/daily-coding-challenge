"""
Interpolation Search: Similar to binary search but can have
    best case time complexity as O(log(log(n)))
    worst case time complexity: O(n)  (linear)

Formula: pos = low + (x-arr[low])*(hi-low)/(arr[hi] - arr[low])
"""
import math
from array import array


def interpolation_search(arr: array, element: int) -> int:
    start: int = 0
    end: int = len(arr) - 1

    while start <= end and arr[start] <= element <= arr[end]:
        position: int = math.floor(
            start + (end - start) * (element - arr[start]) / (arr[end] - arr[start])
        )

        if arr[position] == element:
            return position
        if arr[position] > element:
            end = position - 1
        else:
            start = position + 1

    return -1


if __name__ == "__main__":
    arr = array("H", [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47])
    print("Element", 13, "Found at position", interpolation_search(arr, 13))
    print("Element", 42, "Found at position", interpolation_search(arr, 42))
    print("Element", 10, "Found at position", interpolation_search(arr, 10))
    print("Element", 47, "Found at position", interpolation_search(arr, 47))
    print("Element", 1, "Found at position", interpolation_search(arr, 1))
    print("Element", 55, "Found at position", interpolation_search(arr, 55))
    print("Element", 25, "Found at position", interpolation_search(arr, 25))
