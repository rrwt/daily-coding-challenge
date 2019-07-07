"""
Exponential Search:Find an element in a sorted (un)bounded list of elements.
    The number of elements can be (un)known beforehand.
Time complexity: O(log(i)) - O(log(n)), where i is the index of element being searched
Space complexity: O(1)

- Better than binary search if the element lies near the starting point
"""
from array import array

from binary_search import bin_search_iterative  # type: ignore


def exponential_search(arr: array, element: int) -> int:
    i: int = 1
    n: int = len(arr)

    while i < n and arr[i] <= element:
        i *= 2

    return bin_search_iterative(arr, element, int(i / 2), min(i, n - 1))


if __name__ == "__main__":
    arr = array("H", [10, 20, 40, 45, 55, 75])
    print("Element", 10, "found at position", exponential_search(arr, 10))
    print("Element", 20, "found at position", exponential_search(arr, 20))
    print("Element", 45, "found at position", exponential_search(arr, 45))
    print("Element", 55, "found at position", exponential_search(arr, 55))
    print("Element", 75, "found at position", exponential_search(arr, 75))
    print("Element", 0, "found at position", exponential_search(arr, 0))
    print("Element", 30, "found at position", exponential_search(arr, 30))
    print("Element", 80, "found at position", exponential_search(arr, 80))
