"""
The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N.
The method is to take increasingly larger prime numbers, and mark their multiples as composite.
For example, to find all primes less than 100, we would first mark [4, 6, 8, ...]
(multiples of two), then [6, 9, 12, ...] (multiples of three), and so on. Once we have
done this for all primes less than N, the unmarked numbers that remain will be prime.
Implement this algorithm.
Bonus: Create a generator that produces primes indefinitely(without taking N as an input).
"""


class SieveOfEratosthenes:
    def __init__(self):
        self.primes = []

    def next(self) -> int:
        if not self.primes:
            self.primes = [2]
        else:
            num = 3 if self.primes[-1] == 2 else self.primes[-1] + 2

            while True:
                for prime in self.primes:
                    if num % prime == 0:
                        num += 2
                        break
                else:
                    self.primes.append(num)
                    break

        return self.primes[-1]


if __name__ == "__main__":
    soe = SieveOfEratosthenes()

    for _ in range(30):
        print(soe.next())
