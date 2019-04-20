"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways
it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
"""
import pytest

from problems.problem_7 import count_mapping


class TestCountMapping:
    def test_zero_returns_none(self):
        assert count_mapping('0') == None

    @pytest.mark.parametrize("input_str", [
        ('1',), ('2',), ('3',), ('4',), ('5',), ('1',), ('1',), ('1',), ('1',)
    ])
    def test_single_digit_returns_one(self, input_str):
        assert count_mapping(input_str) == 1

    def test_given_ten_twenty_returns_one(self):
        assert count_mapping('10') == 1
        assert count_mapping('20') == 1
