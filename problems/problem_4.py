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
