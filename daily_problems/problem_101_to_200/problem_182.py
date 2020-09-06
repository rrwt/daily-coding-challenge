"""
A graph is minimally-connected if it is connected and there is no edge
that can be removed while still leaving the graph connected.
For example, any binary tree is minimally-connected.

Given an undirected graph, check if the graph is minimally-connected.
You can choose to represent the graph as either an adjacency matrix or adjacency list.
"""
from typing import List


def is_cyclic(graph, cur_vertex, parent, visited) -> bool:
    """
    Detect cycle in an undirected graph using DFS.
    """
    visited.add(cur_vertex)

    for neighbor, connected in enumerate(graph[cur_vertex]):
        if connected and neighbor != parent:
            if neighbor in visited:
                return True
            else:
                has_cycle = is_cyclic(graph, neighbor, cur_vertex, visited)
                if has_cycle:
                    return True

    return False


def is_minimally_connected(graph: List[List[int]], num_vertices: int) -> bool:
    """
    1. Has no cycle.
    2. All nodes are connected
    """
    visited = set()

    has_cycle = is_cyclic(graph, 0, -1, visited)

    if has_cycle or len(visited) < num_vertices:
        # if num_vertices > len(visited), it means there is a disconnect in the graph.
        return False

    return True


if __name__ == "__main__":
    assert (
        is_minimally_connected(
            [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]], 4
        )
        is True
    )

    assert (
            is_minimally_connected(
                [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 0, 0]], 4
            )
            is False
    )

    assert (
            is_minimally_connected(
                [[0, 1, 1, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]], 4
            )
            is False
    )
