"""
Given an integer n and a list of integers l, write a function
that randomly generates a number from 0 to n-1 that isn't in l (uniform).
"""
from random import randint


def custom_random(n: int, arr: list) -> int:
    """
    non deterministic method
    """
    arr = set(arr)

    while True:
        if (num := randint(1, n)) not in arr:
            return num


if __name__ == "__main__":
    for _ in range(10):
        print(custom_random(10, [2, 3, 6, 8]))
