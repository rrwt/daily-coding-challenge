# Super-ugly numbers are positive numbers with all prime factors in the given prime list.
# Given a number n, the task is to find n’th Super-Ugly number.
# It may be assumed that given set of primes is sorted.
# Also, first Super-Ugly number is 1 by convention.
from typing import List


def super_ugly_numbers(n: int, primes: List[int]) -> int:
    # get nth super-ugly number
    ugly_nums = [0] * n
    ugly_nums[0] = 1
    length = len(primes)
    multiplier_indices = [0] * length
    multipliers = primes[:]

    for index in range(1, n):
        ugly_nums[index] = min(multipliers)

        for inner_index in range(length):
            if ugly_nums[index] == multipliers[inner_index]:
                multiplier_indices[inner_index] += 1
                multipliers[inner_index] = ugly_nums[multiplier_indices[inner_index]] * primes[inner_index]

    return ugly_nums[n-1]


if __name__ == "__main__":
    print(super_ugly_numbers(5, [2, 5]))
    print(super_ugly_numbers(12, [2, 7, 13, 19]))
