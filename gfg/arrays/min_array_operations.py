"""
Consider an array with n elements and value of all the elements is zero. We can perform following operations on the array.
    Incremental operations: Choose 1 element from the array and increment its value by 1.
    Doubling operation: Double the values of all the elements of array.
We are given desired array target[] containing n elements.
Compute and return the smallest possible number of the operations
needed to change the array from all zeros to desired array.
"""
from functools import reduce


def construct_array(arr: list) -> int:
    res = 0
    length = len(arr)

    while True:
        zero_count = 0
        odd_count = 0
        i = 0

        while i < length:
            if arr[i] & 1:
                arr[i] -= 1
                odd_count += 1
                res += 1
            elif arr[i] == 0:
                zero_count += 1
            i += 1

        if zero_count == length:
            return res

        if odd_count == 0:
            for j in range(length):
                arr[j] >>= 1
            res += 1

    # Below is greedy and incorrect. e.g. test case [15, 16]
    # min_el: int = min(arr)

    # if min_el in (0, 1):
    #     return sum(arr)

    # res = len(arr)
    # value = 1

    # while value * 2 <= min_el:
    #     value <<= 1
    #     res += 1

    # res += sum([x - value for x in arr])
    # return res


if __name__ == "__main__":
    arr_list: list = [[2, 3], [2, 1], [16, 16, 16], [15, 16]]
    res_list: list = [4, 3, 7, 9]

    for arr, res in zip(arr_list, res_list):
        assert construct_array(arr) == res
