"""
Given an array of integers, find the first missing positive integer in linear time and constant
space. In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.
"""
import pytest

from .problem_4 import (
    first_missing_positive_integer,
    first_missing_positive_integer_using_on_extra_space
)


class TestFindFirstMissingPositiveInteger:
    def test_given_zero_should_return_one(self):
        assert first_missing_positive_integer([0]) == 1

    def test_given_one_should_return_two(self):
        assert first_missing_positive_integer([1]) == 2

    def test_given_two_should_return_one(self):
        assert first_missing_positive_integer([2]) == 1

    @pytest.mark.parametrize("input_arr,expected_output", [
        ([1, 2, 3, 4, 6], 5),
        ([3, 4, -1, 1], 2),
        ([1, 2, 0], 3)
    ])
    def test_given_array_return_first_positive_integer(self, input_arr, expected_output):
        assert first_missing_positive_integer(input_arr) == expected_output


class TestFindFirstMissingPositiveIntegerWithOnExtraSpace:
    def test_given_zero_should_return_one(self):
        assert first_missing_positive_integer_using_on_extra_space([0]) == 1

    def test_given_one_should_return_two(self):
        assert first_missing_positive_integer_using_on_extra_space([1]) == 2

    def test_given_two_should_return_one(self):
        assert first_missing_positive_integer_using_on_extra_space([2]) == 1

    @pytest.mark.parametrize("input_arr,expected_output", [
        ([1, 2, 3, 4, 6], 5),
        ([3, 4, -1, 1], 2),
        ([1, 2, 0], 3)
    ])
    def test_given_array_return_first_positive_integer(self, input_arr, expected_output):
        assert first_missing_positive_integer_using_on_extra_space(input_arr) == expected_output
