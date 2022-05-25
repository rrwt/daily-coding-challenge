"""
Implement an lru (Least recently used) cache.
"""
from typing import Optional, Union

from .queue import Deque, DNode  # type: ignore


"""
There is a better solution using Ordered Dict.
See: other_problems/lru_cache.py
"""


class LRUCache:
    """
    LRU cache implementation.
    Least Recently used elements will be at the back of the queue.
    In case of overflow, pop out the lru element from the back.
    Use a dictionary/hash-table to keep track of existing cached elements.
    Using a deque for the queue implementation as it is easy to move around.
    """

    def __init__(self, size: int):
        self.queue: Deque = Deque(size)
        self.hash_table: dict = {}  # stores item, and it's pointer (for faster movements)

    def move_to_front(self, key: int, value: int):
        """
        Move the most recently accessed element to the front of the queue.
        time complexity: O(1)
        """
        self.delete(key)
        self.push(key, value)  # value can be different from original

    def push(self, key: int, value: int):
        """
        Push a new/existing element to the front of the queue
        time complexity: O(1)
        """
        if key in self.hash_table:
            self.move_to_front(key, value)
        else:
            try:
                self.queue.insert_front(key)
            except Exception:
                self.queue.remove_last()
                self.queue.enqueue(key)
            finally:
                self.hash_table[key] = {"value": value, "pointer": self.queue.front}

    def delete(self, key: int):
        """
        Delete an element from the queue
        time complexity: O(1)
        """
        pointer: DNode = self.hash_table[key]["pointer"]

        if pointer == self.queue.front:
            self.queue.dequeue()
        else:
            previous, next_ = pointer.previous, pointer.next
            if previous:
                previous.next = next_
            if next_:
                next_.previous = previous

        self.queue.count -= 1
        del self.hash_table[key]

    def get_first(self) -> Optional[Union[int, str]]:
        """
        Get the first item from the cache
        time complexity: O(1)
        """
        return self.queue.front.data if self.queue.front else None

    def get(self, key: int) -> Optional[Union[int, str]]:
        """
        Access some element from the list
        time complexity: O(1)
        """
        return self.hash_table[key]["value"] if key in self.hash_table else None

    def print_queue(self):
        """
        Print the entire queue
        time complexity: O(n)
        """
        head = self.queue.front

        if head:
            while head.next:
                print(head.data, end="->")
                head = head.next
            print(head.data)


if __name__ == "__main__":
    lru = LRUCache(3)
    lru.push(1, 1)
    lru.push(2, 2)
    lru.push(3, 3)
    lru.print_queue()
    lru.push(2, 2)
    lru.print_queue()
    lru.push(4, 4)
    lru.print_queue()
    lru.delete(2)
    lru.print_queue()
    lru.push(9, 9)
    lru.print_queue()
