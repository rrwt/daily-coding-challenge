"""
Find a mother vertex in a given directed graph.
Mother vertex: A vertex v such that all other vertices in G can be reached by a path from v.
"""
import math
from typing import Optional

from ds import GraphM  # type: ignore


def mother_vertex(g: GraphM) -> Optional[int]:
    """
    This solution works by elimination. If all the nodes can be visited by starting from a node i,
    then it means i is the mother vertex, if not, then neither i nor any of it's children can be
    a mother vertex.
    Using Kosaraju's Strongly connected component (SCC) algorithm
    time complexity: O(V+E)
    space complexity: O(V)
    """

    def dfs(vertex: int):
        nonlocal visited
        visited.add(vertex)

        for neighbor, _ in enumerate(g.graph[vertex]):
            if neighbor not in visited and _ < math.inf:
                dfs(neighbor)

    visited: set = set()
    v: int = 0

    for i in range(g.num_vertices):
        if i not in visited:
            dfs(i)
            v = i

    visited = set()
    dfs(v)

    if any(i not in visited for i in range(g.num_vertices)):
        return None

    return v


if __name__ == "__main__":
    g = GraphM(7, "directed")
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(0, 1)
    g.add_edge(4, 1)
    g.add_edge(6, 4)
    g.add_edge(5, 6)
    g.add_edge(5, 2)
    g.add_edge(6, 0)
    print("A mother vertex is", mother_vertex(g))
