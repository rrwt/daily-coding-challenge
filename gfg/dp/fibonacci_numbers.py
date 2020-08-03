"""
Fibonacci Numbers using DP
"""


def fibonacci(n: int) -> int:
    """
    O(n) & O(n)
    """
    if n < 2:
        return n

    fib = [0] * (n+1)
    fib[1] = 1

    for index in range(2, n+1):
        fib[index] = fib[index-1] + fib[index-2]

    return fib[n]


if __name__ == "__main__":
    for _ in range(20):
        print(fibonacci(_))
