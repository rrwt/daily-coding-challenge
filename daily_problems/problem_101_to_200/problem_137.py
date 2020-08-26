"""
Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

    init(size): initialize the array with size
    set(i, val): updates index at i with val where val is either 1 or 0.
    get(i): gets the value at index i.
"""
from random import randint


class BitArray:
    def __init__(self, size: int) -> None:
        self.arr = set()
        self.size = size

    def set(self, index: int, val: int) -> None:
        assert val in (0, 1) and index < self.size
        if val == 0 and index in self.arr:
            self.arr.remove(index)
        elif val == 1:
            self.arr.add(index)

    def get(self, index: int) -> int:
        return int(index in self.arr)


if __name__ == "__main__":
    ba = BitArray(100)
    arr = [0] * 100

    for _ in range(50):
        ind = randint(0, 99)
        ba.set(ind, 1)
        arr[ind] = 1

    for _ in range(50):
        ind = randint(0, 99)
        ba.set(ind, 0)
        arr[ind] = 0

    print(arr)

    for _ in range(100):
        print(ba.get(_), end=", ")
