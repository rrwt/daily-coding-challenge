"""
Jump Search: Jump √n steps and check if current value is greater
than value to be searched for. If yes, search linearly a
maximum of m-1 times. Else, Jump again
Time complexity: O(√n)
Space Complexity: O(1)

Generally better than linear and worst than binary search.
- preferred to binary search if jumping backwards is a costly operation
- Preferred when element to be searched is small and lies closer to start
"""
import math
from array import array


def linear_search(arr: array, element: int, start: int, end: int):
    for i in range(start, end + 1):
        if arr[i] == element:
            return i
        elif arr[i] > element:
            break

    return -1


def jump_search(arr: array, element: int) -> int:
    n: int = len(arr)
    m: int = math.floor(math.sqrt(n))
    i = 0

    while i < n - m:
        i += m

        if arr[i] > element:
            return linear_search(arr, element, i - m, i)

    return linear_search(arr, element, i + 1, n - 1)


if __name__ == "__main__":
    arr: array = array("H", [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610])
    print("Element", 1, "found at index", jump_search(arr, 1))
    print("Element", 144, "found at index", jump_search(arr, 144))
    print("Element", 610, "found at index", jump_search(arr, 610))
    print("Element", 0, "found at index", jump_search(arr, 0))
    print("Element", -1, "found at index", jump_search(arr, -1))
