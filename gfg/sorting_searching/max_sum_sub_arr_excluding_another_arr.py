"""
Given an array of A of n integers and an array B of m integers
find the Maximum Contiguous Subarray Sum of array A such that
any element of array B is not present in that subarray
"""


def max_sum_subarr(arr_a: list, arr_b: list) -> list:
    """
    Time Complexity: O(m+n)
    Space Complexity: (n)
    """
    set_b: set = set(arr_b)
    start, end, temp_start = -1, -1, 0
    max_so_far, max_ending_here = 0, 0

    for i, elem in enumerate(arr_a):
        if elem not in set_b:
            if max_ending_here + elem > 0:
                max_ending_here += elem
            elif elem > max_ending_here:
                max_ending_here = elem
                temp_start = i
            else:
                temp_start = i + 1

            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
                end = i
                start = temp_start
        else:
            max_ending_here = 0
            temp_start = i + 1

    return arr_a[start : end + 1]


if __name__ == "__main__":
    arr_a_list: list = [[1, 7, -10, 6, 2], [3, 4, 5, -4, 6]]
    arr_b_list: list = [[5, 6, 7, 1], [1, 8, 5]]
    res_list: list = [[2], [3, 4]]

    for arr_a, arr_b, res in zip(arr_a_list, arr_b_list, res_list):
        print("first array:", arr_a)
        print("second array:", arr_b)
        assert max_sum_subarr(arr_a, arr_b) == res
