"""
Given an array and a number k where k is smaller than size of array,
we need to find the k’th smallest element in the given array.
It is given that ll array elements are distinct.
"""
from copy import deepcopy


def parent_index(index: int) -> int:
    return int((index - 1) / 2)


def left_child_index(index: int) -> int:
    return 2 * index + 1


def right_child_index(index: int) -> int:
    return 2 * (index + 1)


class KthSmallestMinHeap:
    """
    A min heap can be built to get the value fast.
    O(n) to build the heap and log(n) per element to extract the element.
    Time Complexity: O(n+klog(n))
    Space Complexity: O(1)  # using same array as min heap
    """

    def __init__(self, arr: list) -> None:
        self.len: int = len(arr)
        self.arr: list = deepcopy(arr)

    def heapify(self, index: int, end: int = -1):
        """
        Construct a min heap for the current subtree
        for n nodes, time complexity is O(n).
        It seems to be O(nlogn) but it has mathematically been proven to be O(n)
        """
        if end == -1:
            end = self.len - 1

        while index < end:
            left, right = left_child_index(index), right_child_index(index)
            smallest: int = index

            if left <= end and self.arr[left] < self.arr[smallest]:
                smallest = left
            if right <= end and self.arr[right] < self.arr[smallest]:
                smallest = right

            if smallest != index:
                self.arr[index], self.arr[smallest] = (
                    self.arr[smallest],
                    self.arr[index],
                )
                index = smallest
            else:
                break

    def extract_min(self, end: int) -> int:
        """
        Extract the smallest element from the heap
        Time Complexity: O(log(n))  (k*log(n) for k elements)
        """
        self.arr[0], self.arr[end] = self.arr[end], self.arr[0]
        self.heapify(0, end - 1)
        return self.arr[end]

    def get_kth_smallest_element(self, k: int) -> int:
        for index in range(self.len - 1, -1, -1):
            self.heapify(index)

        for index in range(k - 1):
            self.extract_min(self.len - 1 - index)

        return self.arr[0]


class KthSmallestMaxHeap:
    """
    We can build a max heap of first k elements.
    Afterwards we can compare the topmost element with incoming elements.
    If it is less than root, then make it root and heapify, else ignore it.
    After all the elements are processed, the heap's root is our solution.
    """

    def __init__(self, arr: list) -> None:
        self.len = len(arr)
        self.arr = deepcopy(arr)

    def heapify(self, index: int, end: int = -1):
        """
        Time complexity: O(k) for k elements
        """
        while index < end:
            left, right = left_child_index(index), right_child_index(index)
            max_index: int = index

            if left <= end and self.arr[left] > self.arr[max_index]:
                max_index = left
            if right <= end and self.arr[right] > self.arr[max_index]:
                max_index = right

            if max_index != index:
                self.arr[index], self.arr[max_index] = (
                    self.arr[max_index],
                    self.arr[index],
                )
            else:
                break

    def add_element(self, element: int, end: int = -1):
        """
        We only want to keep the smallest k elements in max heap
        Time Complexity: O((n-k)log(k))
        """
        if element < self.arr[0]:
            self.arr[0] = element
            self.heapify(0, end)

    def kth_element_max_heap(self, k: int) -> int:
        for index in range(k - 1, -1, -1):
            self.heapify(index, k - 1)

        for index in range(k, self.len):
            self.add_element(self.arr[index], k)

        return self.arr[0]


if __name__ == "__main__":
    arr: list = [7, 10, 4, 3, 20, 15]
    kth_min = KthSmallestMinHeap(arr)
    assert kth_min.get_kth_smallest_element(3) == 7
    kth_min = KthSmallestMinHeap(arr)
    assert kth_min.get_kth_smallest_element(4) == 10

    kth_max = KthSmallestMaxHeap(arr)
    assert kth_max.kth_element_max_heap(3) == 7
    kth_max = KthSmallestMaxHeap(arr)
    assert kth_max.kth_element_max_heap(4) == 10
