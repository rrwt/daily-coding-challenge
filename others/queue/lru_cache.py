"""
Implement an lru (Least recently used) cache.
"""
from typing import Optional
from collections import deque


class LRUCache:
    """
    LRU cache implementation.
    Least Recently used elements will be at the back of the queue.
    In case of overflow, pop out the lru element from the back.
    Use a dictionary/hash-table to keep track of existing cached elements.
    Using a deque for the queue implementation as it is easy to move around.
    Using a set to store reference to existing elements.

    Assumption: There is no key-value pair to be set/unset. In that case we'd need
        to implement a hash-table instead of a set
    """

    def __init__(self, maxlength: int):
        self.queue: deque = deque([], maxlength)
        self.set: set = set()

    def move_to_front(self, element: int):
        """
        Move the most recently accessed element to the front of the queue.
        time complexity: O(n) (because of remove operation)
        In my opinion, this can be improved if we store the pointer to value in the hash table
        """
        self.delete(element)
        self.push(element)

    def push(self, element: int):
        """
        Push a new/existing element to the front of the queue
        """
        if element in self.set:
            self.move_to_front(element)
        else:
            self.set.add(element)
            self.queue.appendleft(element)

    def delete(self, element: int):
        """
        Delete an element from the queue
        time complexity: O(n)
        """
        try:
            self.queue.remove(element)
            self.set.remove(element)
        except (ValueError, KeyError):
            print(f"element {element} not found")

    def getFirst(self) -> Optional[int]:
        """
        Get the first item from the cache
        time complexity: O(1)
        """
        return self.queue[0] if len(self.queue) else None

    def get(self, element: int):
        """
        Access some element from the list
        time complexity: O(n)
        """
        if element not in self.set:
            return False
        else:
            self.move_to_front(element)
            return True

    def print_queue(self):
        print("->".join(map(str, self.queue)))


if __name__ == "__main__":
    lru = LRUCache(3)
    lru.push(1)
    lru.push(2)
    lru.push(3)
    lru.print_queue()
    lru.push(2)
    lru.print_queue()
    lru.push(4)
    lru.print_queue()
    lru.delete(2)
    lru.print_queue()
    lru.push(9)
    lru.print_queue()
