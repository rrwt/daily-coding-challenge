"""
Insertion sort: Sort like a hand of cards.
Time Complexity: worst - O(n*n) - reverse sorted
                 best - O(n) - (almost)already sorted
Space Complexity: O(1)
Stable: Yes
Inplace: Yes
"""
from array import array


def insertion_sort(arr: array) -> array:
    length: int = len(arr)

    for i in range(1, length):
        j = i
        element = arr[j]

        while j > 0 and element < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1

        arr[j] = element

    return arr


if __name__ == "__main__":
    print(*insertion_sort(array("H", [12, 11, 13, 5, 6])))
