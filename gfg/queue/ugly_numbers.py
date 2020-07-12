# Ugly numbers are numbers whose only prime factors are 2, 3 or 5.
# The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers.
# By convention, 1 is included.
import heapq
from typing import List, Optional


def ugly_number(n: int, primes: Optional[List[int]] = None) -> int:
    # find nth ugly number

    primes = primes or [2, 3, 5]
    ugly_numbers = [1]
    heapq.heapify(ugly_numbers)
    result = 1

    for index in range(n):
        result = heapq.heappop(ugly_numbers)

        while ugly_numbers and ugly_numbers[0] == result:  # remove duplicates
            heapq.heappop(ugly_numbers)

        for val in primes:
            heapq.heappush(ugly_numbers, result * val)

    return result


if __name__ == "__main__":
    for i in range(1, 20):
        print(ugly_number(i))
