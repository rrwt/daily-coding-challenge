"""
Given an iterator with methods next() and hasNext(), create a wrapper iterator,
PeekableInterface, which also implements peek(). peek shows the next element
that would be returned on next().
"""


class PeekableInterface(object):
    def __init__(self, iterator) -> None:
        self.iterator = iterator
        self.has_next = True

        try:
            self.next_val = next(iterator)
        except StopIteration:
            self.has_next = False
            self.next_val = None

    def peek(self):
        return self.next_val

    def next(self):
        val = self.next_val

        if not self.has_next:
            raise StopIteration

        try:
            self.next_val = next(self.iterator)
        except StopIteration:
            self.has_next = False

        return val

    def hasNext(self) -> bool:
        return self.has_next


if __name__ == "__main__":
    iterator = iter([1, 2, 3])
    pi = PeekableInterface(iterator)

    for _ in range(1, 4):
        assert pi.hasNext() is True
        assert pi.next() == _

    try:
        pi.next()
    except StopIteration:
        print("expected exception was raise")
