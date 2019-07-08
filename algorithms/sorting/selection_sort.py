"""
Selection Sort: Sorts a given array inplace.
    Pick up the next smallest element and put it in it's place.
Time Complexity: O(n*n)
Space Complexity: O(1)
Inplace: Yes
Stable: No
Max. Swaps: O(n)
Useful when memory writes are expensive. Does least number of memory writes: O(n)
"""
from array import array


def selection_sort(arr: array) -> array:
    length: int = len(arr)

    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[min_index], arr[i] = arr[i], arr[min_index]

    return arr


if __name__ == "__main__":
    print(*selection_sort(array("H", [64, 25, 12, 22, 11])))
