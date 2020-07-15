"""
Implement integer exponentiation.
That is, implement the pow(x, y) function,
where x and y are integers and returns x^y.
Do this faster than the naive method of repeated multiplication.
For example, pow(2, 10) should return 1024.
"""
from typing import Union


def pow(x: Union[int, float], y: int) -> Union[int, float]:
    """
    y can be +ve or -ve
    x can be int or float (always positive)
    Time Complexity: O(log(n))
    Space Complexity: O(log(n))  # stack size
    """

    def calc_pow(x: Union[int, float], y: int) -> Union[int, float]:
        if y == 0:
            return 1
        if y == -1:
            return 1 / x
        if y == 1:
            return x

        res = pow(x, int(y / 2))

        if y % 2 == 0:
            return res * res
        else:
            if y > 0:
                return x * res * res
            return res * res / x

    if x < 0:
        raise AssertionError("Invalid value")
    if x in (0, 1):
        return x

    return calc_pow(x, y)


if __name__ == "__main__":
    assert pow(2, 10) == 1024
    assert pow(3, 5) == 3 ** 5
    assert pow(3, -3) == 1 / 27
