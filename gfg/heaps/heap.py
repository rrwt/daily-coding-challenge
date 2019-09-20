"""
Implement Min and Max Heap
"""


def parent_index(index) -> int:
    return (index - 1) >> 1


def left_index(index) -> int:
    return (index << 1) + 1


def right_index(index) -> int:
    return 2 * (index << 1)


class MinHeap:
    def __init__(self, max_size: int = 20):
        self._heap = [None] * max_size
        self._size = 0
        self._max_size = max_size

    def get_min(self):
        """
        Get minimum valued element from the heap
        Time Complexity: O(1)
        """
        return self._heap[0]

    def _push_down(self, index: int):
        left = left_index(index)
        min_index = index

        while left < self._size:
            if self._heap[left] < self._heap[min_index]:
                min_index = left

            right = right_index(index)

            if right < self._size and self._heap[right] < self._heap[min_index]:
                min_index = right

            if min_index == index:
                break
            else:
                self._heap[min_index], self._heap[index] = (
                    self._heap[index],
                    self._heap[min_index],
                )
                index = min_index
                left = left_index(index)

    def _bubble_up(self, index: int):
        while index > 0:
            parent = parent_index(index)

            if self._heap[parent] > self._heap[index]:
                self._heap[parent], self._heap[index] = (
                    self._heap[index],
                    self._heap[parent],
                )
                index = parent
            else:
                break

    def extract_min(self):
        """
        Extract minimum valued element from the heap
        Time Complexity: O(log(n))
        """
        if self._size < 1:
            raise AssertionError("Heap underflow")

        return_value = self._heap[0]
        self._heap[0] = self._heap[self._size - 1]
        self._heap[self._size - 1] = None
        self._size -= 1
        self._push_down(0)
        return return_value

    def decrease_key(self, key: int, new_value: int):
        """
        Decrease the value of a key to a new value
        Time Complexity: O(log(n))
        """
        if self._heap[key] < new_value:
            raise AssertionError("New value is larger than the old one")

        self._heap[key] = new_value
        self._bubble_up(key)

    def insert_value(self, value: int):
        """
        Insert a new value to the heap
        Time Complexity: O(log(n))
        """
        if self._size >= self._max_size - 1:
            raise AssertionError("Heap Overflow")

        self._heap[self._size] = value
        self._bubble_up(self._size)
        self._size += 1

    def delete(self, key: int) -> int:
        """
        Delete a key
        Time Complexity: O(log(n))
        """
        return_value = self._heap[key]
        self.decrease_key(key, -1_000_000)
        self.extract_min()
        return return_value


class MaxHeap:
    def __init__(self, max_size: int = 20):
        self._heap = [None] * max_size
        self._size = 0
        self._max_size = max_size

    def get_max(self):
        """
        Get maximum valued element from the heap
        Time Complexity: O(1)
        """
        return self._heap[0]

    def _push_down(self, index: int):
        left = left_index(index)
        max_index = index

        while left < self._size:
            if self._heap[left] > self._heap[max_index]:
                max_index = left

            right = right_index(index)

            if right < self._size and self._heap[right] > self._heap[max_index]:
                max_index = right

            if max_index == index:
                break
            else:
                self._heap[max_index], self._heap[index] = (
                    self._heap[index],
                    self._heap[max_index],
                )
                index = max_index
                left = left_index(index)

    def _bubble_up(self, index: int):
        while index > 0:
            parent = parent_index(index)

            if self._heap[parent] < self._heap[index]:
                self._heap[parent], self._heap[index] = (
                    self._heap[index],
                    self._heap[parent],
                )
                index = parent
            else:
                break

    def extract_max(self):
        """
        Extract maximum valued element from the heap
        Time Complexity: O(log(n))
        """
        if self._size < 1:
            raise AssertionError("Heap underflow")

        return_value = self._heap[0]
        self._heap[0] = self._heap[self._size - 1]
        self._heap[self._size - 1] = None
        self._size -= 1
        self._push_down(0)
        return return_value

    def increase_key(self, key: int, new_value: int):
        """
        Increase the value of a key to a new value
        Time Complexity: O(log(n))
        """
        if self._heap[key] > new_value:
            raise AssertionError("New value is larger than the old one")

        self._heap[key] = new_value
        self._bubble_up(key)

    def insert_value(self, value: int):
        """
        Insert a new value to the heap
        Time Complexity: O(log(n))
        """
        if self._size >= self._max_size - 1:
            raise AssertionError("Heap Overflow")

        self._heap[self._size] = value
        self._bubble_up(self._size)
        self._size += 1

    def delete(self, key: int) -> int:
        """
        Delete a key
        Time Complexity: O(log(n))
        """
        return_value = self._heap[key]
        self.increase_key(key, 1_000_000)
        self.extract_max()
        return return_value


if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap.insert_value(3)
    min_heap.insert_value(2)
    min_heap.delete(1)
    min_heap.insert_value(15)
    min_heap.insert_value(5)
    min_heap.insert_value(4)
    min_heap.insert_value(45)

    print(min_heap.extract_min())
    print(min_heap.get_min())
    min_heap.decrease_key(2, 1)
    print(min_heap.get_min())
