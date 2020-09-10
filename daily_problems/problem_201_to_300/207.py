"""
Given an undirected graph G, check whether it is bipartite.
Recall that a graph is bipartite if its vertices can be
divided into two independent sets, U and V,
such that no edge connects vertices of the same set.
"""
from typing import List


def dfs(
    graph: List[List[int]], vertex: int, cur_color: int, colors: List[int], visited: set
) -> bool:
    visited.add(vertex)
    colors[vertex] = cur_color
    next_color = 2 if cur_color == 1 else 1

    for neighbor, connected in enumerate(graph[vertex]):
        if connected and neighbor not in visited:
            is_bipartite = dfs(graph, neighbor, next_color, colors, visited)

            if is_bipartite is False:
                return is_bipartite

        elif connected and colors[neighbor] == cur_color:
            return False

    return True


def is_graph_bipartite(graph: List[List[int]], num_vertices: int) -> bool:
    """
    Using DFS
    let color = 1 and 2 for division
    BFS can also be used using queue instead of recursive stack
    Time Complexity: O(V+E)
    Space Complexity: O(E)
    """
    colors = [0] * num_vertices
    visited = set()

    for vertex in range(num_vertices):
        if vertex not in visited:
            is_bipartite = dfs(graph, vertex, 1, colors, visited)
            if is_bipartite is False:
                return False
    return True


if __name__ == "__main__":
    assert is_graph_bipartite(
        [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]], 4
    )
