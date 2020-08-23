"""
A number is considered perfect if its digits sum up to exactly 10.
Given a positive integer n, return the n-th perfect number.
For example, given 1, you should return 19. Given 2, you should return 28.
"""
import random
import math


def get_sum_of_digs(x: int) -> int:
    s: int = 0

    while True:
        while x:
            s += x % 10
            x = x // 10

        if s <= 10:
            return s
        else:
            x = s
            s = 0


def perfect_number_brute_force(n: int) -> int:
    """
    Start With 19 and add 9 to it. Verify the solution.
    """
    if n < 1:
        return 0

    number: int = 19
    if n == 1:
        return number

    while n > 1:
        x = 0

        while x != 10:
            number += 9
            x = get_sum_of_digs(number)

        n -= 1

    return number


def perfect_number_faster(n: int) -> int:
    """
    The solution to the problem is an AP with a = 19 and d = 9.
    There are some outliers such as 100, 1000, 10_000 ...
    Therefore the final solution would be: 19 + (n-1+number_of_outliers)*9

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    if n < 1:
        return 0

    nth_element = 19 + (n - 1) * 9
    outliers = int(math.log10(nth_element)) - 1
    return nth_element + outliers * 9


if __name__ == "__main__":
    for _ in range(5):
        n: int = random.randint(1, 1000)
        print("N:", n)
        print("brute force solution:", perfect_number_brute_force(n))
        print("Faster solution:", perfect_number_faster(n))
