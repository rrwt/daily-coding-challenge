"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""
import pytest

from one import verify_sum, verify_sum_2


class TestSum:
    def test_only_two_numbers(self):
        assert verify_sum([1, 2], 3) == True
        assert verify_sum([3, 4], 5) == False
    
    @pytest.mark.parametrize("arr,k,expected",
        [([1, 1, 1],2,True),
         ([2, 3, 4], 6, True),
         ([2, 3, 4], 8, False)
        ],
    )
    def test_three_numbers(self, arr, k, expected):
        assert verify_sum(arr, k) == expected


class TestSum2:
    def test_only_two_numbers(self):
        assert verify_sum_2([1, 2], 3) == True
        assert verify_sum_2([3, 4], 5) == False
    
    @pytest.mark.parametrize("arr,k,expected",
        [([1, 1, 1],2,True),
         ([2, 3, 4], 6, True),
         ([2, 3, 4], 8, False)
        ],
    )
    def test_three_numbers(self, arr, k, expected):
        assert verify_sum_2(arr, k) == expected
