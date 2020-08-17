"""
Given an even number (greater than 2),
return two prime numbers whose sum will be equal to the given number.

A solution will always exist. See Goldbach’s conjecture.

Example:
    Input: 4
    Output: 2 + 2 = 4

If there are more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then
[a, b] < [c, d], If a < c OR a==c AND b < d.
"""
from typing import Tuple, List


def get_prime_numbers_till(number: int, primes: List = [2, 3]) -> List[int]:
    # list in argument for memoization (next call will not calculate anything til the last number)
    for num in range(primes[-1] + 2, number, 2):
        for prime in primes:
            if num % prime == 0:
                break
        else:
            primes.append(num)

    return primes


def get_prime_pair_using_primes(number: int) -> Tuple[int, int]:
    primes = get_prime_numbers_till(number)
    primes = [1] + primes
    prime_set = set(primes)

    for first in primes:
        if number - first in prime_set:
            return first, number - first


if __name__ == "__main__":
    for _ in range(2, 101, 2):
        print(f"prime pairs for {_} are", get_prime_pair_using_primes(_))
