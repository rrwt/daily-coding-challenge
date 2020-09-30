"""
Given an undirected graph, determine if it contains a cycle.
"""
from dataclasses import dataclass
from typing import List


@dataclass
class Node:
    rank: int
    parent: int


def union(first: int, second: int, parents: List[Node]) -> None:
    parent_first = parents[first].parent
    parent_second = parents[second].parent
    rank_first = parents[first].rank
    rank_second = parents[second].rank

    if rank_first > rank_second:
        parents[parent_second].parent = parent_first
    elif rank_second > rank_first:
        parents[parent_first].parent = parent_second
    else:
        parents[parent_second].parent = parent_first
        parents[parent_first].rank += 1


def find(src: int, parents: List[Node]) -> int:
    if parents[src].parent != src:
        parents[src].parent = find(parents[src].parent, parents)

    return parents[src].parent


def is_cyclic(graph: List[List[int]]) -> bool:
    size = len(graph)

    parents = [Node(0, x) for x in range(size)]
    visited = set()

    for src, neighbors in enumerate(graph):
        for neighbor, connected in enumerate(neighbors):
            if connected and (neighbor, src) not in visited:
                parent_src = find(src, parents)
                parent_neighbor = find(neighbor, parents)

                if parent_src == parent_neighbor:
                    return True
                else:
                    union(parent_src, parent_neighbor, parents)
                    visited.add((src, neighbor))
                    visited.add((neighbor, src))

    return False


if __name__ == "__main__":
    assert is_cyclic([[0, 1, 1], [1, 0, 1], [1, 1, 0],]) is True
