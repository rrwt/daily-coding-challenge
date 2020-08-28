"""
Given a list of numbers L, implement a method sum(i, j)
which returns the sum from the sublist L[i:j] (including i, excluding j).

For example,
    given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.

You can assume that you can do some pre-processing.
sum() should be optimized over the pre-processing step.
"""
from typing import List


class SumList:
    def __init__(self, lst: List[int]) -> None:
        self.lst = lst
        self.size = len(lst)
        self.left_sum = self._get_left_sum()
        self.left_sum.append(self.left_sum[-1] + lst[-1])

    def _get_left_sum(self) -> List[int]:
        left_sum = [0] * self.size

        for i in range(1, self.size):
            left_sum[i] = left_sum[i - 1] + self.lst[i - 1]

        return left_sum

    def sum(self, left_index: int, right_index: int) -> int:
        if left_index < 0:
            left_index = 0
        if right_index > self.size:
            right_index = self.size

        return self.left_sum[right_index] - self.left_sum[left_index]


if __name__ == "__main__":
    sl = SumList([1, 2, 3, 4, 5])
    assert sl.sum(1, 3) == 5
    assert sl.sum(-1, 100) == 15
