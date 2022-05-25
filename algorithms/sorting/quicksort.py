"""
Quicksort: One of the fastest sorting algorithm. Divide and conquer.
    Select a pivot and place it in it's place in the array, then
    recursively do the same for left and right partitions of the remaining array.
Time Complexity: O(n*log(n)) [O(n*n) - Worst case]
Space Complexity: O(log(n))
Inplace: Yes
Stable: No
3-Way: Maintain 3 subarrays. 1. Of lesser value, 2. Of equal, 3. Of greater
"""


def partition(arr: list, start: int, end: int) -> int:
    """
    Choosing last element as pivot
    """
    i, j = start - 1, start

    while j < end:
        if arr[j] < arr[end]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1

    i += 1
    arr[i], arr[end] = arr[end], arr[i]
    return i


def quicksort_recursive(arr: list, start: int, end: int) -> None:
    if start < end:
        partition_index: int = partition(arr, start, end)
        quicksort_recursive(arr, start, partition_index - 1)
        quicksort_recursive(arr, partition_index + 1, end)


def quicksort_iterative(arr: list, start: int, end: int) -> None:
    from collections import deque

    q: deque = deque()
    q.append((start, end))

    while q:
        start, end = q.popleft()

        if start < end:
            p = partition(arr, start, end)

            if p - 1 > start:
                q.append((start, p - 1))
            if p + 1 < end:
                q.append((p + 1, end))


if __name__ == "__main__":
    arr = [80, 90, 100, 70, 60, 50, 40, 10, 20, 30]
    print("before sorting:", *arr)
    quicksort_recursive(arr, 0, len(arr) - 1)
    print("after recursive sorting:", *arr)
    arr = [80, 90, 100, 70, 60, 50, 40, 10, 20, 30]
    quicksort_iterative(arr, 0, len(arr) - 1)
    print("after iterative sorting:", *arr)
