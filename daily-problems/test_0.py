"""
return a new sorted merged list from K sorted lists, each with size N
"""
import pytest

from .problem_0 import (
    merge_sorted_lists,
    merge_sorted_lists_min_heap,
    merge_sorted_merge_sort_algorithm,
)


class TestMergeKSortedList:
    def test_given_two_lists_with_same_elements_each_returns_a_list_of_two_elements(
        self
    ):
        assert merge_sorted_lists([[1], [1]]) == [1, 1]

    def test_given_two_lists_with_two_different_elements_returns_a_sorted_list(self):
        assert merge_sorted_lists([[1], [2]]) == [1, 2]

    @pytest.mark.parametrize(
        "input_lists,expected_output",
        [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
            ([[20, 25, 30], [10, 15, 22]], [10, 15, 20, 22, 25, 30]),
        ],
    )
    def test_given_k_lists_returns_a_sorted_list(self, input_lists, expected_output):
        assert merge_sorted_lists(input_lists) == expected_output


class TestMergeKSortedListUsingMinHeap:
    def test_given_two_lists_with_same_elements_each_returns_a_list_of_two_elements(
        self
    ):
        assert merge_sorted_lists_min_heap([[1], [1]]) == [1, 1]

    def test_given_two_lists_with_two_different_elements_returns_a_sorted_list(self):
        assert merge_sorted_lists_min_heap([[1], [2]]) == [1, 2]

    @pytest.mark.parametrize(
        "input_lists,expected_output",
        [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
            ([[20, 25, 30], [10, 15, 22]], [10, 15, 20, 22, 25, 30]),
        ],
    )
    def test_given_k_lists_returns_a_sorted_list(self, input_lists, expected_output):
        assert merge_sorted_lists_min_heap(input_lists) == expected_output


class TestMergeKSortedListUsingMergeSort:
    def test_given_two_lists_with_same_elements_each_returns_a_list_of_two_elements(
        self
    ):
        assert merge_sorted_merge_sort_algorithm([[1], [1]]) == [1, 1]

    def test_given_two_lists_with_two_different_elements_returns_a_sorted_list(self):
        assert merge_sorted_merge_sort_algorithm([[1], [2]]) == [1, 2]

    @pytest.mark.parametrize(
        "input_lists,expected_output",
        [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
            ([[20, 25, 30], [10, 15, 22]], [10, 15, 20, 22, 25, 30]),
        ],
    )
    def test_given_k_lists_returns_a_sorted_list(self, input_lists, expected_output):
        assert merge_sorted_merge_sort_algorithm(input_lists) == expected_output
