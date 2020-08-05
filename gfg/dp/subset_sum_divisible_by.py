"""
Given a set of non-negative distinct integers, and a value m,
determine if there is a subset of the given set with sum divisible by m.
"""
from typing import List


def subset_sum_divisible_back_track(numbers: List[int], m: int) -> bool:
    """
    backtracking. O(2^n)
    """

    def back_track(total: int, index: int, size: int) -> bool:
        if (w := (total > 0 and total % m == 0) is True) or index == size:
            return w

        # take current or leave current
        return (back_track(total + numbers[index], index + 1, size) or
                back_track(total, index + 1, size))

    if not numbers:
        return False
    if m == 1:
        return True

    return back_track(0, 0, len(numbers))


def sub_set_sum_divisible_dp(numbers: List[int], m: int) -> bool:
    """
    DP
    """
    # TODO


if __name__ == "__main__":
    assert subset_sum_divisible_back_track([3, 1, 7, 5], 6) is True
    assert subset_sum_divisible_back_track([1, 6], 5) is False
