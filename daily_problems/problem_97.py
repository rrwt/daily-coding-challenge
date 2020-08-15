"""
Write a map implementation with a get function that lets
you retrieve the value of a key at a particular time.

It should contain the following methods:
    set(key, value, time): sets key to value for t = time.
    get(key, time): gets the key at t = time.

The map should work like this. If we set a key at a particular time,
it will maintain that value forever or until it gets set at a later time.
In other words, when we get a key at a time, it should return the value
that was set for that key set at the most recent time.

Consider the following examples:
    d.set(1, 1, 0) # set key 1 to value 1 at time 0
    d.set(1, 2, 2) # set key 1 to value 2 at time 2
    d.get(1, 1) # get key 1 at time 1 should be 1
    d.get(1, 3) # get key 1 at time 3 should be 2

    d.set(1, 1, 5) # set key 1 to value 1 at time 5
    d.get(1, 0) # get key 1 at time 0 should be null
    d.get(1, 10) # get key 1 at time 10 should be 1

    d.set(1, 1, 0) # set key 1 to value 1 at time 0
    d.set(1, 2, 0) # set key 1 to value 2 at time 0
    d.get(1, 0) # get key 1 at time 0 should be 2
"""
import sys
from typing import Optional, Tuple


class BSTNode:

    def __init__(self, data: Tuple[int, int]) -> None:
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self, root: Optional[BSTNode] = None) -> None:
        self.root = root

    def _insert_node(self, root_node: BSTNode, node: BSTNode) -> BSTNode:
        if not root_node:
            root_node = node
        elif node.data[0] > root_node.data[0]:
            root_node.right = self._insert_node(root_node.right, node)
        elif node.data[0] < root_node.data[0]:
            root_node.left = self._insert_node(root_node.left, node)
        else:
            root_node.data = node.data

        return root_node

    def insert(self, data: Tuple[int, int]) -> BSTNode:
        node = BSTNode(data)

        if not self.root:
            self.root = node
        else:
            self._insert_node(self.root, node)

        return self.root

    def _search(self, cur_node: BSTNode, min_time: int, max_time: int) -> Optional[Tuple[int, int]]:
        # return potential time and value combination
        if cur_node is None:
            return None

        if cur_node.data[0] > min_time and cur_node.left is not None:
            return self._search(cur_node.left, min_time, max_time)
        elif cur_node.data[0] < min_time and cur_node.right is not None:
            right_res= self._search(cur_node.right, min_time, cur_node.data[0])

            if right_res and right_res[0] <= min_time:
                return right_res

        return cur_node.data if cur_node.data[0] <= min_time else None

    def search(self, time: int) -> Optional[int]:
        res = self._search(self.root, time, sys.maxsize)
        return res[1] if res else None


class Map:

    def __init__(self):
        """
        _map = {key: value,  # value is a bst, where all nodes store [time, value] tuple}
        """
        self._map = {}

    def set(self, key, value, time):
        if key not in self._map:
            self._map[key] = BST()

        self._map[key].insert((time, value))

    def get(self, key, time) -> Optional[int]:
        if key in self._map:
            return self._map[key].search(time)
        return None


if __name__ == '__main__':
    d = Map()
    d.set(1, 1, 0)  # set key 1 to value 1 at time 0
    d.set(1, 2, 2)  # set key 1 to value 2 at time 2
    assert d.get(1, 1) == 1  # get key 1 at time 1 should be 1
    assert d.get(1, 3) == 2  # get key 1 at time 3 should be 2

    d = Map()
    d.set(1, 1, 5)  # set key 1 to value 1 at time 5
    assert d.get(1, 0) is None  # get key 1 at time 0 should be null
    assert d.get(1, 10) == 1  # get key 1 at time 10 should be 1

    d = Map()
    d.set(1, 1, 0)  # set key 1 to value 1 at time 0
    d.set(1, 2, 0)  # set key 1 to value 2 at time 0
    assert d.get(1, 0) == 2  # get key 1 at time 0 should be 2
