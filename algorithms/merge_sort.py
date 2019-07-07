"""
Merge Sort: Divide and Conquer sorting algorithm. Repeatedly get smaller subarrays
    and merge them in sorted manner.
Time Complexity: O(nlogn) - bet, worst, average
Space Complexity: O(n)
Inplace: No
Stable: Yes

- Can even sort linked lists in O(nlogn).
- Constant operations are more expensive than that of QuickSort.
- Useful when sorting huge data (that can't fit in memory).
"""
import math
from array import array


def merge(first_arr: array, second_arr: array):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    i, j, first_len, second_len = 0, 0, len(first_arr), len(second_arr)
    res = array("H")

    while i < first_len and j < second_len:
        if first_arr[i] <= second_arr[j]:
            res.append(first_arr[i])
            i += 1
        else:
            res.append(second_arr[j])
            j += 1

    if i < first_len:
        res.extend(first_arr[i:])
    if j < second_len:
        res.extend(second_arr[j:])

    return res


def merge_sort_recursive(arr: array, start: int, end: int) -> array:
    """
    Time Complexity: O(log(n))
    Space Complexity: O(log(n))  # recursive stack
    """
    if start < end:
        mid = math.floor(start + (end - start) / 2)
        left = merge_sort_recursive(arr, start, mid)
        right = merge_sort_recursive(arr, mid + 1, end)
        return merge(left, right)

    return array("H", [arr[start]]) if start == end else array("H")


if __name__ == "__main__":
    # TODO: Iterative merge sort
    arr = array("H", [12, 11, 13, 5, 6, 7])
    start, end = 0, len(arr) - 1
    print(*merge_sort_recursive(arr, start, end))
