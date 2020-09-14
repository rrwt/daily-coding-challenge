"""
There are N prisoners standing in a circle, waiting to be executed.
The executions are carried out starting with the kth person,
and removing every successive kth person going clockwise until there is no one left.

Given N and k, write an algorithm to determine
where a prisoner should stand in order to be the last survivor.

For example,
    if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3],
    so you should return 3.

Bonus: Find an O(log N) solution if k = 2.
"""
import math


def josephus_problem(n: int, k: int) -> int:
    if n == 1:
        return 1

    return 1 + (josephus_problem(n - 1, k) + k - 1) % n


def josephus_problem_2(n: int) -> int:
    """
    J(2^m + l, 2) = 2 * l + 1
    """
    m = int(math.log2(n))
    pow_m = pow(2, m)
    return 2 * (n - pow_m) + 1


if __name__ == "__main__":
    assert josephus_problem(5, 2) == 3
    assert josephus_problem(1, 3) == 1
    assert josephus_problem(2, 3) == 2
    assert josephus_problem(3, 3) == 2
    assert josephus_problem(4, 3) == 1
    assert josephus_problem(5, 3) == 4
    assert josephus_problem_2(1) == 1
    assert josephus_problem_2(2) == 1
    assert josephus_problem_2(3) == 3
    assert josephus_problem_2(4) == 1
    assert josephus_problem_2(5) == 3
    assert josephus_problem_2(6) == 5
    assert josephus_problem_2(7) == 7
    assert josephus_problem_2(33) == 3
    assert josephus_problem_2(130) == 5
