"""
Given two integers x and n, write a function to compute x^n.
We may assume that x and n are small and overflow doesn’t happen.
"""
from typing import Union


def power(x: int, n: int) -> Union[int, float]:
    if n == 0:
        return 1
    if n == 1:
        return x
    if n == -1:
        return 1 / x
    temp = power(x, n // 2)
    if n % 2 == 0:
        return temp * temp
    else:
        return x * temp * temp if n > 0 else temp * temp / x


if __name__ == "__main__":
    print(power(5, -2))
    print(power(5, 2))
