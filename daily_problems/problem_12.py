"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N,
write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number
from a set of positive integers X?
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""


def staircase_1_2(n: int) -> int:
    """Case 1
    Logic: Solution to nth iteration is the sum of n-1th and n-2th iteration, similar to fibonacci.
    This is because we can only climb 1 or 2 steps at a time
    """
    if n < 3:
        return n

    a, b = 1, 2
    for _ in range(n - 2):
        a, b = b, a + b

    return b


def staircase(n: int, choices: set) -> int:
    """case 2
    Generalized situation. In this case the sum would be f(n) = f(n-x1) + f(n-x2) + ...
    time complexity: O(n*|x|)
    space complexity: O(n)
    """
    cache = [0] * (n + 1)
    cache[0] = 1

    for i in range(1, n + 1):
        cache[i] = sum(cache[i - v] for v in choices if v <= i)

    return cache[n]


if __name__ == "__main__":
    assert staircase_1_2(1) == 1
    assert staircase_1_2(2) == 2
    assert staircase_1_2(3) == 3
    assert staircase_1_2(4) == 5
    assert staircase_1_2(5) == 8

    x = {1, 3, 5}
    print(staircase(1, x))
    print(staircase(2, x))
    print(staircase(3, x))
    print(staircase(4, x))
    print(staircase(5, x))
    print(staircase(6, x))
    print(staircase(7, x))
    print(staircase(8, x))
    print(staircase(9, x))
    print(staircase(10, x))
