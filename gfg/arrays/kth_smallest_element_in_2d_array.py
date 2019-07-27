"""
Given an n x n matrix, where every row and column is sorted in non-decreasing order.
Find the kth smallest element in the given 2D array.
For example, consider the following 2D array.
        10, 20, 30, 40
        15, 25, 35, 45
        24, 29, 37, 48
        32, 33, 39, 50
The 3rd smallest element is 20 and 7th smallest element is 30
"""
import sys
from copy import deepcopy
from typing import Optional


def parent_index(index: int) -> int:
    return int((index - 1) / 2)


def left_child_index(index: int) -> int:
    return 2 * index + 1


def right_child_index(index: int) -> int:
    return 2 * (index + 1)


class KthSmallestMinHeap:
    """
    1) Build a min heap of elements from first row.
       A heap entry also stores row number and column number.
    2) Do following k times.
       …a) Get minimum element (or root) from min heap.
       …b) Find row number and column number of the minimum element.
       …c) Replace root with the next element from same column and min-heapify the root.
    3) Return the last extracted root.
    """

    def __init__(self, arr: list) -> None:
        self.dim = len(arr)
        self.arr = deepcopy(arr)
        self.heap: list = []

    def _heapify(self, index: int):
        while index < self.dim:
            left, right = left_child_index(index), right_child_index(index)
            min_index = index

            if left < self.dim and self.heap[left][0] < self.heap[min_index][0]:
                min_index = left
            if right < self.dim and self.heap[right][0] < self.heap[min_index][0]:
                min_index = right

            if index != min_index:
                self.heap[index], self.heap[min_index] = (
                    self.heap[min_index],
                    self.heap[index],
                )
                index = min_index
            else:
                break

    def _extract_replace_element(self) -> int:
        element, x, y = self.heap[0]

        if x + 1 < self.dim:
            self.heap[0] = self.arr[x + 1][y], x + 1, y
        else:
            self.heap[0] = sys.maxsize, x + 1, y

        self._heapify(0)
        return element

    def kth_element(self, k: int) -> int:
        self.heap = []

        for index in range(self.dim):
            self.heap.append((self.arr[0][index], 0, index))

        for i in range(self.dim - 1, -1, -1):
            self._heapify(i)

        for i in range(k - 1):
            self._extract_replace_element()

        return self.heap[0][0]


if __name__ == "__main__":
    arr: list = [[10, 20, 30, 40], [15, 25, 35, 45], [24, 29, 37, 48], [32, 33, 39, 50]]
    kth = KthSmallestMinHeap(arr)
    assert kth.kth_element(3) == 20
    assert kth.kth_element(7) == 30
