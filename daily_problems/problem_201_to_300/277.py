"""
UTF-8 is a character encoding that maps each symbol to one, two, three, or four bytes.
For example, the Euro sign, €, corresponds to the three bytes 11100010 10000010 10101100.
The rules for mapping characters are as follows:
    For a single-byte character, the first bit must be zero.
    For an n-byte character, the first byte starts with n ones and a zero.
    The other n - 1 bytes all start with 10.
Visually, this can be represented as follows.
 Bytes   |           Byte format
-----------------------------------------------
   1     | 0xxxxxxx
   2     | 110xxxxx 10xxxxxx
   3     | 1110xxxx 10xxxxxx 10xxxxxx
   4     | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

Write a program that takes in an array of integers representing byte values,
and returns whether it is a valid UTF-8 encoding.
"""
from typing import List


def validate_utf(values: List[int]) -> bool:
    num_bytes = len(values) // 8

    if num_bytes != len(values) / 8:
        return False

    if num_bytes == 1:
        return values[0] == 0

    for index in range(num_bytes):
        if values[index] != 1:
            return False

    if values[num_bytes] != 0:
        return False

    for index in range(1, num_bytes):
        j = index * 8

        if values[j] != 1 or values[j + 1] != 0:
            return False

    return True


if __name__ == "__main__":
    assert (
        validate_utf(
            [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0]
        )
        is True
    )
