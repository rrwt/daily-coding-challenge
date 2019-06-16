"""
A binary heap can be a minheap or a maxheap.
Following are some standard operations on minheap.
    1. get_min(): O(1). Get the smallest element
    2. extract_min(): O(log(n)). Pop the min element out.
    3. update_value(): O(log(n)). Update the value of a node
    4. insert/delete(): O(log(n))
    5. min_heapify(): O(log(n)). Heapify a node in the tree
"""
from typing import Optional


class MinHeap:
    def __init__(self):
        self.arr: list = []
        self.size = 0

    def parent_index(self, index: int) -> int:
        return int((index - 1) / 2)

    def right_child_index(self, index: int) -> int:
        return 2 * (index + 1)

    def left_child_index(self, index: int) -> int:
        return 2 * index + 1

    def exchange_nodes(self, index_1, index_2):
        self.arr[index_1], self.arr[index_2] = self.arr[index_2], self.arr[index_1]

    def move_up(self, index):
        """
        time complexity: O(log(n))
        """
        while index >= 1:
            parent_index = self.parent_index(index)

            if self.arr[index] >= self.arr[parent_index]:
                break

            self.exchange_nodes(index, parent_index)
            index = parent_index

    def min_heapify(self, index):
        """
        Heapify single node of an already heapified tree
        time complexity: O(log(n))
        """
        while index < self.size - 1:
            left_child_index = self.left_child_index(index)
            right_child_index = self.right_child_index(index)

            temp = index

            if (
                self.size > left_child_index
                and self.arr[left_child_index] < self.arr[index]
            ):
                temp = left_child_index
            if (
                self.size > right_child_index
                and self.arr[right_child_index] < self.arr[temp]
            ):
                temp = right_child_index

            if temp == index:
                break

            self.exchange_nodes(index, temp)
            index = temp

    def get_min(self) -> Optional[int]:
        return self.arr[0] if self.arr else None

    def insert(self, data: int):
        self.arr.append(data)
        self.size += 1
        self.move_up(self.size - 1)

    def extract_min(self) -> Optional[int]:
        data = self.get_min()

        if data is not None:
            self.arr[0] = self.arr[self.size - 1]
            self.min_heapify(0)
            self.size -= 1
        return data

    def update_value(self, index, new_value: int):
        if self.size <= index or index < 0:
            raise AssertionError("Invalid index")

        previous_value = self.arr[index]
        self.arr[index] = new_value

        if new_value < previous_value:
            self.move_up(index)
        elif new_value > previous_value:
            self.min_heapify(index)

    def delete(self, index: int):
        if index >= self.size or index < 0:
            raise AssertionError("Invalid index")

        self.arr[index] = -10 ** 10
        self.move_up(index)
        self.extract_min()


if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap.insert(3)
    min_heap.insert(2)
    min_heap.delete(1)
    min_heap.insert(15)
    min_heap.insert(5)
    min_heap.insert(4)
    min_heap.insert(45)

    print("heap", min_heap.arr)
    print("extract min:", min_heap.extract_min())
    print("get min:", min_heap.get_min())
    min_heap.update_value(2, 1)
    print("get min", min_heap.get_min())
    print("heap", min_heap.arr)
