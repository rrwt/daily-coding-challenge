"""
Given an integer n, return the length of the longest
consecutive run of 1s in its binary representation.
For example, given 156, you should return 3.
"""


def longest_consecutive_run(n: int) -> int:
    max_count = 0
    count = 0

    while n > 0:
        if n & 1:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0

        n >>= 1

    return max_count


if __name__ == "__main__":
    assert longest_consecutive_run(156) == 3
