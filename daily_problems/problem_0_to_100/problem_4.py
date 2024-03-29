"""
Given an array of integers, find the first missing positive integer in linear time and constant
space. In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.
"""


def first_missing_positive_integer_using_constant_space(arr):
    length = len(arr)

    # part 1: Segregate the array using +ve and-ve values
    start, end = 0, length - 1

    while True:
        while start < length and arr[start] > 0:
            start += 1
        while end >= 0 and arr[end] <= 0:  # treat 0 as -ve value, ignore it.
            end -= 1

        if start >= end:
            break

        arr[start], arr[end] = arr[end], arr[start]

    # part 2: change sign of values at index of existing +ve integers to -ve
    for index in range(start):
        value = abs(arr[index])

        if value <= start:
            arr[value - 1] = -(abs(arr[value - 1]))

    # part 3: find the missing value
    for index in range(length):
        if arr[index] > 0:
            return index + 1

    return start + 1


# using set in O(n) and O(n)
def first_missing_positive_integer(arr):
    arr = set(arr)

    for i in range(1, len(arr) + 2):
        if i not in arr:
            return i


def first_missing_positive_integer_using_extra_space(arr):
    arr_2 = [-1] * (len(arr) + 2)  # in case there is no missing element, return n+1

    for key, val in enumerate(arr):
        # taking advantage of the fact that any value cannot be greater than len(arr)
        if val >= 0:
            arr_2[val] = 1

    for i in range(1, len(arr_2)):
        if arr_2[i] < 0:
            return i

    return None


if __name__ == "__main__":
    assert first_missing_positive_integer_using_constant_space([1, 2, 3]) == 4
    assert first_missing_positive_integer_using_constant_space([1, 2, 0]) == 3
    assert first_missing_positive_integer_using_constant_space([1, -2, 3]) == 2
    assert first_missing_positive_integer_using_constant_space([-1, -2, 3]) == 1
    assert first_missing_positive_integer_using_constant_space([-1, -2, 0]) == 1
