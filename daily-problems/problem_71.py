"""
Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform
probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive).
"""
from random import randint


def rand7() -> int:
    return randint(1, 7)


def rand5() -> int:
    while True:
        return_value: int = rand7()
        if return_value < 6:
            return return_value


if __name__ == "__main__":
    print(rand5())
