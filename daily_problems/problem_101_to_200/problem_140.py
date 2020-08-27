"""
Given an array of integers in which two elements appear
exactly once and all other elements appear exactly twice,
find the two elements that appear only once.

For example,
    given the array [2, 4, 6, 8, 10, 2, 6, 10],
    return 4 and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?
"""
from typing import Tuple, List


def get_single_elements(elements: List[int]) -> Tuple[int, int]:
    a_x_b = 0  # xor of two numbers

    for element in elements:
        a_x_b ^= element

    for i in range(32):
        # get first set bit of xor list
        # this will be set either on a or on b
        if (first_set_bit := (1 << i) & a_x_b) > 0:
            break
    else:
        raise Exception("All numbers are duplicate")

    a = b = 0

    for element in elements:
        if element & first_set_bit:
            a ^= element
        else:
            b ^= element

    return a, b


if __name__ == "__main__":
    print(get_single_elements([2, 4, 6, 8, 10, 2, 6, 10]))
