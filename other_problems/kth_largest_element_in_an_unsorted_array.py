"""
Given an unsorted array of integers and a number k < size(array),
find the kth largest integer in the array
"""
import sys
from typing import List
import heapq


def left_child_index(index: int) -> int:
    return 1 + (index << 1)


def right_child_index(index: int) -> int:
    return 2 + (index << 1)


class MinHeap:

    def __init__(self, array: List[int]) -> None:
        self.heap = array
        self.size = len(self.heap)
        self.temp_val = sys.maxsize

    def heapify(self, index) -> None:
        while index < self.size:
            left_index = left_child_index(index)
            right_index = right_child_index(index)

            min_index = index

            if left_index < self.size and self.heap[min_index] > self.heap[left_index]:
                min_index = left_index
            if right_index < self.size and self.heap[min_index] > self.heap[right_index]:
                min_index = right_index

            if min_index == index:
                break
            else:
                self.heap[min_index], self.heap[index] = self.heap[index], self.heap[min_index]
                index = min_index

    def remove_element(self) -> int:
        return_value = self.heap[0]
        self.heap[0] = self.temp_val
        self.heapify(0)
        self.size -= 1
        return return_value


def kth_largest_element_min_heap(array: List[int], k: int) -> int:
    # create a min heap of first k elements
    heap = MinHeap(array[:k])

    for index in range(k//2, -1, -1):
        heap.heapify(index)

    # for each of the remaining elements, if found greater than min,
    # replace and heapify
    for element in array[k:]:
        if element > heap.heap[0]:
            heap.heap[0] = element
            heap.heapify(0)

    # return the top element. it's the kth largest element
    return heap.remove_element()


class MaxHeap(MinHeap):

    def __init__(self, array: List[int]) -> None:
        super().__init__(array)
        self.temp_val = -sys.maxsize

    def heapify(self, index) -> None:
        while index < self.size:
            left_index = left_child_index(index)
            right_index = right_child_index(index)

            max_index = index

            if left_index < self.size and self.heap[max_index] < self.heap[left_index]:
                max_index = left_index
            if right_index < self.size and self.heap[max_index] < self.heap[right_index]:
                max_index = right_index

            if max_index == index:
                break
            else:
                self.heap[max_index], self.heap[index] = self.heap[index], self.heap[max_index]
                index = max_index


def kth_largest_element_max_heap(array: List[int], k: int) -> int:
    heap = MaxHeap(array)

    for index in range(len(array) // 2, -1, -1):
        heap.heapify(index)

    for _ in range(k-1):
        heap.remove_element()

    return heap.remove_element()


def kth_largest_element_inbuilt_heap(array: List[int], k: int) -> int:
    heapq.heapify(array)

    for _ in range(len(array) - k):
        heapq.heappop(array)

    return heapq.heappop(array)


if __name__ == "__main__":
    assert kth_largest_element_min_heap([11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45], 3) == 50
    assert kth_largest_element_max_heap([11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45], 3) == 50
    assert kth_largest_element_inbuilt_heap([11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45], 3) == 50
