"""
Given an array of integers and a number k, where 1 <= k <= length of the array,
compute the maximum values of each subarray of length k.
For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
    10 = max(10, 5, 2)
    7 = max(5, 2, 7)
    8 = max(2, 7, 8)
    8 = max(7, 8, 7)

Do this in O(n) time and O(k) space.
You can modify the input array in-place and you do not need to store the results.
You can simply print them out as you compute them.
"""
from collections import deque


def max_subarray(arr: list, k: int) -> None:
    """
    Add new element's index to deque.
    Remove elements
        1. from beginning i-k >= element's index
        2. from end (while inserting a new) if new element's value is greater

    Time Complexity: O(n)
    Space Complexity: O(k)
    """
    subarray: deque = deque(maxlen=k)

    for i in range(k):
        while subarray and arr[i] > arr[subarray[-1]]:
            subarray.pop()
        subarray.append(i)

    for i in range(k, len(arr)):
        print(arr[subarray[0]])

        while subarray and subarray[0] <= i - k:
            subarray.popleft()

        while subarray and arr[i] > arr[subarray[-1]]:
            subarray.pop()

        subarray.append(i)

    print(arr[subarray[0]])


if __name__ == "__main__":
    max_subarray([10, 5, 2, 7, 8, 7, 6, 5, 4], 3)
