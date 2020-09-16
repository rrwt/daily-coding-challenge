"""
Implement the function fib(n), which returns the nth
number in the Fibonacci sequence, using only O(1) space.
"""


def fibonacci(n: int) -> int:
    a, b = 0, 1

    if n < 2:
        return n

    for i in range(2, n + 1):
        a, b = b, a + b

    return b


if __name__ == "__main__":
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
