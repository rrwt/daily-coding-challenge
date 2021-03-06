"""
Given that integers are being read from a data stream.
Find median of all the elements read so far starting from the first integer
till the last integer. This is also called Median of Running Integers.
The data stream can be any source of data,
example: a file, an array of integers, input stream etc.
"""
import sys
from typing import Union
from heapq import heappushpop, heappush

from kth_smallest_element import left_child_index, parent_index  # type: ignore


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
        self.max_heap: list = []
        self.max_heap_size: int = 0
        self.min_heap: list = []
        self.min_heap_size: int = 0
        self.current_median: Union[float, int] = 0

    def min_heapify_top_down(self, index: int = 0) -> None:
        """
        Time Complexity: O(log(n))
        """
        left = left_child_index(index)
        element: int = self.min_heap[index]

        while left < self.max_heap_size:
            right = left + 1
            min_index = index

            if self.min_heap[left] < self.min_heap[min_index]:
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
                left = left_child_index(index)
            else:
                break

        self.min_heap[index] = element

    def min_heapify_bottom_up(self, index: int = -1) -> None:
        """
        Time Complexity: O(log(n))
        """
        if index == -1:
            index = self.min_heap_size - 1

        element: int = self.min_heap[index]

        while index > 0:
            parent = parent_index(index)

            if self.min_heap[parent] > element:
                self.min_heap[index] = self.min_heap[parent]
                index = parent
            else:
                break

        self.min_heap[index] = element

    def _add_to_min_heap(self, element: int):
        self.min_heap_size += 1
        self.min_heap.append(element)
        self.min_heapify_bottom_up()

    def max_heapify_top_down(self, index: int = 0) -> None:
        """
        Time Complexity: O(log(n))
        """
        left = left_child_index(index)
        element: int = self.max_heap[index]

        while left < self.max_heap_size:
            right = left + 1
            max_index = index

            if self.max_heap[left] > self.max_heap[max_index]:
                max_index = left
            if (
                right < self.max_heap_size
                and self.max_heap[right] > self.max_heap[max_index]
            ):
                max_index = right

            if index != max_index:
                self.max_heap[index] = self.max_heap[max_index]
                index = max_index
                left = left_child_index(index)
            else:
                break

        self.max_heap[index] = element

    def max_heapify_bottom_up(self, index: int = -1) -> None:
        """
        Time Complexity: O(log(n))
        """
        if index == -1:
            index = self.max_heap_size - 1

        element: int = self.max_heap[index]

        while index > 0:
            parent = parent_index(index)

            if self.max_heap[parent] < element:
                self.max_heap[index] = self.max_heap[parent]
                index = parent
            else:
                break

        self.max_heap[index] = element

    def _add_to_max_heap(self, element: int):
        self.max_heap_size += 1
        self.max_heap.append(element)
        self.max_heapify_bottom_up()

    def _set_median(self):
        """
        Time Complexity: O(1)
        """
        if self.max_heap_size == self.min_heap_size:
            self.current_median = (self.max_heap[0] + self.min_heap[0]) / 2
        elif self.max_heap_size < self.min_heap_size:
            self.current_median = self.min_heap[0]
        else:
            self.current_median = self.max_heap[0]

    def get_median(self, new_element: int) -> Union[float, int]:
        if self.max_heap_size > self.min_heap_size:
            if new_element > self.current_median:
                self._add_to_min_heap(new_element)
            else:
                self._add_to_min_heap(self.max_heap[0])
                self.max_heap[0] = new_element
                self.max_heapify_top_down()

        elif self.max_heap_size == self.min_heap_size:
            if new_element > self.current_median:
                self._add_to_min_heap(new_element)
            else:
                self._add_to_max_heap(new_element)
        else:
            if new_element > self.current_median:
                self._add_to_max_heap(self.min_heap[0])
                self.min_heap[0] = new_element
                self.min_heapify_top_down()
            else:
                self._add_to_max_heap(new_element)

        self._set_median()
        return self.current_median


class RunningMedianUsingInbuiltHeapq:
    def __init__(self):
        self.min_heap, self.max_heap = [], []

    def add_num(self, num: int) -> None:
        """
        The negative signs are to represent a max heap using min heap
        """
        if len(self.min_heap) == len(self.max_heap):
            heappush(self.max_heap, -heappushpop(self.min_heap, -num))
        else:
            heappush(self.min_heap, -heappushpop(self.max_heap, num))

    def find_median(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return float(self.max_heap[0])
        return (self.max_heap[0] - self.min_heap[0]) / 2.0


if __name__ == "__main__":
    matrix: list = [
        [5, 15, 10, 20, 3],
        [2, 1, 5, 7, 2, 0, 5],
        list(range(1, 11)),
        list(range(-1, -6, -1)),
        [6, 10, 2, 6, 5, 0, 6, 3, 1, 0, 0],
    ]

    for arr in matrix:
        print("current array:", arr)
        run_med = RunningMedian()

        for element in arr:
            print(run_med.get_median(element))

    print("method 2")

    for arr in matrix:
        print("current array:", arr)
        run_med = RunningMedianUsingInbuiltHeapq()

        for element in arr:
            run_med.add_num(element)
            print(run_med.find_median())
