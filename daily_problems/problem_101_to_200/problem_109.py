"""
Given an unsigned 8-bit integer, swap its even and odd bits.
The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.
For example,
    10101010 should be 01010101.
    11100010 should be 11010001.

Bonus: Can you do this in one line?
"""


def swap_bits(number: int) -> int:
    # & with 0x55555555 provides all odd bits.
    # & with 0xAAAAAAAA provides all even bits.
    return ((number & 0x55555555) << 1) | ((number & 0xAAAAAAAA) >> 1)


if __name__ == "__main__":
    num1 = int("10101010", 2)
    print(num1)
    print(swap_bits(num1))
