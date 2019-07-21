"""
Given an array of size n and multiple values around which we need to left rotate the array.
How to quickly find multiple left rotations?
"""
from array import array


def get_rotation(arr: array, k: int) -> array:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    length: int = len(arr)
    k = k % length
    res: array = array("B")

    for i in range(length):
        res.append(arr[(k + i) % length])

    return res


if __name__ == "__main__":
    arr: array = array("B", [1, 3, 5, 7, 9])

    for k in range(2, 6):
        print(get_rotation(arr, k))

    print(get_rotation(array("B", [1, 3, 5, 7, 9]), 14))

