"""
Given an array and a number k where k is smaller than size of array,
we need to find the k’th smallest element in the given array.
It is given that ll array elements are distinct.
"""
from random import randint


def quick_select(arr: list, k: int) -> int:
    """Quick Select algorithm
    This is basically a modified quicksort algorithm to find kth largest/smallest element.
    Time Complexity: O(n) - average and O(n*n) - worst
    """
    start, end = 0, len(arr) - 1

    while start <= end:
        pivot = randint(start, end)
        arr[pivot], arr[end] = arr[end], arr[pivot]  # important in case of random pivot
        pivot = end
        i, j = start - 1, start

        while j < end:
            if arr[j] < arr[pivot]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
            j += 1

        arr[j], arr[i + 1] = arr[i + 1], arr[j]

        if i + 1 == k - 1:
            return arr[i + 1]
        elif i + 1 < k - 1:
            start = i + 2
        else:
            end = i

    return -1


if __name__ == "__main__":
    print(quick_select([12, 3, 5, 7, 4, 19, 26], 3))
