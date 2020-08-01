"""
Maximum edges that can be added to DAG so that is remains DAG

A DAG is given to us, we need to find maximum number of edges
that can be added to this DAG, after which new graph still remain
a DAG that means the reformed graph should have maximal number of
edges, adding even single edge will create a cycle in graph.
"""
from typing import List, Tuple

from gfg.graphs.ds import GraphM  # type: ignore
from gfg.graphs.topological_sort import topological_sort_kahn_algorithm  # type: ignore


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

    for src in sorted_vertices:
        for dest, connected in enumerate(graph[src]):
            if connected not in (0, 1) and dest not in visited:
                res.append((src, dest))
                graph[src][dest] = 1
        visited.add(src)

    return res, len(res)


if __name__ == "__main__":
    g = GraphM(6, "directed")
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    print(*add_edges_safely(g.graph, g.num_vertices))
