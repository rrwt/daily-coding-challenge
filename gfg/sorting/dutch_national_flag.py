"""Sort an array of 0s, 1s and 2s
Given an array A[] consisting 0s, 1s and 2s. The task is to write a function that
sorts the given array. The functions should put all 0s first, then all 1s and all
2s in last.
"""
import random


def count_and_sort(arr: list) -> list:
    """
    Time Complexity: O(n)
    """
    count_0, count_1, count_2 = 0, 0, 0

    for el in arr:
        if el == 0:
            count_0 += 1
        elif el == 1:
            count_1 += 1
        else:
            count_2 += 1

    return [0] * count_0 + [1] * count_1 + [2] * count_2


def dnf(arr: list) -> list:
    """
    Time Complexity: O(n)
    """
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:
            mid += 1

    return arr


if __name__ == "__main__":
    for _ in range(5):
        arr: list = [random.randint(0, 2) for _ in range(10)]
        print("original:", arr)
        print("count and sort:", count_and_sort(arr))
        print("dutch national flag:", dnf(arr))
        print("---------------------")
