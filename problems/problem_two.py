"""
Given an array of integers, return a new array such that each element at index i
of the new array is the product of all the numbers in the original array except
the one at i. For example, if our input was [1, 2, 3, 4, 5], the expected output
would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output
would be [2, 3, 6].

Follow-up: what if you can't use division?
"""
import operator
import functools


# naive solution with / operation: O(n)
def get_product_array(arr):
    if len(arr) < 2:
        return []

    prod = functools.reduce(operator.mul, arr)

    return [prod / n for n in arr]


# more restrictive solution: without / operation: O(n)
def get_product_array_without_division(arr):
    if len(arr) < 2:
        return []

    l = len(arr)
    left_product = [1] * l
    right_product = [1] * l

    for i in range(1, l):
        left_product[i] = left_product[i-1] * arr[i-1]

    for i in range(l-2, -1, -1):
        right_product[i] = right_product[i+1] * arr[i+1]

    return [left_product[i]*right_product[i] for i in range(l)]
