"""
Find a mother vertex in a given directed graph.
Mother vertex: A vertex v such that all other vertices in G can be reached by a path from v.
"""
import math
from typing import Optional

from gfg.graphs.ds import GraphM  # type: ignore


def dfs(graph: list, vertex: int, visited: set) -> set:
    if vertex not in visited:
        visited.add(vertex)

        for neighbor, connected in enumerate(graph[vertex]):
            if neighbor not in visited and connected < math.inf:
                dfs(graph, neighbor, visited)

    return visited


def get_mother_vertex(graph: GraphM) -> Optional[int]:
    """
    This solution works by elimination. If all the nodes can be visited
    by starting from a node i, then it means i is the mother vertex,
    if not, then neither i nor any of it's children can be a mother vertex.
    Using Kosaraju's Strongly connected component (SCC) algorithm
    time complexity: O(V+E)
    space complexity: O(V)
    """

    visited = set()
    graph_list = graph.graph
    mother = None

    for vertex in range(graph.num_vertices):
        if vertex not in visited:
            visited = dfs(graph_list, vertex, visited)
            mother = vertex

    visited = set()
    dfs(graph_list, mother, visited)  # check if all others can reach from here

    if any(vertex not in visited for vertex in range(graph.num_vertices)):
        return None
    return mother


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
    print("A mother vertex is", get_mother_vertex(g))
