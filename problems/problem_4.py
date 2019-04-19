"""
Given an array of integers, find the first missing positive integer in linear time and constant
space. In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.
"""


# using set in O(n) and constant extra space
def first_missing_positive_integer(arr):
    arr = set(arr)

    for i in range(1, len(arr)+2):
        if i not in arr:
            return i


def first_missing_positive_integer_using_on_extra_space(arr):
    arr_2 = [-1] * (len(arr)+2)  # in case there is no missing element, return n+1

    for key, val in enumerate(arr):
        # taking advantage of the fact that any value cannot be greater than len(arr)
        if val >= 0:
            arr_2[val] = 1

    for i in range(1, len(arr_2)):
        if arr_2[i] < 0:
            return i

    return None
