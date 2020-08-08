"""
Given an array of integers, write a function to determine whether
the array could become non-decreasing by modifying at most 1 element.

For example,
    given the array [10, 5, 7], you should return true,
    since we can modify the 10 into a 1 to make the array non-decreasing.

    Given the array [10, 5, 1], you should return false,
    since we can't modify any one element to get a non-decreasing array.
"""


def verify_non_decreasing(arr: list) -> bool:
    len_arr = len(arr)

    if len_arr < 3:
        return True

    stack = []
    count_del = 0

    for element in arr:
        while stack and stack[-1] > element:
            count_del += 1
            stack.pop()

        if count_del > 1:
            return False

        stack.append(element)

    return True


if __name__ == "__main__":
    assert verify_non_decreasing([10, 5, 7]) is True
    assert verify_non_decreasing([10, 5, 1]) is False
