"""
A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:
    if n is even, the next number in the sequence is n / 2
    if n is odd, the next number in the sequence is 3n + 1

It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.
Bonus: What input n <= 1000000 gives the longest sequence?
"""
from functools import lru_cache
from typing import Tuple


@lru_cache(maxsize=1_000_000)
def collatz_sequence(n: int) -> Tuple[bool, int]:
    if n == 1:
        return True, 1
    elif n < 1:
        return False, 1

    if n & 1:
        converged, count = collatz_sequence(3 * n + 1)
    else:
        converged, count = collatz_sequence(n // 2)

    return converged, count + 1


def get_longest_sequence(max_val: int) -> int:
    num_with_longest_seq = 1
    max_count = 1

    for n in range(2, max_val + 1):
        converged, count = collatz_sequence(n)

        if converged and count > max_count:
            num_with_longest_seq = n
            max_count = count

    return num_with_longest_seq


if __name__ == "__main__":
    for val in range(1, 100):
        assert collatz_sequence(val)[0] is True

    assert get_longest_sequence(1_000_000) == 837799
