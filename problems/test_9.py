"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5]
should return 10, since we pick 5 and 5.
"""
import pytest

from problems.problem_9 import largest_non_adjacent_sum


class TestLargestSum:
    def test_empty_list_should_return_null(self):
        assert largest_non_adjacent_sum([]) is None

    @pytest.mark.parametrize("input_list,expected", [
        ([1], 1), ([2], 2), ([3], 3), ([-10], -10), ([-20], -20), ([40], 40)
    ])
    def test_list_with_one_integer_should_return_the_integer(self, input_list, expected):
        assert largest_non_adjacent_sum(input_list) == expected

    @pytest.mark.parametrize("given_input,expected", [
        ([1, 2], 2), ([5, -1], 5), ([10, 15], 15), ([30, 12], 30)
    ])
    def test_list_with_two_integers_should_return_the_higher_value(self, given_input, expected):
        assert largest_non_adjacent_sum(given_input) == expected
