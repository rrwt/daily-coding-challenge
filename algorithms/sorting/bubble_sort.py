"""
Bubble Sort: Swap adjacent elements if they are out of order. Largest element
    in unsorted array gets bubbled up to next last place.
Time Complexity: worst - O(n*n), best - O(n) (already sorted).
Space Complexity: O(1)
Stable: Yes
Inplace: Yes

- Useful when the array is sorted/almost sorted. O(n)
"""
from array import array


def bubble_sort(arr: array) -> array:
    length: int = len(arr)

    for i in range(length - 1, 0, -1):
        swapped: bool = False

        for j in range(i):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            break

    return arr


if __name__ == "__main__":
    print(*bubble_sort(array("H", [64, 34, 25, 12, 22, 11, 90])))
