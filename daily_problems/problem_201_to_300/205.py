"""
Given an integer, find the next permutation of it in absolute order.
For example, given 48975, the next permutation would be 49578.
"""


def next_permutation(integer: int) -> int:
    """
    Find first digit from right to left, which is greater than it's left neighbor.
    1. If found:
        i. Exchange the two
        ii. sort all digit from it's original position to the end
    2. If not found, this means we are at the max val:
        i. sort the digits to get lowest value

    """
    digits = [int(_) for _ in str(integer)]
    length = len(digits)

    while True:
        start = length - 1

        while start > -1 and digits[start] <= digits[start - 1]:
            start -= 1

        if start == -1:
            digits = reversed(digits)
        else:
            digits[start], digits[start - 1] = digits[start - 1], digits[start]
            digits = digits[:start] + sorted(digits[start:])

        yield int("".join([str(_) for _ in digits]))


if __name__ == "__main__":
    perm = next_permutation(48975)

    for _ in range(20):
        print(next(perm))
