"""
Design and implement a HitCounter class that keeps track of requests (or hits).
It should support the following operations:
    record(timestamp): records a hit that happened at timestamp
    total(): returns the total number of hits recorded
    range(lower, upper): returns the number of hits that occurred between
        timestamps lower and upper (inclusive)

Follow-up: What if our system has limited memory?
"""
import sys
from collections import defaultdict
from typing import Optional, Union


class CounterNodeNull:
    """Null Object"""

    def __init__(self) -> None:
        self.timestamp = -1
        self.left = None
        self.right = None
        self.count = 0


class CounterNode:
    def __init__(self, timestamp: int, parent: Optional["CounterNode"]) -> None:
        self.timestamp = timestamp
        self.left = CounterNodeNull()
        self.right = CounterNodeNull()
        self.parent = parent
        self.count = 1


class HitCounter:
    """
    This solution doesn't take memory constraint into account
    """

    def __init__(self) -> None:
        self.root = None
        self.timestamp_dict = defaultdict(CounterNode)
        self.max = -1
        self.min = sys.maxsize

    @staticmethod
    def update_parent_count(node) -> None:
        while node:
            node.count += 1
            node = node.parent

    def create_node(
        self,
        root: Union["CounterNode", "CounterNodeNull"],
        parent: Optional["CounterNode"],
        timestamp: int,
    ) -> "CounterNode":
        if not root or root.timestamp < 0:
            return CounterNode(timestamp, parent)
        else:
            if root.timestamp > timestamp:
                if root.left.timestamp > -1:
                    return self.create_node(root.left, root, timestamp)
                else:
                    root.left = CounterNode(timestamp, root)
                    return root.left
            elif root.timestamp < timestamp:
                if root.right.timestamp > -1:
                    return self.create_node(root.right, root, timestamp)
                else:
                    root.right = CounterNode(timestamp, root)
                    return root.right
            else:
                root.count += 1
                return root

    def record(self, timestamp: int) -> None:
        if timestamp in self.timestamp_dict:
            node = self.timestamp_dict[timestamp]
            node.count += 1
        else:
            node = self.create_node(self.root, None, timestamp)

            if self.root is None:
                self.root = node
            if node.timestamp < self.min:
                self.min = node.timestamp
            if node.timestamp > self.max:
                self.max = node.timestamp

            self.timestamp_dict[timestamp] = node

        self.update_parent_count(node.parent)

    def total(self) -> int:
        return self.root.count

    def find_common_parent(self, first_node, second_node) -> CounterNode:
        runner = self.root
        time_stamp_1 = first_node.timestamp
        time_stamp_2 = second_node.timestamp

        while runner:
            if runner.timestamp > time_stamp_1 and runner.timestamp > time_stamp_2:
                runner = runner.left
            elif runner.timestamp < time_stamp_1 and runner.timestamp < time_stamp_2:
                runner = runner.right
            else:
                return runner

    def range(self, lower: int, upper: int) -> int:
        while lower not in self.timestamp_dict and lower < self.max:
            lower += 1
        while upper not in self.timestamp_dict and upper > self.min:
            upper -= 1

        if upper < lower:
            raise ValueError("Upper limit cannot be lower than lower limit")

        first_node = self.timestamp_dict[lower]
        second_node = self.timestamp_dict[upper]
        common_parent = self.find_common_parent(first_node, second_node)

        # first <= common_parent <= second
        return common_parent.count - first_node.left.count - second_node.right.count


if __name__ == "__main__":
    hc = HitCounter()
    hc.record(3)
    hc.record(3)
    hc.record(1)
    hc.record(2)
    hc.record(2)
    hc.record(1)
    hc.record(1)
    hc.record(4)
    hc.record(7)
    hc.record(9)
    assert hc.total() == 10
    assert hc.range(3, 8) == 4
    assert hc.range(5, 8) == 1
    assert hc.range(1, 4) == 8
