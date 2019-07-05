"""
Maximum edges that can be added to DAG so that is remains DAG

A DAG is given to us, we need to find maximum number of edges
that can be added to this DAG, after which new graph still remain
a DAG that means the reformed graph should have maximal number of
edges, adding even single edge will create a cycle in graph.
"""
from typing import List, Union, Tuple

from ds import GraphM  # type: ignore
from topological_sort import topological_sort_kahn_algorithm  # type: ignore


def add_edges_safely(graph: List[list], vertices: int) -> Tuple[List, int]:
    """
    Algorithm: Find a node with 0 in-degree and start there.
        All nodes with less in-degree can safely add an edge
        to all nodes with degrees less than them.
        For nodes with same in-degree, we can safely add a directed node in one direction.
    Solution from Kahn's algorithm can be used here
    time complexity: O(V+E)
    """
    sorted_vertices = topological_sort_kahn_algorithm(graph, vertices)
    res: list = []
    visited: set = set()

    for vertex in sorted_vertices:
        for inner_vertex, connected in enumerate(graph[vertex]):
            if connected not in (0, 1) and inner_vertex not in visited:
                res.append((vertex, inner_vertex))
                graph[vertex][inner_vertex] = 1
        visited.add(vertex)

    return res, len(res)


if __name__ == "__main__":
    graph = GraphM(6, "directed")

    graph.add_edge(4, 0)
    graph.add_edge(4, 1)
    graph.add_edge(5, 2)
    graph.add_edge(5, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)

    print(*add_edges_safely(graph.graph, graph.num_vertices))
