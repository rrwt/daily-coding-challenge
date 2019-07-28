"""
Given that integers are being read from a data stream.
Find median of all the elements read so far starting from the first integer
till the last integer. This is also called Median of Running Integers.
The data stream can be any source of data,
example: a file, an array of integers, input stream etc.
"""
from typing import Union
from collections import deque

from kth_smallest_element import (
    parent_index,
    left_child_index,
    right_child_index,
)  # type: ignore


class RunningMedian:
    """
    1. Create two heaps.
        - One max heap to maintain elements of lower half and
        - One min heap to maintain elements of higher half.
    2. Take initial value of median as 0.
    3. For every newly read element:
        i. If both heaps have same size:
            - If new element is greater than the median, then insert the new element
                into min_heap and set median to the top of min heap.
            - Else, insert it in the max heap and set median to the top of max heap
        ii. If max heap has more elements:
            - If new element is greater than the median, then insert it in the min heap
                and set median to avg of top elements.
            - Else, insert top of max heap to min heap and new element to max heap and
                and set median to avg of top elements.
        iii. If min heap has more elements:
            - If new element is greater than the median, insert top of min heap to
                max heap and new element to min heap and set median to avg of top elements.
            - Else, insert it in the max heap and set median to avg of top elements.
    
    Time Complexity: O(n*log(n))
    Space Complexity: O(n)
    """

    def __init__(self):
        self.max_heap: deque = deque()
        self.max_heap_size: int = 0
        self.min_heap: deque = deque()
        self.min_heap_size: int = 0
        self.current_median: Union[float, int] = 0

    def min_heapify(self, index: int = 0) -> None:
        while index < self.max_heap_size:
            left, right = left_child_index(index), right_child_index(index)
            min_index = index

            if (
                left < self.min_heap_size
                and self.min_heap[left] < self.min_heap[min_index]
            ):
                min_index = left
            if (
                right < self.min_heap_size
                and self.min_heap[right] < self.min_heap[min_index]
            ):
                min_index = right

            if index != min_index:
                self.min_heap[index], self.min_heap[min_index] = (
                    self.min_heap[min_index],
                    self.min_heap[index],
                )
                index = min_index
            else:
                break

    def _add_to_min_heap(self, element: int):
        """
        Time Complexity: O(n)
        """
        self.min_heap_size += 1
        self.min_heap.append(element)
        self.min_heap[0], self.min_heap[-1] = self.min_heap[-1], self.min_heap[0]

        for i in range(self.min_heap_size - 1, -1, -1):
            self.min_heapify(i)

    def max_heapify(self, index: int = 0) -> None:
        while index < self.max_heap_size:
            left, right = left_child_index(index), right_child_index(index)
            max_index = index

            if (
                left < self.max_heap_size
                and self.max_heap[left] > self.max_heap[max_index]
            ):
                max_index = left
            if (
                right < self.max_heap_size
                and self.max_heap[right] > self.max_heap[max_index]
            ):
                max_index = right

            if index != max_index:
                self.max_heap[index], self.max_heap[max_index] = (
                    self.max_heap[max_index],
                    self.max_heap[index],
                )
                index = max_index
            else:
                break

    def _add_to_max_heap(self, element: int):
        """
        Time Complexity: O(n)
        """
        self.max_heap_size += 1
        self.max_heap.append(element)
        self.max_heap[0], self.max_heap[-1] = self.max_heap[-1], self.max_heap[0]

        for i in range(self.max_heap_size - 1, -1, -1):
            self.max_heapify(i)

    def _set_median(self):
        if self.max_heap_size == self.min_heap_size:
            self.current_median = (self.max_heap[0] + self.min_heap[0]) / 2
        elif self.max_heap_size < self.min_heap_size:
            self.current_median = self.min_heap[0]
        else:
            self.current_median = self.max_heap[0]

    def get_median(self, new_element: int = None) -> Union[float, int]:
        if new_element is not None:
            if self.max_heap_size > self.min_heap_size:
                if new_element > self.current_median:
                    self._add_to_min_heap(new_element)
                else:
                    self._add_to_min_heap(self.max_heap.popleft())
                    self.max_heap_size -= 1
                    self._add_to_max_heap(new_element)

            elif self.max_heap_size == self.min_heap_size:
                if new_element > self.current_median:
                    self._add_to_min_heap(new_element)
                else:
                    self._add_to_max_heap(new_element)
            else:
                if new_element > self.current_median:
                    self._add_to_max_heap(self.min_heap.popleft())
                    self.min_heap_size -= 1
                    self._add_to_min_heap(new_element)
                else:
                    self._add_to_max_heap(new_element)

            self._set_median()
        return self.current_median


if __name__ == "__main__":
    arr: list = [5, 15, 10, 20, 3]
    print(arr)
    run_med = RunningMedian()

    for element in arr:
        print(run_med.get_median(element))

    arr: list = [2, 1, 5, 7, 2, 0, 5]
    print(arr)
    run_med = RunningMedian()

    for element in arr:
        print(run_med.get_median(element))
