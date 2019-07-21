"""
Find maximum value of Sum( i*arr[i]) with only rotations on given array allowed
Given an array, only rotation operation is allowed on array. We can rotate the
array as many times as we want. Return the maximum possbile of summation of i*arr[i].
"""
from array import array


def naive_max_sum(arr: array) -> int:
    """
    Time Complexity: O(n*n)
    Space Complexity: O(1)
    """
    length: int = len(arr)
    res: int = 0

    for i in range(length):
        temp_res: int = 0
        for j in range(length):
            rotated_index: int = (i + j) % length
            temp_res += rotated_index * arr[j]

        res = max(res, temp_res)

    return res


def max_sum(arr: array) -> int:
    """
    S(j) = S(j-1) + Sum of array - n * arr[n-j]
    where S(j) is the Sum of product of index and value for jth right rotation
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    sum_arr: int = sum(arr)
    length: int = len(arr)
    res: int = sum([i * arr[i] for i in range(length)])
    temp = res

    for i in range(1, length):
        temp += sum_arr - length * arr[length - i]
        res = max(res, temp)

    return res


if __name__ == "__main__":
    assert naive_max_sum(array("B", [1, 20, 2, 10])) == 72
    assert naive_max_sum(array("B", [10, 1, 2, 3, 4, 5, 6, 7, 8, 9])) == 330
    assert max_sum(array("B", [1, 20, 2, 10])) == 72
    assert max_sum(array("B", [10, 1, 2, 3, 4, 5, 6, 7, 8, 9])) == 330
