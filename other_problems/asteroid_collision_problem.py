"""
We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents
its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet,
the smaller one will explode. If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet.
"""
from typing import List


def asteroid_collision(asteroids: List[int]) -> List[int]:
    stack = []

    for val in asteroids:
        if not stack or stack[-1] < 0 or (stack[-1] > 0 and val > 0):
            stack.append(val)
        elif val < 0 < stack[-1]:
            while stack and 0 < stack[-1] < abs(val):
                stack.pop()

            if stack and stack[-1] == abs(val):
                stack.pop()
            elif not stack or stack[-1] < 0:
                stack.append(val)

    return stack


if __name__ == "__main__":
    assert asteroid_collision([5, 10, -5]) == [5, 10]
    assert asteroid_collision([8, -8]) == []
    assert asteroid_collision([10, 2, -5]) == [10]
    assert asteroid_collision([-2, -1, 1, 2]) == [-2, -1, 1, 2]
    assert asteroid_collision([2, -1, 1, -2]) == []
    assert asteroid_collision([-2, 2, -1, 1]) == [-2, 2, 1]
    assert asteroid_collision([2, -1, 1, -2]) == []
    assert asteroid_collision([-2, 1, 1, -1]) == [-2, 1]
