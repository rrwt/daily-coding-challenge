"""
You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:
    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log.
                 `i` is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""
from collections import deque


class OrderDeque:
    """Using deque

    Time complexity: O(1) to append and O(1) to retrieve.
    """

    def __init__(self, n: int):
        self.log: deque = deque(maxlen=n)
        self.len = 0
        self.max_len = n

    def record(self, order_id: int):
        self.log.append(order_id)
        self.len = min(self.len + 1, self.max_len)

    def get_last(self, i: int) -> int:
        return self.log[i - 1] if i < self.len else -1


class OrderCircularBuffer:
    """Using circular buffer.

    Just overwrite the oldest entry.
    Time complexity: O(1) to append and O(1) to retrieve
    """

    def __init__(self, n: int):
        self.next_index: int = 0
        self.buffer_size = n
        self.log: list = [None] * n

    @staticmethod
    def get_next_index(current_index: int, buffer_size: int) -> int:
        return current_index + 1 if current_index < buffer_size - 1 else 0

    def record(self, order_id: int) -> None:
        self.log[self.next_index] = order_id
        self.next_index = self.get_next_index(self.next_index, self.buffer_size)

    def get_last(self, i: int) -> int:
        return self.log[(self.buffer_size + self.next_index - i) % self.buffer_size]


if __name__ == "__main__":
    o = OrderDeque(3)
    print(o.get_last(1))
    o.record(1000)
    o.record(2000)
    o.record(3000)
    o.record(4000)
    print(o.get_last(2))

    order = OrderCircularBuffer(3)
    print(order.get_last(1))
    order.record(1000)
    order.record(2000)
    order.record(3000)
    order.record(4000)
    print(order.get_last(1))
    print(order.get_last(2))
    print(order.get_last(3))
    order.record(5000)
    print(order.get_last(1))
    print(order.get_last(2))
    print(order.get_last(3))
    order.record(6000)
    print(order.get_last(1))
    print(order.get_last(2))
    print(order.get_last(3))
