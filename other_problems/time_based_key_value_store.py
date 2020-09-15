"""
Time Based Key-Value Store
Create a time based key-value store class TimeMap, that supports two operations.
1. set(string key, string value, int timestamp)
    Stores the key and value, along with the given timestamp.

2. get(string key, int timestamp)
    Returns a value such that set(key, value, timestamp_prev) was called previously,
    with timestamp_prev <= timestamp.
    If there are multiple such values, it returns the one with the largest timestamp_prev.
    If there are no values, it returns the empty string ("").

Note: The timestamps for all TimeMap.set operations are strictly increasing.
"""
from collections import defaultdict
from typing import Tuple, List


class TimeMap:
    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # setting values in increasing order
        # otherwise insert in sorted order
        self.hashmap[key].append((timestamp, value))

    def bin_search(
        self, values: List[Tuple[int, str]], timestamp: int
    ) -> Tuple[int, str]:
        start, end = 0, len(values) - 1

        while start < end:
            mid = (start + end) >> 1

            if values[mid][0] == timestamp:
                return values[mid]
            elif values[mid][0] > timestamp:
                end = mid - 1
            else:
                start = mid + 1

        if values[start][0] <= timestamp:
            return values[start]
        elif start > 0 and values[start-1][0] <= timestamp:
            return values[start-1]

        return timestamp, ""

    def get(self, key: str, timestamp: int) -> str:
        # binary search the largest value, greater than or equal to the one we want
        if key in self.hashmap:
            return self.bin_search(self.hashmap[key], timestamp)[1]

        return ""


"""
["TimeMap","set","set","get","get","get","get","get"]
[[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
"""

if __name__ == "__main__":
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    assert tm.get("foo", 1) == "bar"
    assert tm.get("foo", 3) == "bar"
    tm.set("foo", "bar2", 4)
    assert tm.get("foo", 4) == "bar2"
    assert tm.get("foo", 5) == "bar2"

    tm2 = TimeMap()
    tm2.set("love", "high", 10)
    tm2.set("love", "low", 20)
    assert tm2.get("love", 5) == ""
    assert tm2.get("love", 10) == "high"
    assert tm2.get("love", 15) == "high"
    assert tm2.get("love", 20) == "low"
    assert tm2.get("love", 25) == "low"
