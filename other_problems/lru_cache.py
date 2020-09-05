"""
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache,
           otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
                  When the cache reached its capacity, it should invalidate
                  the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
    Could you do both operations in O(1) time complexity?
"""
from collections import OrderedDict
from typing import Optional


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.size = 0
        self.cache = OrderedDict()

    def get(self, key: int) -> Optional[int]:
        if key in self.cache:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            if self.cache[key] == value:
                self.get(key)
            else:
                del self.cache[key]
                self.cache[key] = value
        else:
            if self.size == self.capacity:
                for temp_key in self.cache.keys():  # delete first key from top
                    del self.cache[temp_key]
                    self.size -= 1
                    break

            self.cache[key] = value
            self.size += 1


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
