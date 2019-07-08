"""
Heap Sort: Comparison based sorting technique based on binary heap.
Time Complexity: O(nlogn)
Space Complexity: O(1)
Stable: No
Inplace: Yes

- Can sort a nearly (k) sorted array
- Can help find largest/smallest k elements in O(klogn)
- For general purpose sorting, mergesort and quicksort faster
"""
import math
from array import array


def heapify(arr: array, start: int, end: int) -> None:
    """
    Find appropriate position for a given element in the heap
    Time Complexity: O(log(n))
    """
    while True:
        left_index = left_child(start)
        right_index = right_child(start)
        largest_index = start

        if left_index <= end and arr[left_index] > arr[largest_index]:
            largest_index = left_index
        if right_index <= end and arr[right_index] > arr[largest_index]:
            largest_index = right_index

        if largest_index != start:
            arr[start], arr[largest_index] = arr[largest_index], arr[start]
            start = largest_index
        else:
            break


def parent(index: int) -> int:
    if index <= 0:
        raise AssertionError("Invalid index")
    return math.floor((index - 1) / 2)


def left_child(index: int) -> int:
    return 2 * index + 1


def right_child(index: int) -> int:
    return 2 * (index + 1)


def heap_sort(arr: array) -> array:
    end: int = len(arr) - 1

    for i in range(end, 0, -1):
        p = parent(i)
        if arr[p] < arr[i]:
            arr[p], arr[i] = arr[i], arr[p]

    while end > 0:  # O(n)
        arr[end], arr[0] = arr[0], arr[end]
        end -= 1
        heapify(arr, 0, end)

    return arr


if __name__ == "__main__":
    print(*heap_sort(array("H", [12, 11, 13, 5, 6, 7])))
