"""
Given a 32-bit integer, return the number with its bits reversed.

For example,
    given the binary number 1111 0000 1111 0000 1111 0000 1111 0000,
    return 0000 1111 0000 1111 0000 1111 0000 1111.
"""
from random import randint


def reverse_bits(n: int) -> int:
    binary = f"{n:032b}"
    reversed_binary = "".join(reversed(list(binary)))
    print(binary)
    print(reversed_binary)
    integer = int(reversed_binary, 2)
    return integer


if __name__ == '__main__':
    print(reverse_bits(randint(1, 1_000_000)))
