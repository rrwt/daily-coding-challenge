from typing import Any, Optional, List


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self.capacity = 10
        self.size = 0
        self.container: List[Optional[Node]] = [None] * self.capacity

    def __make_hash(self, key: Any) -> int:
        return hash(key) % self.capacity

    def __setitem__(self, key, value):
        key_hash = self.__make_hash(key)
        if self.container[key_hash] is None:
            self.container[key_hash] = Node(key, value)
        else:
            runner = self.container[key_hash]

            while runner.next and runner.key != key:
                runner = runner.next

            if runner.key == key:
                runner.value = value
            else:
                runner.next = Node(key, value)

        self.size += 1

    def __getitem__(self, key):
        key_hash = self.__make_hash(key)
        runner = self.container[key_hash]

        if runner is None:
            raise KeyError(key)

        while runner and runner.key != key:
            runner = runner.next

        if not runner:
            raise KeyError(key)

        return runner.value

    def __delitem__(self, key):
        key_hash = self.__make_hash(key)
        runner = self.container[key_hash]
        if not runner:
            raise KeyError(key)

        prev = None
        while runner and runner.key != key:
            prev = runner
            runner = runner.next

        if runner.key == key:
            self.size -= 1
            if not prev:
                if runner.next:
                    runner.key = runner.next.key
                    runner.value = runner.next.value
                    prev = runner
                    runner = runner.next
                else:
                    self.container[key_hash] = None
                    del runner
                    return None

            prev.next = runner.next
            runner.next = None
            del runner

    def items(self):
        for c in self.container:
            while c:
                yield c.key, c.value
                c = c.next

    def keys(self):
        for c in self.container:
            while c:
                yield c.key
                c = c.next

    def values(self):
        for c in self.container:
            while c:
                yield c.value
                c = c.next


if __name__ == "__main__":
    h = HashTable()

    for _ in range(20):
        h[_] = _

    del h[2]

    for _ in range(20):
        try:
            print(_, h[_])
        except KeyError:
            print("KeyError", _)

    print("iterate items")
    for key, value in h.items():
        print(key, value)

    print("iterate keys")
    for key in h.keys():
        print(key)

    print("iterate values")
    for value in h.values():
        print(value)
