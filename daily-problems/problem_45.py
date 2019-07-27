"""
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability,
implement a function rand7() that returns an integer from 1 to 7 (inclusive).
"""
from random import randint


def rand5() -> int:
    return randint(1, 5)


def rand25() -> int:
    return 5 * rand5() + rand5() - 5


def rand7() -> int:
    """
    We can generate a random number from 1 to 25 using rand5 (5*rand5 + rand5 - 5).
    21 is divisible by 7. Therefore if we get a number between 1 and 21, we return number % 7 + 1.
    Else, we try again
    """

    while True:
        num: int = int(rand25())

        if num < 22:
            return num % 7 + 1


if __name__ == "__main__":
    for i in range(1000):
        print(rand7())
