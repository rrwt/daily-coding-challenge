"""
Given a real number n, find the square root of n. For example, given n = 9, return 3.
"""


def almost_equal(first: float, second: float) -> bool:
    if abs(first - second) < 0.0001:
        return True
    return False


def my_sqrt(n: int) -> int:
    if n < 2:
        return n

    start, end = 0, n

    while start < end:
        mid = start + (end - start) / 2

        if almost_equal(mid * mid, n):
            return mid
        if mid * mid < n:
            start = mid
        else:
            end = mid


if __name__ == "__main__":
    assert almost_equal(my_sqrt(9), 3) is True
    assert almost_equal(my_sqrt(4), 2) is True
    assert almost_equal(my_sqrt(25), 5) is True
    assert almost_equal(my_sqrt(2), 1.4142135) is True
