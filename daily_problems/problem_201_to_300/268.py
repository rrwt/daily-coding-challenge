"""
Given a 32-bit positive integer N, determine whether
it is a power of four in faster than O(log N) time
"""


def power_of_4(n: int) -> bool:
    return (n & (n - 1) == 0) and (n - 1) % 3 == 0


def power_of_4_alt(n: int) -> bool:
    return (n & (n - 1) == 0) and (n & 0x55555555 != 0)


if __name__ == "__main__":
    assert power_of_4(64) is True
    assert power_of_4_alt(64) is True
