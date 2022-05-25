"""
Compute the running median of a sequence of numbers. That is,
given a stream of numbers, print out the median of the list so far on each new element.
Recall that the median of an even-numbered list is the average of the two middle numbers.
For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
2 1.5 2 3.5 2 2 2
"""
from typing import List, Union
import heapq


def running_median_fast(array: List[int]) -> List[Union[float, int]]:
    """
    Divide the array in two parts.
    1. Max heap with n/2 small elements.
    2. Min heap with n/2 large elements.

    The median would always be one of:
    1. top of max heap if its element count is greater than that of min heap
    2. top of min heap if its element count is greater than that of max heap
    3. avg of top of min heap and max heap.
    """
    min_heap = []
    max_heap = []
    size_max_heap = 0
    size_min_heap = 0
    medians = []

    for i, el in enumerate(array):
        if not max_heap or -max_heap[0] >= el:
            heapq.heappush(max_heap, -el)
            size_max_heap += 1
        else:
            heapq.heappush(min_heap, el)
            size_min_heap += 1

        while size_min_heap > size_max_heap + 1:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
            size_min_heap -= 1
            size_max_heap += 1

        while size_max_heap > size_min_heap + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
            size_min_heap += 1
            size_max_heap -= 1

        if size_min_heap > size_max_heap:
            medians.append(min_heap[0])
        elif size_max_heap > size_min_heap:
            medians.append(-max_heap[0])
        else:
            medians.append((min_heap[0] - max_heap[0]) / 2)

    return medians


def running_median() -> float:
    count_num = 0
    index_med = -1
    median = None
    arr = []

    while (num := (yield median)) is not None:
        arr.append(num)
        arr.sort()
        count_num += 1

        if count_num & 1:
            index_med += 1
            median = arr[index_med]
        else:
            median = (arr[index_med] + arr[index_med + 1]) / 2


if __name__ == "__main__":
    rm = running_median()
    rm.send(None)  # To put the generator in active state. alt: next(rm)
    for _ in [2, 1, 5, 7, 2, 0, 5]:
        try:
            print(rm.send(_))
        except StopIteration:
            break

    print(running_median_fast([2, 1, 5, 7, 2, 0, 5]))
