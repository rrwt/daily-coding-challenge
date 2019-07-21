"""
Given an array of n elements, create a new array which is a rotation of
given array and hamming distance between both the arrays is maximum.
"""
from array import array


def max_hamming_distance(arr: array) -> int:
    """
    Time Complexity: O(n*n)
    """
    length: int = len(arr)
    max_distance: int = 0

    for i in range(1, length):
        cur_distance: int = 0
        for j in range(length):
            if arr[j] != arr[(i + j) % length]:
                cur_distance += 1

        max_distance = max(max_distance, cur_distance)

    return max_distance


if __name__ == "__main__":
    print(max_hamming_distance(array("B", [1, 4, 1])))
    print(max_hamming_distance(array("B", [2, 4, 8, 0])))
