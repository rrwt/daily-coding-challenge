"""
Given that integers are read from a data stream. Find median of elements read
so for in efficient way. For simplicity assume there are no duplicates.
Making it clear, when the input size is odd, we take the middle element of sorted data.
If the input size is even, we pick average of middle two elements in sorted stream.
Note that output is effective median of integers read from the stream so far.
Such an algorithm is called online algorithm. Any algorithm that can guarantee output
of i-elements after processing i-th element, is said to be online algorithm.
"""
from typing import Union
import heapq


class RunningMedian:
    """A class to get running medians
        Create a min and a max heap.
        The min heap will contain the largest 50% of the elements so far.
        The max heap will contain the smallest 50% of the elements so far.
        If one of the heap contains more elements, it's top element becomes the median,
        else, the mean of two top elements becomes the median.
        Since python only has min heaps, max heap can be implemented as min heap with -ve
        values.

        Note: Only positive values are allowed
    """

    def __init__(self):
        self.min_heap: list = []
        self.len_min: int = 0
        self.max_heap: list = []
        self.len_max: int = 0

    def median(self) -> Union[float, int, None]:
        if self.len_max > self.len_min:
            return self.max_heap[0]
        elif self.len_max < self.len_min:
            return self.min_heap[0]
        else:
            try:
                return (self.min_heap[0] + abs(self.max_heap[0])) / 2
            except IndexError:
                print("No elements found")

        return None

    def running_median(self, value: int) -> Union[int, float, None]:
        """
        Time Complexity: O(log(n))
        """
        if self.len_min <= self.len_max:
            if self.max_heap and value < abs(self.max_heap[0]):
                value = abs(heapq.heappushpop(self.max_heap, -value))

            heapq.heappush(self.min_heap, value)
            self.len_min += 1
        else:
            if value > self.min_heap[0]:
                value = heapq.heappushpop(self.min_heap, value)
            heapq.heappush(self.max_heap, -value)
            self.len_max += 1

        return self.median()


if __name__ == "__main__":
    arr: list = [5, 15, 1, 3]
    sol: list = [5, 10, 5, 4]
    rm = RunningMedian()

    for el, s in zip(arr, sol):
        assert rm.running_median(el) == s
