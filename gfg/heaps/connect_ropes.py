"""
There are n ropes of different lengths, we need to connect these
ropes into one rope. The cost to connect two ropes is equal to sum of
their lengths. We need to connect the ropes with minimum cost.
"""
import heapq
from typing import List


def connect_cost(ropes: List[int]) -> int:
    length = len(ropes)

    if length == 0:
        return 0
    if length == 1:
        return ropes[0]

    heapq.heapify(ropes)
    rope = heapq.heappop(ropes)
    total = 0

    while ropes:
        element = heapq.heappop(ropes)
        total += rope + element
        rope += element

    return total


if __name__ == "__main__":
    assert connect_cost([4, 3, 2, 6]) == 29
