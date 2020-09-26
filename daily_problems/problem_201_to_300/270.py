"""
A network consists of nodes labeled 0 to N. You are given a list of edges (a, b, t),
describing the time t it takes for a message to be sent from node a to node b.
Whenever a node receives a message, it immediately passes the message on to a
neighboring node, if possible.
Assuming all nodes are connected, determine how long it will take for every node
to receive a message that begins at node 0.

For example, given N = 6, and the following edges:
edges = [ (0, 1, 5), (0, 2, 3), (0, 5, 4), (1, 3, 8), (2, 3, 1), (3, 5, 10), (3, 4, 5) ]

You should return 9, because propagating the message
from 0 -> 2 -> 3 -> 4 will take that much time.
"""
import sys
from collections import defaultdict
from typing import List, Tuple


def construct_graph(edges: List[Tuple[int, int, int]]) -> dict:
    graph = defaultdict(list)

    for src, dst, wt in edges:
        graph[src].append((dst, wt))

    return graph


def get_next_source(min_dist: List[int], visited) -> int:
    src = 0
    min_val = sys.maxsize

    for node, dist in enumerate(min_dist):
        if node not in visited and dist < min_val:
            min_val = dist
            src = node

    return src


def propagation_time(edges: List[Tuple[int, int, int]], vertices: int) -> int:
    """
    Dijkstra's SP algorithm
    O(V*V)
    """
    min_dist = [sys.maxsize] * vertices
    graph = construct_graph(edges)

    min_dist[0] = 0
    visited = set()

    for _ in range(vertices - 1):
        src = get_next_source(min_dist, visited)
        src_wt = min_dist[src]
        visited.add(src)

        for neighbor, wt in graph[src]:
            if neighbor not in visited:
                min_dist[neighbor] = min(min_dist[neighbor], src_wt + wt)

    return max(min_dist)


if __name__ == "__main__":
    assert (
        propagation_time(
            [
                (0, 1, 5),
                (0, 2, 3),
                (0, 5, 4),
                (1, 3, 8),
                (2, 3, 1),
                (3, 5, 10),
                (3, 4, 5),
            ],
            6,
        )
        == 9
    )
