"""
Find the maximum of two numbers without using any if-else statements,
branching, or direct comparisons.
"""


def get_max(a: int, b: int) -> int:
    """
    if a < b then -(a < b) = -1
    elif a > b then -(a < b) = 0

    (a^b) & -1 = a^b
    (a^b) & 0 = 0
    """
    return a ^ ((a ^ b) & -(a < b))


def get_min(a: int, b: int) -> int:
    return b ^ ((a ^ b) & -(a < b))


if __name__ == "__main__":
    assert get_max(5, 10) == 10
    assert get_min(5, 10) == 5
