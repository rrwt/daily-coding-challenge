"""
Implement a 2D iterator class. It will be initialized with an array of arrays,
and should implement the following methods:
    next(): returns the next element in the array of arrays.
            If there are no more elements, raise an exception.
    has_next(): returns whether or not the iterator still has elements left.

For example,
    given the input [[1, 2], [3], [], [4, 5, 6]],
    calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.
"""
from typing import Iterator


class ArrayIterator:
    def __init__(self, arr: list) -> None:
        self.arr = arr
        self.generator = self._get_next()
        self.next_val = next(self.generator)

    def _get_next(self) -> Iterator:
        for arr in self.arr:
            for num in arr:
                yield num

    def next(self) -> int:
        val = self.next_val

        try:
            self.next_val = next(self.generator)
        except StopIteration:
            self.next_val = None

        return val

    def has_next(self) -> bool:
        return self.next_val is not None


if __name__ == "__main__":
    it = ArrayIterator([[1, 2], [3], [], [4, 5, 6]])

    for i in range(1, 7):
        assert it.has_next() is True
        assert it.next() == i

    assert it.has_next() is False
