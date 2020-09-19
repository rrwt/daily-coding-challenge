"""
You are given an array of length 24, where each element represents
the number of new subscribers during the corresponding hour.
Implement a data structure that efficiently supports the following:
    update(hour: int, value: int): Increment the element at index hour by value.
    query(start: int, end: int): Retrieve the number of subscribers
        that have signed up between start and end (inclusive).

You can assume that all values get cleared at the end of the day,
and that you will not be asked for start and end values that wrap around midnight.
"""


class Subscribers:
    def __init__(self):
        self.array = [0] * 24

    def update(self, hour: int, value: int) -> None:
        self.array[hour - 1] += value

    def query(self, start: int, end: int) -> int:
        return sum(self.array[start - 1: end])


if __name__ == "__main__":
    # TODO: Segment Tree
    sub = Subscribers()
    sub.update(10, 10)
    sub.update(5, 10)
    sub.update(15, 10)
    sub.update(20, 10)
    sub.update(12, 10)
    assert sub.query(5, 15) == 40
