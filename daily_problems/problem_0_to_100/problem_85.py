"""
Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0,
using only mathematical or bit operations. You can assume b can only be 1 or 0.
"""


def get_result(x: int, y: int, b: int) -> int:
    b = -b  # all 1's in case of 1. 0 in case of 0
    return (x & b) | (y & ~b)


if __name__ == "__main__":
    assert get_result(55, 25, 1) == 55
