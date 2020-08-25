"""
You have a large array with most of the elements as zero
Use a more space-efficient data structure, SparseArray, that implements the same interface:
    init(arr, size): initialize with the original large array and size.
    set(i, val): updates index at i with val.
    get(i): gets the value at index i.
"""
from collections import defaultdict


class SparseArray:
    def __init__(self, size: int) -> None:
        self.arr = defaultdict(int)
        self.size = size

    @staticmethod
    def init(arr: list, size: int) -> "SparseArray":
        sa = SparseArray(size)

        for index, value in enumerate(arr):
            if value > 0:
                sa.arr[index] = value

        return sa

    def set(self, index: int, val: int) -> None:
        if -1 < index < self.size:
            self.arr[index] = val
        else:
            raise IndexError("list index out of range")

    def get(self, index: int) -> int:
        if -1 < index < self.size:
            return self.arr[index]
        else:
            raise IndexError("list index out of range")


if __name__ == "__main__":
    sp_arr = SparseArray.init([1, 0, 0, 3, 2, 0, 0, 0, 5], 9)
    sp_arr.set(2, 15)
    assert sp_arr.get(0) == 1
    assert sp_arr.get(8) == 5
