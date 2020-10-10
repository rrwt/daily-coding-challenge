"""
The number 6174 is known as Kaprekar's constant:
    for all four-digit numbers with at least two distinct digits,
    repeatedly applying a simple procedure eventually results in
    this value. The procedure is as follows:
    For a given input x, create two new numbers that consist of
    the digits in x in ascending and descending order.
    Subtract the smaller number from the larger number.

For example, this algorithm terminates in three steps when starting from 1234:
    4321 - 1234 = 3087
    8730 - 0378 = 8352
    8532 - 2358 = 6174

Write a function that returns how many steps this will take for a given input N.
"""


def kaprekar_constant_count(x: int) -> int:
    x = list(str(x))
    smaller = sorted(x)
    larger = smaller[::-1]
    smaller = int("".join(smaller))
    larger = int("".join(larger))
    diff = larger - smaller

    if diff == 6174:
        return 1

    return 1 + kaprekar_constant_count(diff)


if __name__ == "__main__":
    assert kaprekar_constant_count(1234) == 3
